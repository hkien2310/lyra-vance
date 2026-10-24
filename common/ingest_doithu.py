#!/usr/bin/env python3
"""
common/ingest_doithu.py
Tự động hóa 100% việc nạp 1 hoặc nhiều link YouTube đối thủ vào thư viện doithu/<ten-kenh>/<ten-video>/raw/:
1. Kiểm tra nếu video_id đã tồn tại đầy đủ trong doithu/*/*/raw/ thì bỏ qua ngay (Idempotent).
2. Quét toàn bộ Metadata, Hidden Tags, Chapters, Description & Top 50 Comments (từ pool 100 top comments) bằng yt-dlp.
3. Tự động đặt tên thư mục theo chuẩn doithu/<ten-kenh>/<ten-video>/raw/ (chống trùng lặp slug).
4. Xuất raw/seo.md + raw/seo_metadata.json.
5. Tải ảnh bìa gốc độ phân giải cao nhất về raw/thumbnail.jpg.
6. Tải raw/video.mp4 (kèm phụ đề tiếng Anh nếu có), chạy analyze_audio.py (tạo raw/listen.mp3 + raw/audio_dsp.json) và analyze_motion.py (tạo raw/motion_metadata.json + shot_sheets/ + grids/).

Cách dùng:
    python3 common/ingest_doithu.py "<youtube_url_1>" ["<youtube_url_2>" ...]
    python3 common/ingest_doithu.py danh_sach_link.txt
"""

import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DOITHU_DIR = ROOT_DIR / "doithu"


def get_ytdlp_cmd() -> list[str]:
    return ["yt-dlp"] if shutil.which("yt-dlp") else ["uvx", "yt-dlp"]


def slugify(text: str, max_len: int = 75) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower().replace("đ", "d")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text or "video"


def make_video_slug(title: str) -> str:
    main_part = title.split("|")[0].strip()
    if len(main_part) < 6:
        main_part = title
    return slugify(main_part, max_len=75)


def fmt_num(n: int | None) -> str:
    if n is None:
        return "N/A"
    return f"{n:,}"


def fmt_time(sec: float | int | None) -> str:
    if sec is None:
        return "00:00"
    m, s = divmod(int(round(float(sec))), 60)
    return f"{m:02d}:{s:02d}"


def extract_urls(args: list[str]) -> list[tuple[str, str]]:
    """Trả về danh sách (video_id, url) duy nhất."""
    items = []
    pattern = re.compile(r"https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([A-Za-z0-9_-]{11})")
    for arg in args:
        p = Path(arg)
        if p.exists() and p.is_file():
            content = p.read_text(encoding="utf-8", errors="ignore")
            for m in pattern.finditer(content):
                vid = m.group(1)
                items.append((vid, f"https://www.youtube.com/watch?v={vid}"))
        else:
            for m in pattern.finditer(arg):
                vid = m.group(1)
                items.append((vid, f"https://www.youtube.com/watch?v={vid}"))
            if re.fullmatch(r"[A-Za-z0-9_-]{11}", arg.strip()):
                vid = arg.strip()
                items.append((vid, f"https://www.youtube.com/watch?v={vid}"))
    seen = set()
    unique = []
    for vid, u in items:
        if vid not in seen:
            seen.add(vid)
            unique.append((vid, u))
    return unique


def find_existing_video_dir(video_id: str) -> Path | None:
    """Tìm xem video_id đã được tải vào doithu/*/*/raw chưa."""
    if not DOITHU_DIR.exists():
        return None
    for meta_path in DOITHU_DIR.glob("*/*/raw/seo_metadata.json"):
        try:
            data = json.loads(meta_path.read_text(encoding="utf-8"))
            if data.get("video_id") == video_id:
                return meta_path.parent.parent
        except Exception:
            continue
    return None


def is_raw_complete(video_dir: Path) -> bool:
    raw_dir = video_dir / "raw"
    required = [
        raw_dir / "seo.md",
        raw_dir / "seo_metadata.json",
        raw_dir / "thumbnail.jpg",
        raw_dir / "video.mp4",
        raw_dir / "listen.mp3",
        raw_dir / "audio_dsp.json",
        raw_dir / "motion_metadata.json",
    ]
    if not all(f.exists() for f in required):
        return False
    if not any((raw_dir / "shot_sheets").glob("shots_*.jpg")):
        return False
    if not any((raw_dir / "grids").glob("grid_*.jpg")):
        return False
    return True


