import json
import time 
import os
import threading
from libs import color
from libs.__ghs__ import Facebook



email = ""
password = ""

fb = Facebook(email, password)

def __logo__():
    os.system("clear")
    print("\n")
    os.system('figlet -f small " Requesting..."|lolcat')
    print("\n")
    



print(color.BOLD+color.YELLOW+color.BOLD+"\n[1] Default Friend Request"+color.LIGHT_CYAN)
print(color.BOLD+color.YELLOW+color.BOLD+"\n[2] Request From Group/Friend List"+color.LIGHT_CYAN)

cmd = int(input(color.BOLD+color.GREEN+color.BOLD+"\n[+] Select An Option : "+color.LIGHT_CYAN))
os.system("clear")
if cmd == 1:
    os.system("clear")
    __logo__()
    while True:
        fb.friend_request()
elif cmd ==2:
    request = input(color.BOLD+color.CYAN+color.BOLD+"\n[+] Enter Friend List URL : "+color.LIGHT_CYAN)
    os.system("clear")
    __logo__()
    while True:
        fb.friend_request(request)
else:
    os.system("clear")
    print(color.BOLD+color.RED+color.BOLD+"\n[!] Please Select 1 Or Two "+color.LIGHT_CYAN)
    



