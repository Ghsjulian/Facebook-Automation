#!/bin/bash

echo ""
clear

# Installing Packages And Dependencies

pkg update && pkg upgrade -y
pkg install python3
pkg install figlet 
pkg install wget
pkg install lolcat
pip install mechanize
pip install flask
pip install BeautifulSoup
pip install urllib
pip install lolcat

clear

printf "\n"

# Print The Logo...

figlet -small 'Ghs Julian' | lolcat

printf "\n"

printf "\n You can use it by the command 'python app.py'. It will be started port number 5000. \n"
