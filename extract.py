from googleapiclient.discovery import build
from config import API_KEY

# 🔌 create YouTube connection
youtube = build("youtube", "v3", developerKey=API_KEY)


# 🎥 Extract video data
def get_video_data(video_id):
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )

    response = request.execute()
    return response


# 📺 Extract channel data
def get_channel_data(channel_id):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )

    response = request.execute()
    return response