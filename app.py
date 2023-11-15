import json
from libs.__ghs__ import Facebook
from flask import Flask, request,jsonify,render_template


app = Flask(__name__)
email = ""
password = ""
fb = Facebook(email, password)
#fb.friend_request()



@app.route('/')
def index():
    return render_template('index.html')




@app.route('/chat_list')
def chat_list():
    #return render_template('index.html')
    chat_list = fb.message()
    user_info = json.dumps(str(chat_list))
    cnvrt_data = json.loads(user_info)
    return jsonify(chat_list)




if __name__ == '__main__':
    app.run(debug=True)

