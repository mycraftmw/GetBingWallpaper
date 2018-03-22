#!/usr/bin/python
import os
import sys
import urllib.request
import xml.dom.minidom
bingUrl = "https://www.bing.com"
xmlUrl = "/HPImageArchive.aspx?idx=0&n=1"
enUrl = "&ensearch=1"
finalUrl = bingUrl + xmlUrl

if len(sys.argv) > 1 and sys.argv[1] == 'en':
    finalUrl += enUrl

data = urllib.request.urlopen(finalUrl).read().decode(encoding="utf8")
# print(data)
dom = xml.dom.minidom.parseString(data)

picUrl = dom.getElementsByTagName(
    "urlBase")[0].firstChild.data + "_1920x1080.jpg"

pic = urllib.request.urlopen(bingUrl + picUrl).read()

picDate = dom.getElementsByTagName("enddate")[0].firstChild.data

picName = dom.getElementsByTagName("urlBase")[0].firstChild.data.split(
    "/")[-1] + "_" + picDate + ".jpg"
print(picName)

with open("/home/yuetongyu/Pictures/" + picName, "wb") as f:
    f.write(pic)

os.system(
    'gsettings set org.gnome.desktop.background picture-uri file:///home/yuetongyu/Pictures/'
    + picName)

os.system(
    'gsettings set org.gnome.desktop.screensaver picture-uri file:///home/yuetongyu/Pictures/'
    + picName)
