import json
import time 
import os
import threading
from libs import color
from libs.__ghs__ import Facebook
from flask import Flask, request,jsonify,render_template


app = Flask(__name__)
email = ""
password = ""




fb = Facebook(email, password)

user ="100088668742389"
msg = "Hello How Are You ?"


ghs = fb.__send_message__(user,msg)
