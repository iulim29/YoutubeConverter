from tkinter import *
from tkinter import filedialog
from moviepy import  *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil
import os


#Fucntions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def mp42mp3(our_mp4_file):
    base, out = os.path.splitext(our_mp4_file)
    new_file = base + '.mp3'

    return new_file


def download_file_mp4():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    #downdload video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video,user_path)
    screen.title('Download Complete')

def download_file_mp3():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    # downdload video
    mp3_video = YouTube(get_link).streams.get_audio_only().download()
    #converting mp4 file to mp3
    print('abcd' + user_path)
    mp3_file = mp42mp3(mp3_video)

    # move file to selected directory
    #shutil.move(mp3_file, user_path)
    screen.title('Download Complete')




screen = Tk()
title = screen.title("Youtube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_image = PhotoImage(file='blob-icon-17339 (1).png')

#resizing image
logo_image = logo_image.subsample(2,2)
canvas.create_image(250, 80, image = logo_image)

#link field
link_field =Entry(screen,width=50)
link_label = Label(screen, text="Enter your download link:", font=('Arial', 15))

#select path for saving the file
path_label = Label(screen, text="Download Path",font=('Arial', 15))
select_btn = Button(screen, text="Select", command=select_path)

#add widgets to windows
canvas.create_window(250,170,window = link_label)
canvas.create_window(250,220,window = link_field)

canvas.create_window(250,270,window = path_label)
canvas.create_window(250,320,window = select_btn)

#download buttons
download_btn1 = Button(screen, text="MP4", command=download_file_mp4)
download_btn2 = Button(screen, text="MP3", command=download_file_mp3)
canvas.create_window(200,380, window=download_btn1)
canvas.create_window(300,380, window=download_btn2)



screen.mainloop()
