# Download YouTube videos using Python
# https://twitter.com/clcoding/status/1543973091935940609

import pytube 

def get_youtubevideo(url, path):
    yt = pytube.YouTube(url)
    # download video in highest resolution, path is the storage path
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
    # How to set a desired video resolution, if one doesn't want to download the highest available resolution?
    # https://twitter.com/seyienei_meyase/status/1544105286729838592
    # mp3 format (not webm format)
    # yt.streams.filter(only_audio=True).order_by('abr').desc().first().download(path)
    # transform webm into mp3 without ffmpeg
    # yt.streams.filter(only_audio=True).order_by('abr').desc().first().download(path, filename_prefix=None, filename_extension='mp3')
    # progress bar for downloading
    yt.streams.filter(only_audio=True).order_by('abr').desc().first().download(path, progress=True)
    # Stream.download() got an unexpected keyword argument 'progress'
    

get_youtubevideo("https://www.youtube.com/watch?v=6JDpXFmkIAc", "leyouth")