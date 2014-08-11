
from PIL import Image
from PIL.ExifTags import TAGS
import os
import time
from datetime import datetime

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
# get_exif(path).keys()
# pic = get_exif(path)
# pic['DateTimeOriginal']
# pic['DateTimeDigitized']

def picDate (path):
    res = ""
    try:
        res = datetime.strptime(get_exif(path)['DateTimeDigitized'], "%Y:%m:%d %H:%M:%S")
    except:
        #res = get_exif(path)['DateTimeDigitized']
        res = ""
    try:
        res = datetime.strptime(get_exif(path)['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
    except:
        res = ""
    return res

def isPic (path):
    file, ext = os.path.splitext(path)
    return (ext.upper() in [".JPG",".JPEG",".PNG",".AVI",".WAV",".NEF",".MOV",".TIFF"])
