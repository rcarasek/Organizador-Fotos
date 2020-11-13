import os
from datetime import datetime
# https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/
# What is PIL/Pillow?   PIL (Python Imaging Library) adds many image processing features to Python. Pillow is a fork of PIL that adds some user-friendly features.

from PIL import Image

def folder_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')


def photo_shooting_date(file):
    photo = Image.open(file)
    info = getexif()
    if 36867 in info:
        date = info[36867]
        date = datetime.strftime(date, '%Y:%m:%d %h:%m:%s')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

print(folder_path_from_photo_date('IMG_1269.PNG'))

    
