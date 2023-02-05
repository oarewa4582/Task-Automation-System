import os
#one of python’s standard utility modules used to interact with the operating system
import shutil
#also one of python’s standard utility modules used to interact with files and their collections
from pathlib import Path

#create the defined dictionaries  
DIRECTORIES = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".pdf", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PYTHON": [".py"],
    "SQL": [".sql"]
 
}
#map the file formats with the directory 
formats_file = {format_file: directory
                for directory, formats_file in DIRECTORIES.items()
                for format_file in formats_file}

#map the extensions with the directory  
def sort_junk():
    ''' check for the existing directory for the same name we defined. 
    If the existing directory is found then it will continue or else a new directory is created. And it will categorize all the files based on the extension in the appropriate folder. '''
    for entry in os.scandir():
        if entry.is_dir():
            continue
        path_file = Path(entry)
        format_file = path_file.suffix.lower()
        if format_file in formats_file:
            directory_path = Path(formats_file[format_file])
            directory_path.mkdir(exist_ok=True)
            path_file.rename(directory_path.joinpath(path_file))
  
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass
  
if __name__ == "__main__":
    sort_junk()