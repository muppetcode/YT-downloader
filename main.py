from tkinter import *
import pytube
import os

root = Tk()
root.iconbitmap("assets/downloader.ico")
root.title("YouTube Downloader")

video_list = list() # List that manages downloads
sucsessful_videos = list() # List that stores finished downloads

watermark = Label(root, text="YouTube Downloading Tool by muppet")
watermark.pack()

def set_queue_label():
    queue_label.config(text="Videos: {}".format(len(video_list)))

def get_itag_value(itag):
    global itag_value
    itag_value = itag
    remove_start_page()
    create_download_page()

def create_download_page():
    global add_button
    global clear_button
    global download_button
    global queue_label
    global entry_field
    add_button = Button(root, text="Add", command=add_video, width=50, height=3)
    clear_button = Button(root, text="Clear", command=clear_queue, width=50, height=3)
    download_button = Button(root, text="Download", command=download_videos, width=50, height=3)
    entry_field = Entry(root, width=50) # URL entry widget
    queue_label = Label(root, text="Videos: 0")
    entry_field.pack()
    queue_label.pack()
    add_button.pack()
    clear_button.pack()
    download_button.pack()
    entry_field.insert(0, "Copy URL here")

def remove_download_page():
    entry_field.destroy()
    queue_label.destroy()
    add_button.destroy()
    clear_button.destroy()
    download_button.destroy()

def create_start_page():
    global resolution_button_18
    global resolution_button_22
    global resolution_button_137
    resolution_button_18 = Button(root, text="Resolution Itag: 18", command=lambda: get_itag_value(18), width=50, height=3)
    resolution_button_22 = Button(root, text="Resolution Itag: 22 (Most common)", command=lambda: get_itag_value(22), width=50, height=3)
    resolution_button_137 = Button(root, text="Resolution Itag: 137", command=lambda: get_itag_value(137), width=50, height=3)
    resolution_button_18.pack()
    resolution_button_22.pack()
    resolution_button_137.pack()

def remove_start_page():
    resolution_button_18.destroy()
    resolution_button_22.destroy()
    resolution_button_137.destroy()

def remove_log():
    try:
        finish_label.destroy()
        log_label.destroy()
        finished_log_label.destroy()
        continue_button.destroy()
    except:
        log_label.destroy()
        finished_log_label.destroy()
        continue_button.destroy()
    create_start_page()

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
            stream = v.streams.get_by_itag(itag_value)
            stream.download("Videos") # Places all videos in the 'Video' folder, will give option to change in the future
            global finish_label
            finish_label = Label(root, text=("Finished video {}".format(x)))
            finish_label.pack()
            set_queue_label()
            sucsessful_videos.append(video)
        except: # Python won't give a value error on invalid URLs or videos
            global log_label
            log_label = Label(root, text="ERROR: Invalid URL or incompatible resolution")
            log_label.pack()
        global finished_log_label
        finished_log_label = Label(root, text="Downloaded {} out of {} videos".format(len(sucsessful_videos), len(video_list)))
        finished_log_label.pack()
        video_list.clear()
        sucsessful_videos.clear()
        set_queue_label()
        remove_download_page()
        global continue_button
        continue_button = Button(root, text="Continue", command=remove_log, width=50, height=3)
        continue_button.pack()

create_start_page() # Starting page

root.mainloop()
