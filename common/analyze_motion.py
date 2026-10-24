#!/usr/bin/env python3
"""
common/analyze_motion.py
Tự động hóa Bước Phân Tích Chuyển Động Đối Thủ (Lyra Vance Local Workflow):
1. Tự động tìm file .mp4 trong projects/XX/doi-thu/ (nếu chưa có .mp4, tự đọc link YouTube từ file .md trong doi-thu/ và tải bằng uvx yt-dlp).
2. Dùng ffmpeg phát hiện toàn bộ các điểm cắt cảnh (Scene Cuts / Shots) từ đầu đến cuối video.
3. Xuất trọn bộ Lưới Khung Hình Tốc Độ Cao (High-FPS Motion Grids: 4 FPS - mỗi 0.25s 1 hình, 6x10 = 60 hình / 15 giây mỗi tấm) bao phủ 100% thời lượng video từ 00:00 đến hết bài vào projects/XX/doi-thu/grids/.
4. Xuất file projects/XX/doi-thu/motion_metadata.json ghi lại danh sách từng shot và danh sách các tấm grid để AI đọc toàn bộ 100% không bỏ sót giây nào.
"""

import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path


def find_or_download_video(target_dir: Path) -> Path:
    standard_mp4 = target_dir / "video.mp4"
    legacy_mp4 = target_dir / "competitor_video.mp4"
    if legacy_mp4.exists() and not standard_mp4.exists():
        legacy_mp4.rename(standard_mp4)
    if standard_mp4.exists():
        return standard_mp4

    video_exts = (".mp4", ".mov", ".mkv", ".webm")
    for f in sorted(target_dir.iterdir()):
        if f.is_file() and f.suffix.lower() in video_exts and not f.name.startswith("."):
            return f

    # Nếu chưa có file video, tìm URL hoặc Video ID trong file .md / .txt / .json của thư mục
    yt_url = None
    for f in sorted(target_dir.iterdir()):
        if f.is_file() and f.suffix.lower() in (".md", ".txt", ".json"):
            text = f.read_text(encoding="utf-8", errors="ignore")
            m_url = re.search(r"https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([A-Za-z0-9_-]{11})", text)
            if m_url:
                yt_url = m_url.group(0)
                break
            m_id = re.search(r"Video ID:\s*([A-Za-z0-9_-]{11})", text)
            if m_id:
                yt_url = f"https://www.youtube.com/watch?v={m_id.group(1)}"
                break

    if not yt_url:
        raise FileNotFoundError(f"Không tìm thấy file .mp4 hoặc link YouTube trong {target_dir}")

    out_mp4 = standard_mp4
    print(f"[analyze_motion] Đang tải video đối thủ từ {yt_url} -> {out_mp4} ...")
    import shutil
    ytdlp_cmd = ["yt-dlp"] if shutil.which("yt-dlp") else ["uvx", "yt-dlp"]
    cmd = ytdlp_cmd + [
        "-f",
        "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best",
        "--merge-output-format",
        "mp4",
        "-o",
        str(out_mp4),
        yt_url,
    ]
    subprocess.run(cmd, check=True)
    return out_mp4


def get_video_info(video_path: Path) -> dict:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,r_frame_rate,duration:format=duration",
        "-of",
        "json",
        str(video_path),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)
    stream = data.get("streams", [{}])[0]
    fmt = data.get("format", {})
    duration = float(stream.get("duration") or fmt.get("duration") or 0.0)
    fps_str = stream.get("r_frame_rate", "30/1")
    num, den = fps_str.split("/")
    fps = round(float(num) / float(den), 2) if float(den) else 30.0
    return {
        "width": int(stream.get("width", 1280)),
        "height": int(stream.get("height", 720)),
        "fps": fps,
        "duration_sec": round(duration, 2),
    }


