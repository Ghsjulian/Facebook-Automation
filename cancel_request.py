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
    os.system('figlet -f small " Canceling..."|lolcat')
    print("\n")
    
os.system("clear")
__logo__()
while True:
    fb.__Cancel_Request__()

