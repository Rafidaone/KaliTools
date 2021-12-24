import os
import requests
from colorama import Fore
import time


print(Fore.LIGHTBLUE_EX + "updating tools.py")
#this is to cheak if there is a file tools.py so it wont error out if there is no spam-bot.py file in the folder
if os.path.isfile('tools.py'):
    print("deleting tools.py")
    os.remove("tools.py")
    time.sleep(0.5)
    print("deleted tools.py")
#this is were it connects to my web site to get the newes vershion of spam-bot
image_url = "https://raw.githubusercontent.com/Rafidaone/KaliTools/main/tools.py"
print("downloading kali tools from " + image_url)
r = requests.get(image_url)
with open("tools.py", 'wb') as f:
    f.write(r.content)
print("finished downloading tools.py")
print(Fore.GREEN + "you now have the newest version of Kali Tools!")



print(Fore.LIGHTBLUE_EX + "installing update.sh")
#this is to cheak if there is a file tools.py so it wont error out if there is no spam-bot.py file in the folder
if os.path.isfile('update.sh'):
    print("deleting update.sh")
    os.remove("update.sh")
    time.sleep(0.5)
    print("deleted update.sh")

image_url = "https://raw.githubusercontent.com/Rafidaone/KaliTools/main/update.sh"
print("downloading new update script from " + image_url)
r = requests.get(image_url)
with open("tools.py", 'wb') as f:
    f.write(r.content)
print("finished downloading update.sh")
print(Fore.GREEN + "update.py is now discatinued by the developer in exchange for update.sh")
time.sleep(1.5)
input('press enter to exit')
