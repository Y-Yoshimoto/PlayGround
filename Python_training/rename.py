# config: UTF-8
import sys
import os
import re

a=1
files = os.listdir('./')
for file in files:
    png = re.compile("png")
    if png.search(file):
        os.rename(file, "IMG%02d.png" %(a))
        a+=1
    else:
        pass
