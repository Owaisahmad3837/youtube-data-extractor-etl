import os 

from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("Key_of_Youtube_API")

print(API_KEY)