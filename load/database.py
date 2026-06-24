from sqlalchemy import create_engine, text
from config.config import DATABASE_URL


engine = create_engine(
    DATABASE_URL
)



def create_table():

    with engine.begin() as conn:

        conn.execute(text("""

        CREATE TABLE IF NOT EXISTS videos(

            video_id TEXT PRIMARY KEY,

            title TEXT,

            channel_id TEXT,

            views BIGINT,

            likes BIGINT,

            comments BIGINT,

            engagement_rate FLOAT,

            like_ratio FLOAT,

            trend_score FLOAT

        )

        """))

    print("Table created")




def insert_video(video):


    query = text("""


    INSERT INTO videos(

        video_id,

        title,

        channel_id,

        views,

        likes,

        comments,

        engagement_rate,

        like_ratio,

        trend_score

    )


    VALUES(

        :video_id,

        :title,

        :channel_id,

        :views,

        :likes,

        :comments,

        :engagement_rate,

        :like_ratio,

        :trend_score

    )


    ON CONFLICT(video_id)

    DO NOTHING


    """)



    with engine.begin() as conn:


        conn.execute(

            query,

            video

        )


    print("Video inserted")