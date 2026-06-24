from extract.video_stats import extract_video_stats
from extract.videos import extract_video

from transform.video_metrics import (
    calculate_trend_score,
    calculate_video_metrics
)

from load.database import (
    create_table,
    insert_video
)



def main():

    create_table()


    videos = extract_video("hero")


    print(
        "video extracted:",
        len(videos)
    )


    for video in videos:

        stats=extract_video_stats(
            video["video_id"]
        )
        video.update(stats)
        # FIRST calculate metrics
        video = calculate_video_metrics(
            video
        )


        # SECOND calculate trend
        video = calculate_trend_score(
            video
        )


        print(video)


        insert_video(
            video
        )


        print(
            "Loaded:",
            video["title"]
        )




if __name__ == "__main__":

    main()