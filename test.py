import json
import time 
import os
import threading
from libs import color
from libs.__ghs__ import Facebook
from flask import Flask, request,jsonify,render_template


app = Flask(__name__)
email = "01302661227"
password = "ghs_smith:"

if not os.path.exists('config/cookies.json'):
    email_id = input(color.BOLD+color.YELLOW+color.BOLD+"\n[+] Enter Email/ID/Phone : "+color.LIGHT_CYAN)
    u_pass = input(color.BOLD+color.YELLOW+color.BOLD+"\n[+] Enter Facebook Password : "+color.LIGHT_CYAN)
    fb = Facebook(email_id,u_pass)



fb = Facebook(email, password)
user ="100088668742389"
inbox = fb.__Chatbox__(user)

#print(inbox)