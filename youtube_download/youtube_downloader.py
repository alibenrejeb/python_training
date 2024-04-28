import ssl
import ffmpeg
import os
from pytube import YouTube

# This restores the same behavior as before.
context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Progress of download for {stream.type}: {int(percent)}%")
    if int(percent) == 100:
        print("")

def download_video(url):
    yt = YouTube(url)
    yt.register_on_progress_callback(on_download_progress)

    streams = yt.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution').desc()
    video_stream = streams.first()
    streams = yt.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr').desc()
    audio_stream = streams.first()

    print(f"Download {yt.title}...")
    video_stream.download("videos")
    audio_stream.download("audios")
    print("")

    print("Make final video download...")
    video_stream_filename = os.path.join("videos", video_stream.default_filename)
    audio_stream_filename = os.path.join("audios", video_stream.default_filename)
    stream = ffmpeg.output(ffmpeg.input(video_stream_filename), ffmpeg.input(audio_stream_filename), video_stream.default_filename, vcodec="copy", acodec="copy", loglevel="quiet")
    ffmpeg.run(stream_spec=stream, overwrite_output=True)
    print("Done")

    os.remove(video_stream_filename)
    os.remove(audio_stream_filename)
    os.rmdir("videos")
    os.rmdir("audios")