def fmt_time(sec: float) -> str:
    m = int(sec // 60)
    s = sec - m * 60
    return f"{m:02d}:{s:04.1f}"


def fmt_time_slug(sec: float) -> str:
    m = int(sec // 60)
    s = int(sec % 60)
    return f"{m:02d}m{s:02d}s"


def detect_scenes(video_path: Path, duration: float, threshold: float = 0.25) -> list[dict]:
    cmd = [
        "ffmpeg",
        "-i",
        str(video_path),
        "-vf",
        f"select='gt(scene,{threshold})',showinfo",
        "-f",
        "null",
        "-",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    cuts = [0.0]
    for line in res.stderr.splitlines():
        if "Parsed_showinfo" in line and "pts_time:" in line:
            m = re.search(r"pts_time:([0-9.]+)", line)
            if m:
                t = round(float(m.group(1)), 2)
                if t - cuts[-1] >= 0.8:
                    cuts.append(t)
    if duration - cuts[-1] >= 0.5:
        cuts.append(round(duration, 2))
    else:
        cuts[-1] = round(duration, 2)

    shots = []
    for i in range(len(cuts) - 1):
        start_s = cuts[i]
        end_s = cuts[i + 1]
        shots.append(
            {
                "shot_index": i + 1,
                "start_sec": start_s,
                "end_sec": end_s,
                "start_time": fmt_time(start_s),
                "end_time": fmt_time(end_s),
                "duration_sec": round(end_s - start_s, 2),
            }
        )
    return shots


def generate_full_video_grids(
    video_path: Path,
    grids_dir: Path,
    duration: float,
    fps: int = 4,
    cols: int = 6,
    rows: int = 10,
    tile_w: int = 720,
) -> list[dict]:
    """
    Chia toàn bộ video từ 00:00 đến hết thành các tấm lưới liên tiếp (mặc định 4 FPS, 6x10 = 60 frames = 15 giây/grid).
    Mỗi ô chuẩn 720p (4320x4050 toàn tấm), cách nhau đúng 0.25 giây (1/4 giây).
    """
    grids_dir.mkdir(parents=True, exist_ok=True)
    for old_f in grids_dir.glob("grid_*.jpg"):
        old_f.unlink()

    frames_per_grid = cols * rows
    window_sec = frames_per_grid / fps  # 60 / 4 = 15.0s
    num_grids = math.ceil(duration / window_sec)
    grids_meta = []

    for idx in range(num_grids):
        start_sec = round(idx * window_sec, 2)
        end_sec = round(min((idx + 1) * window_sec, duration), 2)
        seg_dur = round(end_sec - start_sec, 2)
        if seg_dur <= 0.2:
            continue

        grid_name = f"grid_{idx + 1:02d}_{fmt_time_slug(start_sec)}_{fmt_time_slug(end_sec)}.jpg"
        out_path = grids_dir / grid_name

        vf = f"fps={fps},scale={tile_w}:-1,tile={cols}x{rows}"
        cmd = [
            "ffmpeg",
            "-y",
            "-ss",
            str(start_sec),
            "-t",
            str(seg_dur),
            "-i",
            str(video_path),
            "-vf",
            vf,
            "-frames:v",
            "1",
            "-update",
            "1",
            "-q:v",
            "2",
            str(out_path),
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        grids_meta.append(
            {
                "grid_index": idx + 1,
                "file": str(out_path),
                "start_sec": start_sec,
                "end_sec": end_sec,
                "start_time": fmt_time(start_sec),
                "end_time": fmt_time(end_sec),
                "fps": fps,
                "layout": f"{cols}x{rows} (tile_w={tile_w}px, mỗi hàng {cols} hình = {cols/fps:.1f}s, mỗi ô = {1/fps:.2f}s)",
            }
        )
    return grids_meta


def generate_shot_sheets(
    video_path: Path,
    shots_dir: Path,
    shots: list[dict],
    cols: int = 3,
    rows: int = 3,
    tile_w: int = 1280,
) -> list[dict]:
    """
    Trích xuất frame chính giữa của từng Shot ở độ phân giải gốc HD (1280x720) và ghép thành các tấm 3x3 (3840x2160 4K).
    Giúp soi chi tiết trang phục, chất liệu và gương mặt của từng cảnh nét gấp 12 lần so với lưới 6x10.
    """
    shots_dir.mkdir(parents=True, exist_ok=True)
    for old_f in shots_dir.glob("*.jpg"):
        old_f.unlink()

    temp_frames = []
    for s in shots:
        mid_sec = round((s["start_sec"] + s["end_sec"]) / 2.0, 2)
        frame_path = shots_dir / f"_tmp_shot_{s['shot_index']:03d}.jpg"
        cmd = [
            "ffmpeg",
            "-y",
            "-ss",
            str(mid_sec),
            "-i",
            str(video_path),
            "-vf",
            f"scale={tile_w}:-1",
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(frame_path),
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        if frame_path.exists():
            temp_frames.append((s, frame_path))

    per_sheet = cols * rows
    num_sheets = math.ceil(len(temp_frames) / per_sheet)
    sheets_meta = []

    for idx in range(num_sheets):
        batch = temp_frames[idx * per_sheet : (idx + 1) * per_sheet]
        if not batch:
            continue
        first_shot = batch[0][0]["shot_index"]
        last_shot = batch[-1][0]["shot_index"]
        sheet_name = f"shots_{idx + 1:02d}_shot{first_shot:02d}_to_shot{last_shot:02d}.jpg"
        out_path = shots_dir / sheet_name

        n = len(batch)
        if n == 1:
            import shutil
            shutil.copyfile(batch[0][1], out_path)
        else:
            inputs = []
            for _, fp in batch:
                inputs.extend(["-i", str(fp)])
            filter_in = "".join(f"[{i}:v]" for i in range(n))
            vf = f"{filter_in}xstack=inputs={n}:layout="
            layouts = []
            for i in range(n):
                r = i // cols
                c = i % cols
                x_expr = "0" if c == 0 else "+".join("w0" for _ in range(c))
                y_expr = "0" if r == 0 else "+".join("h0" for _ in range(r))
                layouts.append(f"{x_expr}_{y_expr}")
            vf += "|".join(layouts)

            cmd = ["ffmpeg", "-y"] + inputs + ["-filter_complex", vf, "-frames:v", "1", "-q:v", "2", str(out_path)]
            subprocess.run(cmd, capture_output=True, check=True)
        sheets_meta.append(
            {
                "sheet_index": idx + 1,
                "file": str(out_path),
                "shots_range": f"{first_shot}-{last_shot}",
                "layout": f"{cols}x{rows} @ {tile_w}px/tile",
            }
        )

    for _, fp in temp_frames:
        if fp.exists():
            fp.unlink()

    return sheets_meta


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 common/analyze_motion.py <raw_dir> [--force]")
        sys.exit(1)

    target_dir = Path(sys.argv[1]).resolve()
    force = "--force" in sys.argv
    if not target_dir.exists():
        print(f"Không tìm thấy thư mục: {target_dir}")
        sys.exit(1)

    video_path = find_or_download_video(target_dir)
    meta_path = target_dir / "motion_metadata.json"
    grids_dir = target_dir / "grids"
    shots_dir = target_dir / "shot_sheets"

    if not force and meta_path.exists() and any(grids_dir.glob("grid_*.jpg")) and any(shots_dir.glob("shots_*.jpg")):
        data = json.loads(meta_path.read_text(encoding="utf-8"))
        data["video_file"] = str(video_path)
        for s in data.get("shot_sheets", []):
            s["file"] = str(shots_dir / Path(s["file"]).name)
        for g in data.get("grids", []):
            g["file"] = str(grids_dir / Path(g["file"]).name)
        meta_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[analyze_motion] Đã có sẵn {len(data.get('shot_sheets', []))} shot_sheets & {len(data.get('grids', []))} grids tại {target_dir} (bỏ qua cắt lại).")
        return

    info = get_video_info(video_path)
    print(f"[analyze_motion] Video: {video_path.name} | {info['width']}x{info['height']} @ {info['fps']}fps | {info['duration_sec']}s")

    shots = detect_scenes(video_path, info["duration_sec"])
    durations = [s["duration_sec"] for s in shots]
    avg_shot = round(sum(durations) / len(durations), 2) if durations else 0.0

    grids_dir = target_dir / "grids"
    grids = generate_full_video_grids(video_path, grids_dir, info["duration_sec"], fps=4, cols=6, rows=10, tile_w=720)

    shots_dir = target_dir / "shot_sheets"
    shot_sheets = generate_shot_sheets(video_path, shots_dir, shots, cols=3, rows=3, tile_w=1280)

    report = {
        "video_file": str(video_path),
        "video_info": info,
        "shot_summary": {
            "total_shots": len(shots),
            "avg_shot_duration_sec": avg_shot,
            "min_shot_duration_sec": min(durations) if durations else 0.0,
            "max_shot_duration_sec": max(durations) if durations else 0.0,
        },
        "shot_sheets": shot_sheets,
        "grids": grids,
        "shots": shots,
    }

    meta_path = target_dir / "motion_metadata.json"
    meta_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[analyze_motion] Đã phát hiện {len(shots)} shots (trung bình {avg_shot}s/shot).")
    print(f"[analyze_motion] Đã xuất {len(shot_sheets)} tấm 4K Shot Sheets (3x3 @ 1280px/ô) tại: {shots_dir}")
    print(f"[analyze_motion] Đã xuất {len(grids)} tấm 4K High-FPS Grids (6x10 @ 720px/ô, 4320x4050) tại: {grids_dir}")
    print(f"[analyze_motion] Đã lưu metadata tại: {meta_path}")


if __name__ == "__main__":
    main()
