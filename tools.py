import os
import colorama
import requests
from colorama import Fore, Style
from sys import platform
import time
import subprocess


print(Fore.BLUE + 'code by RafiDEV more at rafidev.net' + Style.RESET_ALL)


#cheks what os is the script ran in

if platform == "linux" or platform == "linux2":
        print("Linux")
#cheks if ran as root
        if os.geteuid() != 0:

                print(Fore.RED + 'warning not runing as root!')
                print(Style.RESET_ALL)

if platform == "darwin":
        guyos = "Mac OS"
        print('this script might have problems running on MacOS')
elif platform == "win32":
        guyos = "Windows"
        print(Fore.RED + 'this script isent made for windows and most functions wont work!')

v = 3


#this is the main menu
while True:
        print('______________________________________')
        print(Fore.GREEN + '-$$$$-  main menu  -$$$$-')
        print(Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + "os is " + str(guyos))
        print(Fore.MAGENTA + 'version: ' + str(v))
        print(Style.RESET_ALL + '--------------------------------------')
        print('0 | exit')
        print('--|------')
        print('1 | update')
        print('--|------')
        print('2 | wifite')
        print('--|------')
        print('3 | tshark')
        print('--|------')
        print("4 | drive")
        print("--|------")
        print('5 | put device into monitore mode')
        print("--|------")
        print('6 | put device into managed mode')
        print("--|------")
        print('7 | chat spam bot       (you need a gui)')
        print("--|------")
        print("8 | decrypt wifi hand shake file")
        print('--------------------------------------')
        # the actual typing thing
        print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
        guy = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)


#             the optinas/command start



#      exit
        if guy == '0':
                break

        # tshark
        if guy == '3':
                print('type filters to be applied')
                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                f = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)
                os.system('sudo tshark ' + f)


# update
        if guy == '1':
                print(Fore.LIGHTBLUE_EX + "updating update.py")
        # this is to cheak if there is a file tools.py so it wont error out if there is no spam-bot.py file in the folder

                if os.path.isfile('update.py'):
                        print("deleting update.py")
                        os.remove("update.py")

                        print("deleted update.py")
                        # this is were it connects to my gh to get the newes vershion of script
                        image_url = "https://raw.githubusercontent.com/Rafidaone/KaliTools/main/update.py"
                        print("downloading the update script from " + image_url)
                        r = requests.get(image_url)
                        with open("update.py", 'wb') as f:

                                f.write(r.content)
                                print("finished downloading update.py")
                                print(Fore.GREEN + "you now have the newest version of update script!")
                                print("please execute update.py to continue")
                                break




        # wifite
        if guy == '2':
                print('would you like to use custom word list? [Yes/No]')

                while True:

                        print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                        r = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                        if r == 'yes':
                                print('type or past the directory of word list example: rockyou.txt or home/fold/file/rockyou.txt')

                                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                                r = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)
                                os.system('sudo wifite -dict ' + r)
                                break
                        if r == 'no':
                                os.system('sudo wifite')
                                break
                        else:
                                print(' please select "yes" or "no"')

#       tshark
        if guy == '3':
                print('the dev did not add this to the script yet try updating if he added it')

#    drive
        if guy == '4':
                print('this is the drive script were it makes lots of trash files')
                print('would you like to make files or delete the files made?')

                while True:
                        print('''
                                _________
                                0 | cancel
                                --|------
                                1 | delete files made
                                --|------
                                2 | make files
                                ---------
                                                ''')

                        print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                        r = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                        if r == '1':
                                print('past or type the directory to delete files made')
                                print('wen the console stops throwing up numbers at you its done!')

                                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                                d = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                                n = 0

                                while True:

                                        n = 1 + n


                                        if os.path.isfile(d + '/' + str(n) + '.txt'):
                                                print('removed ' + str(n) + ' files!        press ^C to stop')
                                                os.remove(d + '/' + str(n) + '.txt')


                        if r == '2':
                                print('past or type the directory to make the files')


                                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                                d = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                                n = 0

                                while True:
                                        n = 1 + n

                                        if not os.path.isfile(d + '/' + str(n) + '.txt'):
                                                print('made ' + str(n) + ' files!        press ^C to stop')
                                                with open(d + '/' + str(n) + '.txt', 'w') as f:
                                                        f.write('''

                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.#%*.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.#%/.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,.#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%..,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...#%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/#%%%%%%%%%%%%%%...#%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.........%%%%%%%%%%#...%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%.........%%%%%%%%%%%%%....#%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%#*............/%%%%%%%%%%,....%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%.....%%%......#%%%%%%#.....%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%*......%%%/.....%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%............%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%#........%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%../.........................#%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%#.....#%(...........(%%%#......#%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%....#%%%%%%%%%%%%%%%%%%%%%%%....../%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%#.....#%%%%%%%%%%%%%%%%%%%%%%%%%%%......%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%#.(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.*%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



                                                    ''')


                        if r == '0':
                                break

                        else:
                                print(Fore.RED + r + Fore.GREEN + ' is not on the menu, please select something from the menu' + Style.RESET_ALL)
                                time.sleep(1.5)


#    put device into monitor mode
        if guy == '6':
                os.system('ifconfig')
                print()
                print('type the device to put into managed mode, example: wlan1mon')

                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                device = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                os.system('airmon-ng stop ' + device)


                #    put device into maneged mode
        if guy == '5':

                        os.system('ifconfig')
                        print()
                        print('type the device to put into monitor mode, example: wlan1')

                        print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                        device = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                        os.system('airmon-ng start ' + device)



#   spam bot
        if guy == '7':
                import pyautogui

                print(Fore.GREEN + 'type a word to spam to stop press ^C')

                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                word = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)
                print('in 5 sec spam will begin')

                time.sleep(1)
                print('in 4 sec spam will begin')

                time.sleep(1)
                print('in 3 sec spam will begin')

                time.sleep(1)
                print('in 2 sec spam will begin')

                time.sleep(1)
                print('in 1 sec spam will begin')
                time.sleep(1)

                print('spamming ' + word)
                t = 0
                while True:
                        t = 1 + t
                        print("I have typed " + str(t) + ' words       press ^C to stop')
                        pyautogui.typewrite(word)
                        pyautogui.keyDown('enter')
                        pyautogui.keyUp('enter')


#               decrypt hand shake
        if guy == "8":
                print("past the directory of hand shake file, example:   neighbors-wifi.cap school-wifi.pcap")
                print("")
                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                hand = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)

                print("past the directory of wordlist    ")
                print("")
                print(Fore.GREEN + '┌──(' + Fore.LIGHTBLUE_EX + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                list = input('└─' + Fore.LIGHTBLUE_EX + '$ ' + Fore.GREEN)
                os.system("sudo aircrack-ng " + hand + " -w " + list)



        else:

                print(Fore.RED + guy + Fore.GREEN + ' is not on the main menu' + Style.RESET_ALL)
                time.sleep(2)
#                      options/command end
print(Fore.GREEN + "exiting script" + Style.RESET_ALL)
