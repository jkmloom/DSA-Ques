import requests
import random

def fetch_yt_video():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos?page=1&limit=10&query=javascript&sortBy=keep%20one%3A%20mostLiked%20%7C%20mostViewed%20%7C%20latest%20%7C%20oldest"
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        video = data['data']['data']
        select_video_from_list = video[random.randint(0,10)]
        items = select_video_from_list['items']
        video_id = items['id']
        content_title = items['snippet']['title']
        channel_title = items['snippet']['channelTitle']
        return video_id, content_title, channel_title
    else:
        raise Exception("Failed to fetch data!")

def main():
    try:
        video_id, title, channel = fetch_yt_video()
        print(f"ID: {video_id}\nTitle: {title}\nChannel: {channel}")
    except Exception as exc:
        print(str(exc))

if __name__ == "__main__":
    main()