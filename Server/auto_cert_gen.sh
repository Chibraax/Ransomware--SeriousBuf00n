#!/bin/bash

echo "[> Check if OpenSSL is installed..."
if [ -f /usr/bin/openssl ] && [ -f /bin/openssl ];then
	echo "OpenSSL installed !"

else
	echo "OpenSSL not installed, need install it";
	sudo apt install openssl ;
fi

#Generate priv key
openssl genrsa -out key.pem 2048
#Generate certificat with the previous key generated
openssl req -new -key key.pem -out signreq.csr
#Signin the certificate with the key
openssl x509 -req -days 365 -in signreq.csr -signkey key.pem -out certificate.pem
