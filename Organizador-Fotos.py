# Installing
# A step by step series of examples that tell you how to get a development env running 
# Install Python 3.x with pip
# Install Pillow, a Python Imaging Library
# pip install Pillow
# Install PyInstaller, to generate .exe file (for Windows)
# pip install pyinstaller

import os
from datetime import datetime
from PIL import Image

def folder_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date

def photo_shooting_date(file):
    photo = Image.open(file)
    info = photo._getexif()
    print(info)
    return info

print(folder_path_from_photo_date('IMG_1269.PNG'))
  
