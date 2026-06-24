import os
from dotenv import load_dotenv
load_dotenv()

KEY_API=os.getenv("youtube_api_key")


DATABASE_URL=os.getenv("DATABASE_URL")