def fetch_youtube_info(url: str) -> dict:
    print(f"[ingest_doithu] Đang lấy Metadata, Tags, Chapters & Top Comments từ: {url} ...")
    cmd = get_ytdlp_cmd() + [
        "-J",
        "--no-playlist",
        "--write-comments",
        "--extractor-args",
        "youtube:max_comments=100,100,0,0;comment_sort=top",
        url,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def download_thumbnail(info: dict, out_jpg: Path) -> None:
    if out_jpg.exists() and out_jpg.stat().st_size > 1000:
        return
    thumb_url = info.get("thumbnail")
    thumbnails = info.get("thumbnails") or []
    for t in reversed(thumbnails):
        u = t.get("url", "")
        if u.startswith("http"):
            thumb_url = u
            break
    if not thumb_url:
        return
    print(f"[ingest_doithu] Đang tải ảnh bìa gốc -> {out_jpg.name} ...")
    subprocess.run(
        ["ffmpeg", "-y", "-i", thumb_url, "-frames:v", "1", "-q:v", "2", str(out_jpg)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )


def build_seo_files(info: dict, raw_dir: Path) -> None:
    video_id = info.get("id", "")
    url = f"https://www.youtube.com/watch?v={video_id}"
    title = info.get("title", "")
    channel = info.get("channel") or info.get("uploader") or ""
    subs = info.get("channel_follower_count")
    views = info.get("view_count")
    likes = info.get("like_count")
    comment_count = info.get("comment_count")
    upload_date = info.get("upload_date", "")
    if len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    duration = info.get("duration") or 0
    description = info.get("description") or ""
    tags = info.get("tags") or []
    categories = info.get("categories") or []
    chapters = info.get("chapters") or []

    hashtags = re.findall(r"#[A-Za-z0-9_]+", description)
    seen_ht = set()
    unique_hashtags = [h for h in hashtags if not (h.lower() in seen_ht or seen_ht.add(h.lower()))]

    raw_comments = info.get("comments") or []
    raw_comments_sorted = sorted(raw_comments, key=lambda c: int(c.get("like_count") or 0), reverse=True)[:50]
    top_comments = []
    for idx, c in enumerate(raw_comments_sorted, 1):
        author = c.get("author") or "user"
        text = (c.get("text") or "").strip().replace("\r\n", "\n")
        c_likes = int(c.get("like_count") or 0)
        top_comments.append({
            "rank": idx,
            "author": author,
            "likes": c_likes,
            "text": text,
        })

    clean_meta = {
        "video_id": video_id,
        "url": url,
        "title": title,
        "channel": channel,
        "channel_handle": info.get("uploader_id", ""),
        "channel_follower_count": subs,
        "view_count": views,
        "like_count": likes,
        "comment_count": comment_count,
        "upload_date": upload_date,
        "duration_sec": duration,
        "duration_formatted": fmt_time(duration),
        "categories": categories,
        "tags": tags,
        "hashtags": unique_hashtags,
        "chapters": chapters,
        "description": description,
        "top_comments": top_comments,
    }

    (raw_dir / "seo_metadata.json").write_text(
        json.dumps(clean_meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = [
        url,
        "",
        "=== YOUTUBE VIDEO DATA ===",
        "",
        f"TITLE: {title}",
        f"CHANNEL: {channel} ({fmt_num(subs)} subscribers)",
        f"VIEWS: {fmt_num(views)} views",
        f"LIKES: {fmt_num(likes)}",
        f"COMMENTS COUNT: {fmt_num(comment_count)}",
        f"UPLOADED: {upload_date}",
        f"DURATION: {fmt_time(duration)} ({duration}s)",
        "",
        "--- HIDDEN TAGS (KEYWORDS) ---",
        ", ".join(tags) if tags else "(Không đặt thẻ ẩn)",
        "",
        "--- CHAPTERS (MỐC THỜI GIAN) ---",
    ]
    if chapters:
        for ch in chapters:
            lines.append(f"{fmt_time(ch.get('start_time', 0))} - {fmt_time(ch.get('end_time', 0))} : {ch.get('title', '')}")
    else:
        lines.append("(Không chia Chapters tự động)")

    lines.extend([
        "",
        "--- DESCRIPTION ---",
        description,
        "",
        "--- HASHTAGS ---",
        " ".join(unique_hashtags) if unique_hashtags else "(Không có Hashtag)",
        "",
        f"--- TOP COMMENTS ({len(top_comments)}) ---",
    ])
    for c in top_comments:
        single_line_text = re.sub(r"\s+", " ", c["text"])
        lines.append(f"{c['rank']}. {c['author']} (❤️ {c['likes']}) — {single_line_text}")

    (raw_dir / "seo.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def resolve_target_video_dir(channel_slug: str, base_video_slug: str, video_id: str) -> Path:
    candidate = DOITHU_DIR / channel_slug / base_video_slug
    meta_file = candidate / "raw" / "seo_metadata.json"
    if meta_file.exists():
        try:
            existing_id = json.loads(meta_file.read_text(encoding="utf-8")).get("video_id")
            if existing_id and existing_id != video_id:
                return DOITHU_DIR / channel_slug / f"{base_video_slug}-{video_id.lower()}"
        except Exception:
            pass
    return candidate


def ingest_single_url(video_id: str, url: str, custom_out_dir: Path | None = None) -> Path:
    if custom_out_dir is not None:
        raw_dir = custom_out_dir.resolve()
        raw_dir.mkdir(parents=True, exist_ok=True)
        video_dir = raw_dir
    else:
        existing_dir = find_existing_video_dir(video_id)
        if existing_dir and is_raw_complete(existing_dir):
            print(f"[ingest_doithu] ĐÃ CÓ ĐỦ RAW cho {video_id} tại: {existing_dir} (Bỏ qua tải lại)")
            return existing_dir

        info = fetch_youtube_info(url)
        channel_name = info.get("channel") or info.get("uploader") or "unknown-channel"
        video_title = info.get("title") or info.get("id") or "video"

        channel_slug = slugify(channel_name, max_len=40)
        base_video_slug = make_video_slug(video_title)

        video_dir = existing_dir or resolve_target_video_dir(channel_slug, base_video_slug, video_id)
        raw_dir = video_dir / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

    if custom_out_dir is not None:
        info = fetch_youtube_info(url)

    print(f"[ingest_doithu] Thư mục đích: {raw_dir}")

    # 1. Lưu seo.md & seo_metadata.json
    build_seo_files(info, raw_dir)

    # 2. Tải thumbnail.jpg
    download_thumbnail(info, raw_dir / "thumbnail.jpg")

    # 3. Chạy analyze_motion.py (tự tải video.mp4 nếu chưa có, xuất motion_metadata.json, shot_sheets/, grids/)
    subprocess.run([sys.executable, str(ROOT_DIR / "common" / "analyze_motion.py"), str(raw_dir)], check=True)

    # 4. Chạy analyze_audio.py (tách listen.mp3 và xuất audio_dsp.json có tách từng bài theo Chapters)
    subprocess.run(
        [sys.executable, str(ROOT_DIR / "common" / "analyze_audio.py"), str(raw_dir)],
        stdout=subprocess.DEVNULL,
        check=True,
    )
    print(f"[ingest_doithu] HOÀN TẤT NẠP RAW: {video_dir}")
    return video_dir


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 common/ingest_doithu.py <youtube_url> [--out projects/XX/doi-thu]")
        sys.exit(1)

    args = sys.argv[1:]
    custom_out: Path | None = None
    filtered_args: list[str] = []
    i = 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            custom_out = Path(args[i + 1])
            i += 2
        else:
            filtered_args.append(args[i])
            i += 1

    items = extract_urls(filtered_args)
    if not items:
        print("Không tìm thấy đường link YouTube hợp lệ nào trong tham số đầu vào!")
        sys.exit(1)

    print(f"[ingest_doithu] Tìm thấy {len(items)} link YouTube cần xử lý.")
    completed = []
    failed = []
    for idx, (vid, u) in enumerate(items, 1):
        print(f"\n================ [{idx}/{len(items)}] {u} ================")
        try:
            v_dir = ingest_single_url(vid, u, custom_out_dir=custom_out)
            completed.append((vid, u, str(v_dir)))
        except Exception as e:
            print(f"[ingest_doithu] LỖI khi xử lý {u}: {e}", file=sys.stderr)
            failed.append((vid, u, str(e)))

    print(f"\n================ TỔNG KẾT ({len(completed)}/{len(items)} thành công) ================")
    for vid, u, c in completed:
        print(f" [OK] {vid} -> {c}")
    for vid, u, err in failed:
        print(f" [ERR] {vid} ({u}) -> {err}")


if __name__ == "__main__":
    main()
