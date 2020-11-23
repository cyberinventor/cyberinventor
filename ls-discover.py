import requests
import readline
import os
import random
from datetime import date

os.system("printf '\033]2;ls-discovery\a'")
print(""" author:\n\u001b[31m _______________
<\u001b[36m cyberinventor \u001b[31m>
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||

\u001b[0m
""")

os.system('g++ read.cpp -o putlines && ./putlines')
os.system('clear')
os.system("printf '\033]2;ls-discovery\a'")
class banner:
	art =	"""
	version: 1.0
\u001b[1030m
\u001b[31m██╗░░░░░░██████╗░░░░░░██████╗░██╗░██████╗░█████╗░░█████╗░██╗░░░██╗███████╗██████╗░██╗░░░██╗
\u001b[32m██║░░░░░██╔════╝░░░░░░██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
\u001b[33m██║░░░░░╚█████╗░█████╗██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
\u001b[34m██║░░░░░░╚═══██╗╚════╝██║░░██║██║░╚═══██╗██║░░██╗██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
\u001b[35m███████╗██████╔╝░░░░░░██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
\u001b[36m╚══════╝╚═════╝░░░░░░░╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
\n\n\n\n
	"""
	art2 = """\u001b[31m
	version: 1.0
\u001b[31m _______________
<\u001b[36m cyberinventor \u001b[31m>
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||

\u001b[0m
"""
	art3 ="""
	version: 1.0

\u001b[34m[ \u001b[32m _    _            _                                          \u001b[33m    _____                 _   _ \u001b[34m ]
\u001b[34m[ \u001b[32m| |  | |          | |                    \u001b[31m  /\                 \u001b[33m   / ____|               | | | |\u001b[34m ]
\u001b[34m[ \u001b[32m| |__| | __ _  ___| | _____ _ __ ___     \u001b[31m /  \   _ __ ___     \u001b[33m   | |  __ _ __ ___  __ _| |_| |\u001b[34m ]
\u001b[34m[ \u001b[32m|  __  |/ _` |/ __| |/ / _ \ '__/ __|   \u001b[31m / /\ \ | '__/ _ \     \u001b[33m  | | |_ | '__/ _ \/ _` | __| |\u001b[34m ]
\u001b[34m[ \u001b[32m| |  | | (_| | (__|   <  __/ |  \__ \   \u001b[31m/ ____ \| | |  __/     \u001b[33m  | |__| | | |  __/ (_| | |_|_|\u001b[34m ]
\u001b[34m[ \u001b[32m|_|  |_|\__,_|\___|_|\_\___|_|  |___/  \u001b[31m/_/    \_\_|  \___|     \u001b[33m   \_____|_|  \___|\__,_|\__(_)\u001b[34m ]
\u001b[0m
\n\n\n\n
"""
if date.today().weekday() == 0:
	print(banner.art)

if date.today().weekday() == 1:
	print(banner.art2)

if date.today().weekday() == 2:
	print(banner.art3)

if date.today().weekday() == 3:
	print(banner.art)

if date.today().weekday() == 4:
	print(banner.art2)

if date.today().weekday() == 5:
	print(banner.art3)

if date.today().weekday() == 6:
	print(banner.art)

url = input('\u001b[34menter the url to discover directories on: ')
words = open('getword.txt')
startwords = open(words.readline())
getnum = open('lines.txt')
lines = getnum
print('\u001b[32m')
for i in range(int(lines.readline())):
	try:
		guess = requests.get(url+"/"+startwords.readline().strip())
		print(guess, guess.url)
		a = open('results.txt', 'a')
		a.write(f"\n{guess} {guess.url}")
	except KeyboardInterrupt:
		print("\u001b[32m[*]\u001b[31m Bye Bye good night!")
		break
print('\u001b[32m[*]\u001b[0m done discovering ')
