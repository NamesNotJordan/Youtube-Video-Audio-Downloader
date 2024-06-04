import tkinter
import customtkinter
from pytube import YouTube

DOWNLOAD_DEST = "/home/jayden/Downloads"

def video_download():
    progress_percent.configure(text="0%")
    progress_bar.set(0)
    finish_label.configure(text="")
    try:
        youtube_link = link.get()
        yt_object = YouTube(youtube_link, on_progress_callback=on_progress)
        
        video = yt_object.streams.get_highest_resolution()
        if audio_only_checkbox.get() == "on":
            video = yt_object.streams.get_audio_only()
        
        title.configure(text=video.title)
        video.download(DOWNLOAD_DEST)
        finish_label.configure(text="Download Complete")
    except:
        finish_label.configure(text="Invalid link", text_color="red")


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
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Audio only Check
audio_only_var = customtkinter.StringVar(value="off")
audio_only_checkbox = customtkinter.CTkCheckBox(app, text="Audio Only", variable=audio_only_var, onvalue="on", offvalue="off")
audio_only_checkbox.pack(padx=10, pady=10)
# button
video_download_button = customtkinter.CTkButton(app, text="Download", command=video_download)
video_download_button.pack()



# Run app
app.mainloop()