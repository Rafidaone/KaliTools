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
	print('this script might have problems running on macos')
elif platform == "win32":
	print(Fore.RED + 'this script isent made for windows and most functions wont work!')

#this is the main menu
while True:
	
	print('_________________________')
	print(Fore.GREEN + '-$$$$-  main menu  -$$$$-')
	print(Style.RESET_ALL)
	print('0 | exit')
	print('--|------')
	print('1 | install/update   -this is for debian os only like raspbian ubuntu kali etc')
	print('--|------')
	print('2 | wifite')
	print('--|------')
	print('3 | tshark')
	print('--|------')
	print("4 | drive")
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
				print('type or past the directory of word list example: rockyou.txt or home/fold/file/rockyou.txt')

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
		print(Fore.RED + 'warning this only works on debian linux' + Style.RESET_ALL)
		os.system('')

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

			print(Fore.GREEN + '┌──(' + Fore.BLUE + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
			r = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)

			if r == '1':
				print('past or type the directory to delete files made')
				print('wen the console stops throwing up numbers at you its done!')

				print(Fore.GREEN + '┌──(' + Fore.BLUE + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
				d = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)

				n = 0

				while True:

					n = 1 + n


					if os.path.isfile(d + '/' + str(n) + '.txt'):
						print('removed ' + str(n) + ' files!        press ^C to stop')
						os.remove(d + '/' + str(n) + '.txt')


			if r == '2':
				print('past or type the directory to make the files')


				print(Fore.GREEN + '┌──(' + Fore.BLUE + 'HackerMan㉿Russia' + Fore.GREEN + ')-[~]')
				d = input('└─' + Fore.BLUE + '$ ' + Fore.GREEN)

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

	else:
		print(Fore.RED + guy + Fore.GREEN + ' is not on the main menu' + Style.RESET_ALL)
		time.sleep(2)
#                      options/command end
