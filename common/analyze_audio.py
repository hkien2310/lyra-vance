#!/usr/bin/env python3
"""
Local Audio Technical Analyzer for Lyra Vance Workflow (Step 01).
Usage:
    python3 common/analyze_audio.py <path_to_audio_or_video_or_dir>
"""

import json
import subprocess
import sys
from pathlib import Path
import librosa
import numpy as np

AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac"}
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm"}

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Krumhansl-Schmuckler key profiles
MAJOR_PROFILE = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MINOR_PROFILE = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])


def fmt_time(sec: float) -> str:
    m, s = divmod(int(round(sec)), 60)
    return f"{m}:{s:02d}"


def ensure_listen_mp3(input_path: Path) -> Path:
    """If input is video or oversized audio (>25MB), create a lightweight 128k mp3 for AI listening."""
    if input_path.suffix.lower() == ".mp3" and input_path.stat().st_size <= 25 * 1024 * 1024:
        return input_path
    out_mp3 = input_path.with_name(f"{input_path.stem}_listen.mp3")
    if not out_mp3.exists():
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(input_path), "-vn", "-ac", "2", "-ar", "44100", "-b:a", "128k", str(out_mp3)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
    return out_mp3


def detect_key(y: np.ndarray, sr: int) -> dict:
    y_harm = librosa.effects.harmonic(y)
    chroma = librosa.feature.chroma_cqt(y=y_harm, sr=sr, fmin=librosa.note_to_hz("C2"))
    chroma_vals = np.mean(chroma, axis=1)

    maj_norm = (MAJOR_PROFILE - MAJOR_PROFILE.mean()) / MAJOR_PROFILE.std()
    min_norm = (MINOR_PROFILE - MINOR_PROFILE.mean()) / MINOR_PROFILE.std()
    c_norm = (chroma_vals - chroma_vals.mean()) / (chroma_vals.std() + 1e-8)

    candidates = []
    for i in range(12):
        maj_corr = float(np.dot(c_norm, np.roll(maj_norm, i)) / 12)
        min_corr = float(np.dot(c_norm, np.roll(min_norm, i)) / 12)
        # Check third & seventh interval energy to distinguish Minor/Dorian from Major
        maj_3_7 = chroma_vals[(i + 4) % 12] + 0.5 * chroma_vals[(i + 11) % 12]
        min_3_7 = chroma_vals[(i + 3) % 12] + 0.5 * chroma_vals[(i + 10) % 12]
        if min_3_7 > maj_3_7 * 1.1:
            min_corr += 0.08
        candidates.append((f"{NOTE_NAMES[i]} Major", maj_corr))
        candidates.append((f"{NOTE_NAMES[i]} Minor", min_corr))

    candidates.sort(key=lambda x: x[1], reverse=True)
    top_notes = [NOTE_NAMES[idx] for idx in np.argsort(chroma_vals)[::-1][:5]]
    return {
        "primary_key": candidates[0][0],
        "confidence": round(candidates[0][1], 3),
        "secondary_key": candidates[1][0],
        "secondary_confidence": round(candidates[1][1], 3),
        "dominant_notes": top_notes,
    }


