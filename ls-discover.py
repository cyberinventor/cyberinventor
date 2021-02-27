import requests
import readline
import os
import random
from datetime import date
import arts
import threading

readline.parse_and_bind('tab: complete')
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
print("Note: You can hit tab to autocomplete")
path = input("Enter the wordlist path/name: ")

os.system('clear')
os.system("printf '\033]2;ls-discovery\a'")
if date.today().weekday() == 0:
	banner = arts.art
elif date.today().weekday() == 1:
	banner = arts.art2
elif date.today().weekday() == 2:
	banner = arts.art3
elif date.today().weekday() == 3:
	banner = arts.art
elif date.today().weekday() == 4:
	banner = arts.art2
elif date.today().weekday() == 5:
	banner = arts.art3
elif date.today().weekday() == 6:
	banner = arts.art
f = open(path)
lines = len(f.readlines())
f.close()
count = 0
print(banner)
url = input('\u001b[34menter the url to discover directories on: ')
with open(path) as wordlist:
	os.system("clear")
	print('\u001b[32m')
	Found = ""
	Progress = ""
	for word in wordlist.readlines():
		Info = f"""
\u001b[4m\u001b[34mLS-DISCOVERY v1.0.2 \u001b[0m\u001b[31m<\u001b[36m cyberinventor \u001b[31m>\u001b[0m
--------------------------------------------------------------------------------------
URL/DOMAIN	{url}
FOUND		{0 if Found == "" else Found}
Progress	{Progress}
Wordlist	{path}
--------------------------------------------------------------------------------------
"""
		print(banner)
		print(Info)
		try:
			r = requests.get(f"{url}/{word}")
			if r.status_code == 200:
				Found += "/"+word+"\n"
			else:
				count+=1
				os.system("clear")
				Progress = f"Progess: \u001b[31m{count}\u001b[0m/\u001b[34m{lines}\u001b[0m"
		except KeyboardInterrupt:
			print("\u001b[32m[*]\u001b[31m Bye Bye good night!")
			break
print('\u001b[32m[*]\u001b[0m done discovering ')
