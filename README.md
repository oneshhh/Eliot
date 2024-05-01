# Eliot
A ransomware toolkit using fernet encryption.


This tool utilizes the robust Fernet cryptography library to encrypt files in the current directory, rendering them inaccessible. The only way to restore these files is by using the corresponding decrypter and the unique key generated during encryption.

to use this file save it as eliot.pyw and it will encrypt all the files in its current directory and generate a key.key file containing its key for decryption.

to decrypt all the files back to their original form, run the decrypt.py file and type the password.
you can set your own password by editing the decrypt.py file.

By default the password for decryption is set to "fsociety".
