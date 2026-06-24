from extract.channel_extract import extract_channel
from extract.playlist_extract import extract_playlist
from extract.videos_extract import extract_videos

from transform.clean import transform
from load.json_loader import save_json


# -----------------------------
# INPUT
# -----------------------------
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Google Developers


# -----------------------------
# STEP 1: CHANNEL
# -----------------------------
channel = extract_channel(channel_id)


# -----------------------------
# STEP 2: PLAYLIST
# -----------------------------
playlist_id = channel["uploaded_playlist"]

video_ids = extract_playlist(playlist_id, limit=10)


# -----------------------------
# STEP 3: VIDEOS
# -----------------------------
videos = extract_videos(video_ids)


# -----------------------------
# BUILD RAW DATA
# -----------------------------
raw_data = {
    "channel": channel,
    "videos": videos
}


# -----------------------------
# TRANSFORM
# -----------------------------
clean_data = transform(raw_data)


# -----------------------------
# LOAD
# -----------------------------
save_json(clean_data)

print("ETL Completed 🚀")