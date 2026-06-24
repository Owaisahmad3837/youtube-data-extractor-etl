from googleapiclient.discovery import build
from config.config import API_KEY

youtube = build("youtube", "v3", developerKey=API_KEY)


def extract_videos(video_ids):

    result = []

    response = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    ).execute()

    for video in response["items"]:

        result.append({
            "title": video["snippet"]["title"],
            "views": video["statistics"].get("viewCount"),
            "likes": video["statistics"].get("likeCount")
        })

    return result