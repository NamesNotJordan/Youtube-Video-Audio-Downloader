import os


def convert_single(file_name, source_folder, destination_folder, format:str):
    #new_file_name = file_name[:-3] + f".{format}"
    # Splits the file name from it's extension then adds the new extension
    new_file_name = os.path.splitext(file_name)[0] + f".{format}"
    os.system(f"ffmpeg -i {os.path.join(source_folder,file_name) } {destination_folder}/{new_file_name}")

def convert_batch(source_folder, destination_folder):
    pass