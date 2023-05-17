from pytube import YouTube 
from pytube import Playlist 
  
#where to save 
SAVE_PATH = "Neso_OS" 
  
#link of the video to be downloaded 
links = input("Enter URL >> ")
i = 1
try:
    # yt = YouTube(link)
    playlist = Playlist(links)
    PlayListLinks = playlist.video_urls
    N = len(PlayListLinks)
    #print('Number of videos in playlist: %s' % len(PlayListLinks))

    print(f"This link found to be a Playlist Link with number of videos equal to {N} ")
    print(f"\n Lets Download all {N} videos")

    for j,link in enumerate(PlayListLinks):
        yt = YouTube(link)
        mp4_files = yt.streams.filter(file_extension="mp4")
        mp4_720p_files = mp4_files.get_by_resolution("720p")
        title = yt.title
        mp4_720p_files.download(SAVE_PATH,filename=str(i)+'.'+title) 
        print(j+1, ' Video is Downloaded.')
        i = i + 1

except Exception as e: 
    print("ERROR: ", e) 