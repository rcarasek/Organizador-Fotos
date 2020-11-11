import os
from datetime import datetime
from PIL import Image


def photo_shooting_date(file):
    photo = Image.open(file)
    info = getexif()
    if 36867 in info:
        date = info[36867]
        date = datetime.strftime(date, '%y:%m:%d %h:%m:%s')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

print(photo_shooting_date('cdfs.jpg'))

    
