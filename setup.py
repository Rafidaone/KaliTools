import os
import colorama
import time

print("this will install all the programs needed for tools.py")
time.sleep(0.5)
print('btw if your using kali linux most off the tools will be installed for you')
print('do you want to contine? [Yes/No]')
while True:

                        print(Fore.GREEN + '┌──(' + Fore.BLUE +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                        r = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)

                        if r == 'yes':
                                print('ok starting install:')

                                print(Fore.GREEN + '┌──(' + Fore.BLUE +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
                                r = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)
                                os.system('sudo wifite -dict ' + r)
                                break
                        if r == 'no':
                                os.system('sudo wifite')
                                break
                        else:
                                print(' please select "yes" or "no"')




