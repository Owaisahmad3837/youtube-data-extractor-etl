def transform(data):


    for video in data["videos"]:


        video["views"] = int(
            video["views"]
        )



    return data