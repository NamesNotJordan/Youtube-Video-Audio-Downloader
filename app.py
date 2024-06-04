import tkinter
import customtkinter
from pytube import YouTube


def video_download():
    try:
        youtube_link = link.get()
        yt_object = YouTube(youtube_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=video.title)
        video.download()
        finish_label.configure(text="Download Complete")
    except:
        finish_label.configure(text="Invalid link", text_color="red")

def audio_download():
    pass

# updates the progress bar and percent while downloading a video
def on_progress(stream, chunk, bytes_remaining):
    # Calculate progress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_complete = bytes_downloaded / total_size * 100
    # Update progress percent displayed
    progress_percent.configure(text=f"{int(percent_complete)}%")
    progress_percent.update()
    # Update progress bar
    progress_bar.set(float(percent_complete) / 100)


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

#Progress meter
progress_percent = customtkinter.CTkLabel(app, text="0%")
progress_percent.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.pack(padx=10, pady=10)

# buttons
video_download_button = customtkinter.CTkButton(app, text="Download", command=video_download)
video_download_button.pack()

download_audio_button = customtkinter.CTkButton(app, text="Download Audio Only", command= audio_download)
download_audio_button.pack()


# Run app
app.mainloop()