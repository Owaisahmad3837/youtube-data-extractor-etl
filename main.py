import json
from utils import get_video_id, get_channel_id
from extract import get_video_data, get_channel_data
import os

os.makedirs("output", exist_ok=True)

# 🎥 INPUT
video_url = input("Enter YouTube video URL: ")
channel_url = input("Enter YouTube channel URL: ")

# -----------------------
# VIDEO FLOW
# -----------------------
video_id = get_video_id(video_url)

if video_id:
    video_data = get_video_data(video_id)

    with open("output/video.json", "w", encoding="utf-8") as f:
        json.dump(video_data, f, indent=4)

    print("✅ Video data saved!")
else:
    print("❌ Invalid video URL")


# -----------------------
# CHANNEL FLOW
# -----------------------
channel_id = get_channel_id(channel_url)

if channel_id:
    channel_data = get_channel_data(channel_id)

    with open("output/channel.json", "w", encoding="utf-8") as f:
        json.dump(channel_data, f, indent=4)

    print("✅ Channel data saved!")
else:
    print("❌ Invalid channel URL")