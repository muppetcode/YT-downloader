# Tkinter (GUI) and pytube
from tkinter import *
import pytube

root = Tk()
root.iconbitmap("Assets/downloader.ico")

video_list = list() # List that manages downloads
sucsessful_videos = list() # List that stores finsihed downloads

watermark = Label(root, text="YouTube Downloading Tool by muppet")
watermark.pack()

entry_field = Entry(root) # URL entry widget
entry_field.pack()
entry_field.insert(0, "Copy URL here")

queue_label = Label(root, text="Videos: 0")
queue_label.pack()

def set_queue_label():
    queue_label.config(text="Videos: {}".format(len(video_list)))

def add_video():
    if entry_field.get() == "" or entry_field.get() == "Copy URL here": # Checks that the entry isn't blank or the defualt value
        pass
    else:
        video_list.append(entry_field.get())
        entry_field.delete(0, END)
        set_queue_label()

def clear_queue():
    video_list.clear()
    set_queue_label()
    entry_field.delete(0, END)
    entry_field.insert(0, "Copy URL here")

def download_videos(): # I wouldn't change this too much
    for x, video in enumerate(video_list):
        try:
            v = pytube.YouTube(video) # pytube video object
            stream = v.streams.get_by_itag(22) # Only compatible resolution atm :(
            stream.download("Videos") # Places all videos in the 'Video' folder, feel free to change this
            finish_label = Label(root, text=("Finished video {}".format(x)))
            finish_label.pack()
            video_list.clear()
            set_queue_label()
            sucsessful_videos.append(video)
        except: # Python won't give a code error on invalid URLs or videos
            log_label = Label(root, text="Invalid URL or incompatible resolution")
            log_label.pack()
        finished_log_label = Label(root, text="Downloaded {} out of {} videos".format(len(sucsessful_videos), len(video_list)))
        finished_log_label.pack()
        video_list.clear()
        sucsessful_videos.clear()
        set_queue_label()

add_button = Button(root, text="Add to queue", command=add_video)
add_button.pack()

clear_button = Button(root, text="Clear", command=clear_queue)
clear_button.pack()

download_videos = Button(root, text="Download", command=download_videos)
download_videos.pack()

root.mainloop()
