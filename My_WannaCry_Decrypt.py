import os
from cryptography.fernet import Fernet

files0 = []
files1 = []
files2 = []
path0 = os.path.expanduser("~") + "/Documents/"
path1 = os.path.expanduser("~") + "/Images/"
path2 = os.path.expanduser("~") + "/Vidéos/"

#Gathering all files to encrypt
for file in os.listdir(path0):
    if file == "Wish_WannaCry.py" or file == "filekey.key":
        continue
    if os.path.isfile(path0 + file):
        files0.append(path0 + file)

for file in os.listdir(path1):
    if file == "Wish_WannaCry.py" or file == "filekey.key":
        continue
    if os.path.isfile(path1 + file):
        files1.append(path1 + file)

for file in os.listdir(path2):
    if file == "Wish_WannaCry.py" or file == "filekey.key":
        continue
    if os.path.isfile(path2 + file):
        files2.append(path2 + file)

with open ("filekey.key", "rb") as filekey:
    secretkey = filekey.read()

for file in files0:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    decrypted_contents = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted_contents)

for file in files1:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    decrypted_contents = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted_contents)

for file in files2:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    decrypted_contents = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted_contents)

print(files0)
print(files1)
print(files2)