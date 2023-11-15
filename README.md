<center>
<h1> Facebook Automation</h1><br><br><br>
<h1>Developer : Ghs Julian</h1>

<strong>
  This is a Facebook Automation using python. You can automate your Facebook
  account using this tools . It's Awesome 😎
</strong>
<br><br>
<h1> Installation & Command</h1>
<br>

```bash
git clone && cd Facebook && pip install -r requirements.txt && python app.py
```

<br>
<strong> Bassic Examples Of Code...</strong><br><br>

```python
import json
from libs.__ghs__ import Facebook
from flask import Flask, request,jsonify,render_template

app = Flask(__name__)
email = "your_email"
password = "your_password"
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


```

<br><br>
<h1>Demo & Screenshots</h1>

<img src="ss/S1.png" width="290" height="270"><br><br>
<img src="ss/S2.png" width="290" height="270"><br><br>
<img src="ss/S3.png" width="290" height="270"><br><br>
<img src="ss/S4.png" width="290" height="270">
</center>