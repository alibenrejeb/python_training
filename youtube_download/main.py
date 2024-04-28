import ssl
from pytube import YouTube

BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='
# This restores the same behavior as before.
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Progress of download: {int(percent)}%")

def get_video_url_from_user():
    url = input("Please enter your youtube video url: ")
    # if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
    if not url.lower().startswith(BASE_YOUTUBE_URL):
        return get_video_url_from_user()
        print("ERROR: Please enter your youtube video url")
    return url

def get_video_stream_itag_from_user(streams):
    i = 1
    for stream in streams:
        print(f"{i}- {stream.resolution}")
        i+=1

    while True:
        index_stream = input("Enter the resolution who you want to download: ")
        if index_stream == "":
            print("ERROR: you must enter a resolution to download")
        else:
            try:
                index_stream = int(index_stream)
            except:
                print("ERROR: you must enter an integer choice")
            else:
                if not 1 <= index_stream <= len(streams):
                    print(f"ERROR: you must enter un number between 1 and {len(streams)}")
                else:
                    break;

    return streams[int(index_stream)-1].itag

def get_details_youtube(yt):
    print("Title: ", yt.title)
    print("Number of views:", yt.views)
    # audio_stream = yt.streams.filter(only_audio=True).first()

# url = "https://www.youtube.com/watch?v=hhhbB1LpVTs"
# url = "https://www.youtube.com/watch?v=o9cSL3yHA20"
url = get_video_url_from_user()

yt = YouTube(url)
yt.register_on_progress_callback(on_download_progress)

streams = yt.streams.filter(progressive=True, file_extension='mp4')
tag_stream = get_video_stream_itag_from_user(streams)
stream = yt.streams.get_by_itag(tag_stream)
# stream = yt.streams.get_highest_resolution()
print("Download...")
stream.download()
print("Done")

