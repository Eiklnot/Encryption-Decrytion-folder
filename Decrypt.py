#!//usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "Ransomer.py" or file == "thekey.key" or file == "Decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

pw = "dnd"

user_pw = input("Enter the secret phrase to decrypt the file\n")

if user_pw == pw:

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Congrats, your files are decrypted")
else:
	print("Wrong secretphrase!")
