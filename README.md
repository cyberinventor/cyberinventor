# About ls-discovery
ls-discovery is a tool that bruteforces a website and find hidden files and directories. <br>
# Getting started
## Installation
**1.** ```git clone https://github.com/cyberinventor/ls-discovery.git```
<br>
 **2.** ```cd ls-discovery```
<br>
**3.** ```bash install.sh```
<br>
## Uninstall
**1.** ```bash uninstall.sh```

## check for updates
**1.** ```bash update.sh```

## ls-discovery execution
**1.** ```python3 ls-discover.py```
**you will get something like this when it runs**
# Operating Systems tested on
1.```kali linux```

# Screenshots on how to use ls-discovery
<br><br>
<h1>how to start and use the wordlist in ls-discovery</h1>
<img src="https://www.mediafire.com/convkey/2245/cn3tuxpvydr4yuc6g.jpg" alt='screen1.png'>
start ls-discovery  python3 ls-discover.py
<h1> example</h1>
<br> enter the wordlist name: /root/ls-discovery/wordlist/directory-list-1.0.txt <br>
<h1> example2</h1>
<br>
<h1> in example two you need to move the wordlist you want to use into the ls-discovery folder <br></h1>
ls
<br>
passwords.txt
<br>
mv /root/passwords.txt ls-discovery
<br>
enter the wordlist name: passwords.txt <br>
<br>
<p> you can use the built in wordlists in ls-discovery look below to see the names of the built in wordlists.<br> and you can also download your own wordlist</p>
<br>
<h1> Built in wordlist names</h1>
<p>
apache-user-enum-1.0.txt <br> apache-user-enum-2.0.txt <br> default-list-2.3-medium.txt <br> directories.jbrofuzz<br> directory-list-1.0.txt<br> directory-list-2.3-small.txt <br> directory-list-lowercase-2.3-medium.txt <br> directory-list-lowercase-2.3-small.txt```
</p>
<h1>Notes</h1>
<br>
i recommend you guys move the wordlist you want to use in the ls-discovery folder
<br><br>
<h1>entering the target url</h1><br>
in this screenshot you need to enter the url of target url with https://example.com or http://example.com
<img src="https://www.mediafire.com/convkey/9d49/evpvmg7wu9jr0pf6g.jpg" alt='screen2.png'>
<br><br>
<h1>start attacking</h1><br>
after you press enter your attack will start while the attack is running you will be able to see the results. just open the results.txt file in a editor and you will see the results you can also open new terminal an type cd ls-discovery and press enter then type nano results.txt and press enter you will see the results.txt
<img src="https://www.mediafire.com/convkey/a208/ten0z81k7r87lrb6g.jpg" alt='screen3.png'>
if you see < Response [200] > it means ls-discovery found a file or directory
if you see < Response [404] > it means ls-discovery did not find that file or directory
<br><br>
<h1>To Make It Easier for you guys read the instructions below &#8595;</h1>
<h1>httpmessages</h1>
you can see the response codes or http messages on https://www.w3schools.com/tags/ref_httpmessages.asp
<br><br>
<h1>http messages or response codes you may see</h1>
<br>
200 - Ok
<br>
400 - Bad Request
<br>
401 - Unauthorized
<br>
403 - Forbidden
<br>
404 - not found
<br>
405 - Method Not Allowed
<br>
500 - Internal Server Error
<br>
501 - Not Implemented
<br>
502 - Bad Gateway
<br>
503 - Service Unavailable
<br>
504 - Gateway Timeout
<br>
if you want to understand those numbers above visit the link https://www.w3schools.com/tags/ref_httpmessages.asp
<br><br>
<h1>Screenshots</h1>
<p>On Ubuntu Wsl</p>
<img src=http://www.mediafire.com/convkey/2bc1/e402vgon0i9vliu6g.jpg alt=on ubuntu>
<img src="http://www.mediafire.com/convkey/fc52/pil3kolu3jg06446g.jpg" alt=on ubuntu>
<p>On Kali Linux</p>
<img src="https://www.mediafire.com/convkey/2245/cn3tuxpvydr4yuc6g.jpg" alt='on kali linux'>
<img src="https://www.mediafire.com/convkey/9d49/evpvmg7wu9jr0pf6g.jpg" alt='screen2.png'>
<img src="https://www.mediafire.com/convkey/a208/ten0z81k7r87lrb6g.jpg" alt='screen3.png'>
<h1>Please Report Any Issues Are What You Want Me to Implement.</h1>
