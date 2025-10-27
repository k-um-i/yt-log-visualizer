import pandas as pd
import re
from pytubefix import YouTube
import time
import os

CACHE_FILE = "metadata_cache.csv"

def extract_video_id(url: str):
    """Extract video ID from a YouTube URL or text."""
    if not isinstance(url, str):
        return None
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None


def fetch_metadata(video_id: str):
    """Fetch title, channel, duration, and livestream status from YouTube."""
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        is_live = yt.vid_info.get("videoDetails", {}).get("isLiveContent", False)
        return {
            "Video ID": video_id,
            "Title": yt.title,
            "Channel": yt.author,
            "Duration": yt.length / 60.0,  # minutes
            "Type": "Livestream" if is_live else "Video",
        }
    except Exception:
        return {
            "Video ID": video_id,
            "Title": None,
            "Channel": None,
            "Duration": None,
            "Type": None,
        }


def load_metadata_cache():
    if os.path.exists(CACHE_FILE):
        return pd.read_csv(CACHE_FILE)
    else:
        return pd.DataFrame(columns=["Video ID", "Title", "Channel", "Duration", "Type"])


def save_metadata_cache(df):
    df.to_csv(CACHE_FILE, index=False)


def update_metadata_cache(video_ids):
    """Fetch and cache metadata for any new videos."""
    cache = load_metadata_cache()
    known_ids = set(cache["Video ID"])
    new_ids = [vid for vid in video_ids if vid not in known_ids and isinstance(vid, str)]

    if new_ids:
        new_entries = []
        for vid in new_ids:
            meta = fetch_metadata(vid)
            new_entries.append(meta)
            time.sleep(0.5) # Rate limit

        new_df = pd.DataFrame(new_entries)
        cache = pd.concat([cache, new_df], ignore_index=True)
        save_metadata_cache(cache)

    return cache


def load_youtube_log(file) -> pd.DataFrame:
    """Load YouTube log CSV and merge metadata."""
    df = pd.read_csv(file)
    df = df.rename(columns=lambda c: c.strip())

    if "Log Date" in df.columns:
        df["Log Date"] = pd.to_datetime(df["Log Date"], errors="coerce")

    if "Amount Logged" in df.columns:
        df["Amount Logged"] = pd.to_numeric(df["Amount Logged"], errors="coerce")

    if "Comment" in df.columns:
        df["Video ID"] = df["Comment"].apply(extract_video_id)

    df = df.dropna(subset=["Log Date", "Amount Logged", "Video ID"])

    # Merge cached metadata
    cache = update_metadata_cache(df["Video ID"].unique())
    df = df.merge(cache, on="Video ID", how="left")

    return df

