printf '\033]2;Installation in progress\a'
python3=/usr/bin/python3
git=/usr/bin/git
pip3=/usr/bin/pip3
echo "Checking For python3..."
sleep 5
if [ -f $python3 ]
then
	echo "Found"
else
	echo "Not Found - Installing..."
	sleep 2
	sudo apt install python3
fi
echo "Checking For python3-pip..."
sleep 5
if [ -f $pip3 ]
then
	echo "Found"
else
	echo "Not Found - Installing..."
	sleep 2
	sudo apt install python3-pip
fi
echo "Checking For git..."
sleep 5
if [ -f $git ]
then
	echo "Found"
else
	echo "Not Found - Installing..."
	sleep 2
	sudo apt install git
fi
echo "Installing Wordlists"
wget https://github.com/hacker3983/wordlist/raw/master/default-list-2.3-medium.txt
wget https://raw.githubusercontent.com/hacker3983/wordlist/master/apache-user-enum-1.0.txt
wget https://raw.githubusercontent.com/hacker3983/wordlist/master/apache-user-enum-2.0.txt
wget https://raw.githubusercontent.com/hacker3983/wordlist/master/directory-list-1.0.txt
wget https://github.com/hacker3983/wordlist/raw/master/directories.jbrofuzz
wget https://raw.githubusercontent.com/hacker3983/wordlist/master/directory-list-2.3-small.txt
wget https://raw.githubusercontent.com/hacker3983/wordlist/master/directory-list-lowercase-2.3-medium.txt
wget https://github.com/hacker3983/wordlist/blob/master/directory-list-lowercase-2.3-small.txt
echo "Installing Requirements..."
sleep 5
pip3 install -r requirements.txt
echo "Installation complete."
