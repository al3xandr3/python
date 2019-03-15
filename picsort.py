
from PIL import Image
from PIL.ExifTags import TAGS
import os
# import time
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


def picdate(path):
    res = ""
    try:
        dt = get_exif(path)['DateTimeOriginal']

        res = datetime.strptime(dt, "%Y:%m:%d %H:%M:%S")  # 'DateTimeDigitized'
    except Exception as ex:
        print(ex)
        res = ""
    return res


def isPic(path):
    file, ext = os.path.splitext(path)
    return ext.upper() in [".JPG", ".JPEG", ".PNG", ".NEF", ".TIFF"]


if __name__ == "__main__":
    import glob

    target = sys.argv[1]
    try:
        for file in glob.glob(target + "\\*"):
            if isPic(file):
                if picdate(file) != "":
                    dir = picdate(file).strftime("%Y-%m-%d")
                    if not(os.path.exists(dir)):
                        os.mkdir(picdate(file).strftime("%Y-%m-%d"))
                    os.rename(file, dir + '\\' + os.path.basename(file))
    except Exception as ex:
        print(file)
        # print dir + '\\' + os.path.basename(file)
        print(ex)
