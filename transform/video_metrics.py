def calculate_video_metrics(video):

    views = video.get("views",0)
    likes = video.get("likes",0)
    comments = video.get("comments",0)


    if views > 0:

        engagement_rate = (
            (likes + comments) / views
        )

        like_ratio = (
            likes / views
        )

    else:

        engagement_rate = 0
        like_ratio = 0



    video["engagement_rate"] = round(
        engagement_rate * 100,2
    )


    video["like_ratio"] = round(
        like_ratio * 100,2
    )


    return video



def calculate_trend_score(video):


    views = video.get("views",0)

    likes = video.get("likes",0)

    comments = video.get("comments",0)


    engagement = video.get(
        "engagement_rate",
        0
    )


    score = (

        views * 0.5

        +

        likes * 0.3

        +

        comments * 0.2

        +

        engagement * 1000

    )


    video["trend_score"] = round(
        score,2
    )


    return video