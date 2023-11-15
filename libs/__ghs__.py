import mechanize
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import re
from libs import color
from libs import file 
import time
from libs import agent 
import json 
import os
import urllib.parse

class Facebook:
    def __init__(self, username, password):
        self.browser = mechanize.Browser()
        self.cj = mechanize.CookieJar()
        self.browser.set_cookiejar(self.cj)
        self.browser.set_handle_equiv(True)
        self.browser.set_handle_gzip(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(False)
        self.browser.addheaders = [('User-agent',agent.ghs_agent)]
        if os.path.exists('config/cookies.json'):
            self.set_cookie("datr",self.get_cookies("datr"))
            self.set_cookie("sb",self.get_cookies("sb"))
            self.set_cookie("noscript",self.get_cookies("noscript"))
            self.set_cookie("c_user",self.get_cookies("c_user"))
            self.set_cookie("xs",self.get_cookies("xs"))
            self.set_cookie("fr",self.get_cookies("fr"))
            self.set_cookie("m_page_voice",self.get_cookies("m_page_voice"))
        self.username = username
        self.password = password
        if self.check_login():
            print("Login Successful")
        else:
            self.sign_in()




    def sign_in(self):
        self.browser.open('https://free.facebook.com/login.php')
        self.browser.select_form(nr=0)
        self.browser.form['email'] = self.username
        self.browser.form['pass'] = self.password
        self.browser.submit()
        time.sleep(0.5)
        response_data = self.browser.response()
        res_data = response_data.read()
        res = res_data.decode()
        file.save_data(str(res))
        if "Enter login code to continue" in res:
            print("\n Waiting For Approve...")
            time.sleep(5)
            self.checkpoint()
        else:
            self.save_cookie()
        
        
       
        
        
    def save_cookie(self):
        cookies = self.cj
        cookie_info = {}
        for cookie in cookies:
            cookie_info[cookie.name] = cookie.value
        f = open("config/cookies.json", "w")
        f.write(json.dumps(cookie_info))
        f.close()



    def checkpoint(self):
        self.sign_in()




    def check_login(self):
        if 'c_user' in [cookie.name for cookie in self.browser.cookiejar]:
            return True
        else:
            return False




    def set_cookie(self,c_name,c_value):
        c = cookielib.Cookie(version=0, name=c_name, value=c_value, port=None, port_specified=False, domain='.facebook.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)
        self.cj.set_cookie(c)
        
        
       


    def get_cookies(self,name):
        f = open("config/cookies.json", "r")
        f_data = f.read()
        json_data = json.loads(f_data)
        return json_data[name]
        
        


    def friend_request(self):
        self.browser.open("https://mobile.facebook.com/friends/center/requests/")
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        file.save_data(str(res))
        print("Friends...")
        for link in self.browser.links():
            if link.text == "Confirm":
                for link2 in self.browser.links():
                    print(link2.text)
            
        
        
        
    def message(self):
        self.browser.open("https://mobile.facebook.com/messages/")
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        #file.save_data(str(res))
        print("Message...")
        data = ["Home","Profile","Messages","Notifications","Chat","Friends","Pages","Groups","Menu","New Message","New Group","Search for messages","See Older Messages","View Message Requests","View Filtered Messages","View Archived Messages","View Unread Messages","View Spam Messages","Active friends","Your Pages","Help","Settings & privacy","Report a problem","Terms & Policies","Logout","Back To Top"]
        users = {}
        msg_link = "https://mobile.facebook.com/messages/read/?tid=cid.c.100086161317364%3A100086562424514"
        for link in self.browser.links():
            if link.text in data:
                continue
            #print(link.text)
            users[link.text]=link.attrs[0][1]
        return users
            
        
        
        
        
    
    def inbox(self,msg_id):
        url = "https://free.facebook.com"+msg_id
        self.browser.open(url)
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        #file.save_data(res)
        soup = BeautifulSoup(res, 'html.parser')
        data = []
        
        message_elements = soup.find_all("div", {"class": "e bx by"})
        for a in message_elements.find_all('a'):
            print(a)
        # Extract the message text from each element
        #messages = [re.sub(r'\n', '', message_element.get_text()) for message_element in message_elements]
        # Print the messages
        #for message in message_elements:
            #print(message)
        
        """
         #extract and print the text from each span tag
        for span in soup.find_all('span'):
            data.append(span.text)
        return data[::-1]
        """
       
    
    
    
    
        
        """
        response = self.browser.response()
        res_data = response.read()
        res = res_data.decode()
        file.save_data(str(res))
        print("Friends...")
        """
        



