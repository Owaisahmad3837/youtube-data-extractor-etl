from googleapiclient.discovery import build
from config.config import API_KEY

youtube = build("youtube", "v3", developerKey=API_KEY)


def extract_playlist(playlist_id, limit=10):

    videos = []

    response = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=limit
    ).execute()

    for item in response["items"]:
        videos.append(item["contentDetails"]["videoId"])

    return videos