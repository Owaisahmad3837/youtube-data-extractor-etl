from googleapiclient.discovery import build
from config.config import KEY_API


youtube=build(
  "youtube",
  "v3",
  developerKey=KEY_API
)

def  extract_playlist(channel_id):
  response=youtube.playlists().list(
    part="snippet",
    channelId=channel_id,
    maxResults=10
  ).execute()


  playlists=[]

  for item in response["items"]:
    playlist={
       "playlist_id":
            item["id"],


            "title":
            item["snippet"]["title"]
    }

    playlists.append(playlist)


  return playlists