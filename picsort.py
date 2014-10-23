
from PIL import Image
from PIL.ExifTags import TAGS
import os
import time
from datetime import datetime
import sys


# reference: http://al3xandr3.github.io/picture-organizer.html

def get_exif(path):
    ret = {}
    i = Image.open(path)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def picDate (path):
    res = ""
    try:
        res = datetime.strptime(get_exif(path)['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S") # 'DateTimeDigitized'
    except:
        res = ""
    return res

def isPic (path):
    file, ext = os.path.splitext(path)
    return (ext.upper() in [".JPG",".JPEG",".PNG",".NEF",".TIFF"])

if __name__ == "__main__":
    import glob
    for file in glob.glob('*'):
        if isPic(file):
            if picDate(file) != "":
                dir = picDate(file).strftime("%Y-%m-%d")
                if not(os.path.exists(dir)):
                    os.mkdir(picDate(file).strftime("%Y-%m-%d"))
                os.rename(file, dir + '/' + file)
        else: 
            sys.exit("Place this in the folder with the images to sort, then: python picsort.py")