def analyze_file(target: Path) -> dict:
    listen_mp3 = ensure_listen_mp3(target)
    y, sr = librosa.load(str(listen_mp3), sr=22050, mono=True)
    duration = float(librosa.get_duration(y=y, sr=sr))

    # 1. Tempo & Beats
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    bpm = float(np.ndim(tempo) and tempo[0] or tempo)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    ibi = np.diff(beat_times)
    beat_stability = float(1.0 - min(1.0, np.std(ibi) / (np.mean(ibi) + 1e-6))) if len(ibi) > 2 else 0.0

    # 2. Key & Harmony
    key_info = detect_key(y, sr)

    # 3. Loudness & Dynamic Range
    rms = librosa.feature.rms(y=y)[0]
    rms_db = librosa.amplitude_to_db(rms, ref=1.0)
    mean_rms_db = float(np.mean(rms_db))
    peak_db = float(librosa.amplitude_to_db(np.array([np.max(np.abs(y))]), ref=1.0)[0])
    crest_factor_db = round(peak_db - mean_rms_db, 1)

    # 4. Frequency Balance (Spectral Energy Distribution)
    S = np.abs(librosa.stft(y)) ** 2
    freqs = librosa.fft_frequencies(sr=sr)
    total_energy = np.sum(S) + 1e-12
    bands = {
        "sub_bass_20_60Hz_pct": (20, 60),
        "bass_60_250Hz_pct": (60, 250),
        "low_mid_250_500Hz_pct": (250, 500),
        "mid_500_2000Hz_pct": (500, 2000),
        "high_mid_2k_6kHz_pct": (2000, 6000),
        "high_6k_plus_pct": (6000, sr // 2),
    }
    freq_profile = {
        name: round(float(np.sum(S[(freqs >= lo) & (freqs < hi), :]) / total_energy * 100), 1)
        for name, (lo, hi) in bands.items()
    }

    # 5. Structural Segmentation & Energy Arc
    n_segments = max(4, min(10, int(round(duration / 25))))
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    raw_frames = librosa.segment.agglomerative(mfcc, k=n_segments)
    raw_times = list(librosa.frames_to_time(raw_frames, sr=sr))
    bound_times = [0.0]
    for t in raw_times:
        if t - bound_times[-1] >= 4.0 and duration - t >= 4.0:
            bound_times.append(float(t))
    bound_times.append(duration)
    rms_times = librosa.frames_to_time(np.arange(len(rms)), sr=sr)

    max_rms = float(np.percentile(rms, 95)) + 1e-8
    min_rms = float(np.percentile(rms, 10))
    sections = []
    for i in range(len(bound_times) - 1):
        t0, t1 = bound_times[i], bound_times[i + 1]
        mask = (rms_times >= t0) & (rms_times < t1)
        sec_rms = float(np.mean(rms[mask])) if np.any(mask) else 0.0
        norm_e = max(0.0, min(1.0, (sec_rms - min_rms) / (max_rms - min_rms + 1e-8)))
        if norm_e >= 0.75:
            level = "High / Peak"
        elif norm_e >= 0.45:
            level = "Medium / Groove"
        else:
            level = "Low / Atmospheric"
        sections.append({
            "time_range": f"{fmt_time(t0)} - {fmt_time(t1)}",
            "duration_sec": round(t1 - t0, 1),
            "energy_score": round(norm_e, 2),
            "energy_level": level,
        })

    return {
        "source_file": str(target),
        "listen_file": str(listen_mp3),
        "duration_sec": round(duration, 1),
        "duration_formatted": fmt_time(duration),
        "tempo": {
            "bpm": round(bpm, 1),
            "bpm_rounded": int(round(bpm)),
            "half_time_bpm": round(bpm / 2, 1),
            "double_time_bpm": round(bpm * 2, 1),
            "beat_stability": round(beat_stability, 2),
        },
        "harmony": key_info,
        "dynamics_and_mix": {
            "mean_rms_db": round(mean_rms_db, 1),
            "peak_db": round(peak_db, 1),
            "crest_factor_db": crest_factor_db,
            "compression_character": (
                "Dense / Heavily Compressed (Club/Modern Pop)" if crest_factor_db < 11.0
                else "Balanced / Punchy Dynamic" if crest_factor_db < 15.0
                else "Wide Dynamic / Breathing & Cinematic"
            ),
            "frequency_energy_pct": freq_profile,
        },
        "energy_sections": sections,
    }


def resolve_input(path_str: str) -> Path:
    p = Path(path_str)
    if p.is_file():
        return p
    if p.is_dir():
        candidates = [
            f for f in sorted(p.iterdir())
            if f.suffix.lower() in (AUDIO_EXTS | VIDEO_EXTS) and not f.stem.endswith("_listen")
        ]
        if not candidates:
            raise FileNotFoundError(f"Không tìm thấy file nhạc/video trong thư mục: {p}")
        return candidates[0]
    raise FileNotFoundError(f"Không tìm thấy đường dẫn: {p}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 common/analyze_audio.py <file_or_folder_path>", file=sys.stderr)
        sys.exit(1)
    target_file = resolve_input(sys.argv[1])
    result = analyze_file(target_file)
    print(json.dumps(result, indent=2, ensure_ascii=False))
