def calculate_channel_metrics(channel):

  subscribers=int(channel.get("subscribers",0))
  views=int(channel.get("views",0))


  channel_score = (

        subscribers * 0.6

        +

        views * 0.4

    )


  channel["channel_score"] = round(
        channel_score,
        2
    )


  return channel  

