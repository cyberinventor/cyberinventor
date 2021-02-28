curl "https://raw.githubusercontent.com/cyberinventor/ls-discovery/master/version.txt" -o file.txt > /dev/null 2>&1
file="file.txt"
file2="version.txt"
i=1
while read line; do
        latest_version=$line
done < $file

i=1
rm file.txt
while read line2; do
        current_version=$line2
done < $file2

if [ "$current_version" = "$latest_version" ]
then
        echo "Checking for updates..."
        sleep 5
        echo "Already up to date."
else
        echo "checking for updates..."
        sleep 5
        echo "Not up to date..."
        echo "Downloading Updates..."
        sleep 5
        cd .. && rm -rR ls-discovery
        git clone "https://github.com/cyberinventor/ls-discovery"
        cd ls-discovery && bash install.sh
fi
echo "Installation finished you may now close the terminal and run the program..."
