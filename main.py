from pytube import YouTube, Playlist
import tkinter as tk
import os

root = tk.Tk()
root.title("YT Music Downloader")
root.geometry("500x200")

entry = tk.Entry(root)
entry.pack()

def download_song():
	yt = YouTube(entry.get())
	video = yt.streams.filter(only_audio=True).first()
	out_file = video.download(output_path='./output')

	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)

def download_playlist():
	p = Playlist(entry.get())

	for video in p.videos:
		song = video.streams.filter(only_audio=True).first()
		out_file = song.download(output_path=f'./output/{p.title}')

		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)

download_song_btn = tk.Button(root, text="Download song", width=50, command=download_song)
download_song_btn.pack()

download_playlist_btn = tk.Button(root, text="Download playlist", width=50, command=download_playlist)
download_playlist_btn.pack()

root.mainloop()

