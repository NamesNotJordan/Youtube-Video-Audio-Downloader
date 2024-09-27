import os


def convert_to_mp3(file_name,source_folder, destination_folder):
    new_file_name = file_name[:-3] + "mp3"
    os.system(f"ffmpeg -i {os.path.join(source_folder,file_name) } {destination_folder}/{new_file_name}")