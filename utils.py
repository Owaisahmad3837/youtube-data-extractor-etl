from urllib.parse import urlparse, parse_qs

# 🎥 Extract video ID from YouTube URL
def get_video_id(url):
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get("v")

    if video_id:
        return video_id[0]

    return None


# 📺 Extract channel ID (simple case)
def get_channel_id(url):
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Example: /channel/UCxxxx
    if "/channel/" in path:
        return path.split("/channel/")[1]

    return None