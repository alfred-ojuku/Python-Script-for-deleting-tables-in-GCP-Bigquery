import pytube

video_url = input('Enter Url')

#creating an instance for the youtube video
video_instance = pytube.YouTube(video_url)
stream = video_instance.streams.get_highest_resolution()

#download
stream.download()