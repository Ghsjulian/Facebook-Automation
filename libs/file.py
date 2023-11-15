import os 
import time 

def save_data(file):
    f = open("config/index.html", "w")
    f.write(file)
    f.close()