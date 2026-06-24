from googleapiclient.discovery import build

from config.config import KEY_API



youtube = build(
    "youtube",
    "v3",
    developerKey=KEY_API
)



def extract_video_stats(video_id):


    response = youtube.videos().list(

        part="statistics",

        id=video_id

    ).execute()



    item = response["items"][0]


    stats = item["statistics"]


    video_stats = {


        "views": int(
            stats.get("viewCount",0)
        ),


        "likes": int(
            stats.get("likeCount",0)
        ),


        "comments": int(
            stats.get("commentCount",0)
        )

    }


    return video_stats