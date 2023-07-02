# Created by: github.com/anyon142

if [ -d "/data/data/com.termux/files" ];then
    echo '[*] Setting up it in your termux'
    echo
    termux-setup-storage
    apt update -y
    apt upgrade -y
    apt install python fortune -y
    pip install requests
    pip install instaloader

else
    sudo echo '[*] Setting up it in your Linux'
    echo
    sudo apt-get update -y
    sudo apt-get upgrade -y
    sudo apt-get install python3 python3-pip fortune -y
    sudo pip install requests
    sudo pip install instaloader

fi

echo
echo -e "\033[1;91m[*] \033[1;92mInstallation is completed"
echo -e "\033[1;91m[*] \033[1;92mType command 'python crackerx.py' to run the tool"
echo


