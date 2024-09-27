import os


def convert_to_mp3(file_name, file_destination):
    new_file_name = file_name[:-3] + "mp3"
    os.system(f"ffmpeg -i {os.path.join(file_destination,file_name) } {file_destination}/{new_file_name}")