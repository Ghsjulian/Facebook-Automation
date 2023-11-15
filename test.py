import json
from libs.__ghs__ import Facebook
from flask import Flask, request,jsonify,render_template


app = Flask(__name__)
email = ""
password = ""
fb = Facebook(email, password)
#fb.friend_request()
msg_id ="/messages/read/?tid=cid.c.100086161317364%3A100086562424514&surface_hierarchy=unknown&eav=AfaQ7d4lPNxPl5CMKYARKdN5wcKMxjKvIxwuGLmgBR4HilcLki8WgXOMY-E7oBImi9k&paipv=0&refid=11#fua"
inbox = fb.inbox(msg_id)



print(inbox)