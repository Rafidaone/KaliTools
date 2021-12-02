import os
import colorama
from colorama import Fore, Style
from sys import platform
import time
import subprocess

print(Fore.BLUE + 'code by RafiDEV more at rafidev.net' + Style.RESET_ALL)


#cheks what os is the script ran in
if platform == "linux" or platform == "linux2":
#cheks if ran as root
	if os.geteuid() != 0:
		
		print(Fore.RED + 'warning not runing as root!')
		print(Style.RESET_ALL)
if platform == "darwin":
	print('this script might have probloms runing on macos')
elif platform == "win32":
	print(Fore.RED + 'this script isent made for windows and most functins wont work!')

#this is the main menu
while True:
	
	print('_________________________')
	print(Fore.GREEN + '-$$$$-  main menu  -$$$$-')
	print(Style.RESET_ALL)
	print('0 | exit')
	print('--|------')
	print('1 | install/update   -this is for debien os only like rasbean ubuntu kali etc')
	print('--|------')
	print('2 | wifite')
	print('--|------')
	print('3 | tshark')
	print('----------------')
	# the actual typing thing
	print(Fore.GREEN + '┌──(' + Fore.BLUE +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
	guy = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)


#             the optinas/command start
	


#      exit
	if guy == '0':
		print('bye mate, see you soon')
		break

	# tshark
	if guy == '3':
		print('starting tshark')
		os.system('sudo tshark')


	# wifite
	if guy == '2':
		print('would you like to use custom word list? [Yes/No]')

		while True:

			print(Fore.GREEN + '┌──(' + Fore.BLUE +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
			r = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)

			if r == 'yes':
				print('type or past the dirctory of word list example: rockyou.txt or home/fold/file/rockyou.txt')

				print(Fore.GREEN + '┌──(' + Fore.BLUE +'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
				r = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)
				os.system('sudo wifite -dict ' + r)
				break
			if r == 'no':
				os.system('sudo wifite')
				break
			else:
				print(' please select "yes" or "no"')

#	update
	if guy == '3':
		print(fore.RED + 'warning this only works on debien linux' + Style.RESET_ALL)
		os.system('')


	else:
		print(Fore.RED + guy + Fore.GREEN + ' is not on the main menue' + Style.RESET_ALL)
		time.sleep(2)
#                      options/command end
