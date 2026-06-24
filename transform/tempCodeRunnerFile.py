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


    videos = extract_video("python")


    print(
        "video extracted:",
        len(videos)
    )


    for video in videos:


        # temporary testing data
        video["views"] = 10000
        video["likes"] = 500
        video["comments"] = 100



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