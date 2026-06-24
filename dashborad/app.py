import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)
import streamlit as st
import pandas as pd


from sqlalchemy import create_engine, text

from config.config import DATABASE_URL



engine = create_engine(
    DATABASE_URL
)



st.title("📊 YouTube Analytics Dashboard")



def load_videos():


    query = text("""

    SELECT *

    FROM videos

    ORDER BY trend_score DESC

    """)


    with engine.connect() as conn:

        df = pd.read_sql(
            query,
            conn
        )


    return df




videos = load_videos()



st.subheader("Top Trending Videos")


st.dataframe(
    videos
)



st.subheader("Total Videos")


st.metric(
    "Videos",
    len(videos)
)



st.subheader("Highest Views")


if len(videos)>0:


    max_views = videos["views"].max()


    st.metric(
        "Views",
        max_views
    )



st.subheader("Top 5 Videos")


top5 = videos.head(5)



st.bar_chart(

    top5.set_index("title")["views"]

)