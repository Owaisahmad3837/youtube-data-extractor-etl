from googleapiclient.discovery import build
import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from config.config import KEY_API
youtube=build(
  "youtube",
  "v3",
  developerKey=KEY_API
)

def extract_video(keyword):
  response=youtube.search().list(
    part="snippet",
    q=keyword,
    type="video",
    maxResults=10
  ).execute()


  videos=[]

  for item in response["items"]:

    video={

      "video_id":
      item["id"]["videoId"],

      "title":
      item["snippet"]["title"],

      "channel_id":
      item["snippet"]["channelId"],


      "channel_title":
      item["snippet"]["channelTitle"]      

    }

  videos.append(video)

  return videos
