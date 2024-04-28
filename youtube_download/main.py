import youtube_downloader

# urls = (
#     "https://www.youtube.com/watch?v=mrKXrw8mLnk",
#     "https://www.youtube.com/watch?v=hhhbB1LpVTs",
#     "https://www.youtube.com/watch?v=Tqy3JAtBxwg",
#     "https://www.youtube.com/watch?v=wHm9Y9ehEo4"
# )

BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='
def get_video_url_from_user():
    url = input("Please enter your youtube video url: ")
    if not url.lower().startswith(BASE_YOUTUBE_URL):
        print("ERROR: Please enter your youtube video url")
        return get_video_url_from_user()
    return url

def add_videos_url():
    urls = []
    while True:
        print(
            """
            1- Add new Youtube video url
            2- Run download audio for videos
            """
        )
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        if choice == "1":
            url = get_video_url_from_user()
            urls.append(url)
        if choice == "2":
            break;
    return urls;

urls = add_videos_url()
while len(urls) == 0:
    urls = add_videos_url()

for url in urls:
    youtube_downloader.download_video(url)
