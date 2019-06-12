
from flask import Flask, request,render_template
from flask_cors import CORS
app = Flask(__name__,static_folder='statics')
CORS(app)
@app.route("/")
def hello():
    return render_template('login.html') 

@app.route("/login",methods=["POST"])
def login():
    userName = request.form['username']
    password = request.form['password']
    print(userName)
    print(password)
    if userName == 'GIX' and password == 'gix_iot':
        return 'success'
    else:
        return 'failed'

@app.route("/index")
def index():
   return render_template('index1.html')

@app.route("/stream")
def stream():
   return render_template('index2.html')
   		 	
app.run(host='::', port=8888, debug=True)
