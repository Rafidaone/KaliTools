import os
import requests
from colorama import Fore
import time
print("if you want to update please run the update coommand in tools.py")


def update():
    print(Fore.LIGHTBLUE_EX + "updating tools.py")
#this is to cheak if there is a file tools.py so it wont error out if there is no spam-bot.py file in the folder
    if os.path.isfile('tools.py'):
        print("deleting tools.py")
        os.remove("tools.py")
        print("deleted tools.py")
#this is were it connects to my github to get the newes vershion of kalitools
    image_url = "https://raw.githubusercontent.com/Rafidaone/KaliTools/main/tools.py"
    print("downloading kali tools from " + image_url)
    r = requests.get(image_url)
    with open("tools.py", 'wb') as f:
        f.write(r.content)
    print("finished downloading tools.py")
    print(Fore.GREEN + "you now have the newest version of Kali Tools!")
    input("press enter to exit")


update()
