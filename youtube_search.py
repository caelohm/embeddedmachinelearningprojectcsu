import os
import time
import re
from pyautogui import press, hotkey
import pyperclip

file_paths = []

for dirpath, dnames, fnames in os.walk("./Songs/"):
    for f in fnames:
        file_paths.append(f)

# switch to firefox
# must do before loop to 
# avoid going back to program

gen_start = int(input('Input genre to start from\n'))
gen_start -= 1

for gen_num in range(gen_start, len(file_paths)):

    print(file_paths[gen_num])

    f = open('./Songs/' + file_paths[gen_num], 'r', encoding='utf-8')

    Songs = f.readlines()

    f.close()

    song_start = int(input('Input song number to start from\n'))
    song_start -= 1

    for ml in range(song_start, len(Songs)):
        s_s_ = Songs[ml].split('  |  ')
        pyperclip.copy(s_s_[1] + ' ' + s_s_[2].replace('https://rateyourmusic.com/release/album/', '').replace('/', ' ').replace('-', ' ').replace('_', ' '))
        time.sleep(1)

        print(str(ml+1))

        hotkey('alt', 'tab')
        press('/')
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'v')
        press('enter')
        input('input when song has been added')