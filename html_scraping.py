import os
import time
# cannot use this library because RYM does not
# allow requests not from a browser
# HTTP Error 503: Service Unavailable
# and it bans your IP
# import urllib.request
from pyautogui import press, hotkey
import pyperclip

# get .txt file names to put html into
html = []

for dirpath, dnames, fnames in os.walk("./html_album_links/"):
    for f in fnames:
        html.append(dirpath + f)


#read chart_links.txt for every genre link
f = open('./chart_links.txt', 'r')
chart_links = f.readlines()
f.close()


# switch to firefox
hotkey('alt', 'tab')
for cl in range(len(chart_links)):

    # put chart link in clipboard
    pyperclip.copy(chart_links[cl].replace('\n', ''))

    # open new tab and paste link from clipboard
    hotkey('ctrl', 't')
    hotkey('ctrl', 'l')
    hotkey('ctrl', 'v')
    press('enter')

    # give 5 seconds to load webpage
    time.sleep(5)

    hotkey('ctrl', 'u')
    # give 5 seconds to load source code (html)
    time.sleep(5)

    hotkey('ctrl', 'a')
    hotkey('ctrl', 'c')
    # give 3 seconds to copy to clipboard
    time.sleep(3)

    # close tabs
    hotkey('ctrl', 'w')
    hotkey('ctrl', 'w')
    time.sleep(2)

    # write html to respective .txt file
    print(html[cl])
    f = open(html[cl], 'w', encoding='utf-8')
    f.write(pyperclip.paste())
    f.close()

# prevent rateyourmusic.com from
# banning our IP for too many requests
# 15 sec for 35 genres = 9 minutes to complete