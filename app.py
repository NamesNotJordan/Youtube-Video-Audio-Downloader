import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        youtube_link = link.get()
        yt_object = YouTube(youtube_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
    except:
        print("Invalid link")
    print


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="Paste youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=20)

finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

download_btn = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_btn.pack()

#TODO: Add buttons for diffent download options


# Run app
app.mainloop()