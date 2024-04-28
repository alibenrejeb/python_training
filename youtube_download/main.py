import youtube_downloader

urls = (
    "https://www.youtube.com/watch?v=mrKXrw8mLnk",
    "https://www.youtube.com/watch?v=hhhbB1LpVTs",
    "https://www.youtube.com/watch?v=Tqy3JAtBxwg",
    "https://www.youtube.com/watch?v=wHm9Y9ehEo4"
)

for url in urls:
    youtube_downloader.download_video(url)
