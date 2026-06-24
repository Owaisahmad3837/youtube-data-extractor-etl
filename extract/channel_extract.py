from googleapiclient.discovery import build
from config.config import API_KEY

youtube = build("youtube", "v3", developerKey=API_KEY)


def extract_channel(channel_id):

    response = youtube.channels().list(
        part="snippet,statistics,contentDetails",
        id=channel_id
    ).execute()

    data = response["items"][0]

    return {
        "title": data["snippet"]["title"],
        "subscribers": data["statistics"].get("subscriberCount"),
        "views": data["statistics"].get("viewCount"),
        "uploaded_playlist": data["contentDetails"]["relatedPlaylists"]["uploads"]
    }