import os
import time
import re
# import urllib.request
# cannot use this library because RYM does not
# allow requests not from a browser
# HTTP Error 503: Service Unavailable
# and it bans your IP
from pyautogui import press, hotkey
import pyperclip
import random
import sys

# If an IP block happens mid-scrape, this can re-do the albums
# that could not be accessed at the time

# html files are used for naming song .txt files
# and knowing album links
html = []

for dirpath, dnames, fnames in os.walk("./html_album_links/"):
    for f in fnames:
        html.append(dirpath + f)

# switch to firefox
# must do before loop to 
# avoid going back to program
hotkey('alt', 'tab')

for gen_num in range(len(html)):

    f = open('./Songs/' + html[gen_num].replace('./html_album_links/', ''), 'r', encoding='utf-8')

    Songs = f.readlines()

    f.close()

    for ml in range(len(Songs)):

        # only correct songs where this tag indicates a problem
        # else do nothing
        if (re.search('problem finding top song', Songs[ml]) != None):
            # put chart link in clipboard
            link = re.search('https://rateyourmusic.com/.+', Songs[ml].replace('\n', '')).group(0)
            pyperclip.copy(link)

            # open new tab and paste link from clipboard
            hotkey('ctrl', 't')
            hotkey('ctrl', 'l')
            hotkey('ctrl', 'v')
            press('enter')

            # give ~15 seconds to load webpage
            time.sleep(10)

            hotkey('ctrl', 'a')
            hotkey('ctrl', 'c')
            # give 3 seconds to copy to clipboard
            time.sleep(3)

            # close tab
            hotkey('ctrl', 'w')
            time.sleep(2)

            album_page = pyperclip.paste()

            songs = {}

            # must make firefox fullscreen. 
            # "Credits" only appear at the bottom
            # if the brower is in a certain aspect ratio
            try:
                if (re.search('it appears that some requests from your computer might be coming from automated scripts', album_page) != None):
                    hotkey('alt', 'tab')
                    input('Waiting for input after captcha\n')
                    hotkey('alt', 'tab')
                # extract text from 'Track listing'
                # to 'Credits'. This is the song ratings for the album.
                res1 = re.search('Track listing', album_page)
                res1.group(0)
                res2 = re.search('Total length', album_page)
                if (res2 == None):
                    res2 = re.search('Credits', album_page)
                if (res2 == None):
                    res2 = re.search('Lists', album_page)
                res2.group(0)
                album_page = album_page[res1.end():res2.end()+10]
                print(album_page)

                # separate each line
                album_page = album_page.split('\n')

                # find rating song pairs and put into dictionary
                for x in range(len(album_page)):
                    if ((re.search('\d\.\d', album_page[x]) != None)):
                        songs[album_page[x].replace('\r', '')[4:]] = album_page[x+1].replace('\r', '')[4:]
                
                # sort dictionary
                songs = {k: v for k, v in sorted(songs.items(), key=lambda item: item[0], reverse=True)}

                top_song = next(iter(songs))
            except:
                top_song = 'problem finding top song'
                songs[top_song] = ''
            
            Songs[ml] = top_song + '  |  ' + songs[top_song] + '  |  ' + link + '\n'

    f = open('./Songs/' + html[gen_num].replace('./html_album_links/', ''), 'w', encoding='utf-8')
    f.writelines(Songs)
    f.close()        
 


# back to program
hotkey('alt', 'tab')

# prevent rateyourmusic.com from
# banning our IP for too many requests
# 15 sec for 100 songs = 25 minutes to complete
# 33.333 * 35 genres = 15 hours to get every song
# I am being very conservative in my time between
# albums to try and avoid an ip ban mid execution