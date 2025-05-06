import csv
import re
from pytubefix import YouTube
from collections import defaultdict
from datetime import datetime


def extract_youtube_url(comment):
    match = re.search(r"(https?://www\.youtube\.com/watch\?v=[\w\-]+)", comment)
    return match.group(1) if match else None


def parse_log(csv_path):
    channel_time = defaultdict(float)
    livestream_time = 0.0
    video_time = 0.0
    video_entries = []
    seen_urls = set()
    time_by_date = defaultdict(lambda: {"live": 0.0, "video": 0.0})

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Media Type"] != "Listening Time":
                continue

            url = extract_youtube_url(row["Comment"])
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)

            log_date_str = "Invalid date."
            try:
                log_datetime = datetime.strptime(row["Log Date"], "%Y-%m-%d %H:%M:%S")
                log_date_str = log_datetime.date().isoformat()
            except ValueError:
                print(f"[WARN] Invalid date format: {row['Log Date']}")

            try:
                print(f"[INFO] Fetching metadata for {url}")
                yt = YouTube(url)
                title = yt.title
                channel = yt.author
                is_live = yt.vid_info.get("videoDetails", {}).get(
                    "isLiveContent", False
                )
            except Exception as e:
                print(f"[WARN] Failed to fetch metadata for {url}: {e}")
                continue

            try:
                minutes = float(row["Amount Logged"])
            except ValueError:
                print(f"[WARN] Invalid time in row: {row['Amount Logged']}")
                continue

            channel_time[channel] += minutes
            if is_live:
                livestream_time += minutes
                time_by_date[log_date_str]["live"] += minutes
            else:
                video_time += minutes
                time_by_date[log_date_str]["video"] += minutes

            video_entries.append(
                {
                    "title": title,
                    "channel": channel,
                    "duration": f"{minutes:.1f} minutes",
                    "url": url,
                    "is_live": is_live,
                }
            )

    channel_time_minutes = sorted(
        channel_time.items(), key=lambda x: x[1], reverse=True
    )
    time_by_date_sorted = sorted(time_by_date.items(), key=lambda x: x[0])

    return {
        "channel_time_minutes": channel_time_minutes,
        "livestream_time_minutes": livestream_time,
        "video_time_minutes": video_time,
        "video_entries": video_entries,
        "time_by_date": time_by_date_sorted,
    }
