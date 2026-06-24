from googleapiclient.discovery import build
from config.config import KEY_API

youtube=build(
  "youtube",
  "v3",
  developerKey=KEY_API
)

def extract_channel(channel_id):
  response=youtube.channels().list(
    part="snippet,statistics",
    id=channel_id
  ).execute()

  item=response["items"][0]

  channels={
    "channel_id":
    channel_id,

    "name":
    item["snippet"]["title"],


    "subscribers":
    item["statistics"]["subscriberCount"],


    "views":
    item["statistics"]["viewCount"]


  }

  return channels