#making a new file that is not exist yet
file = open("drinks.txt","x")
file.close()

#checking if the new file already exist
import os

if os.path.exists("drinks.txt"):
    print("file drinks.txt is existed")
else:
    print("file drinks.txt is not exist")

#delet file drinks.txt if it is existing
if os.path.exists("drinks.txt"):
    os.remove("drinks.txt")