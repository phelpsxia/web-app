#back-up for DVR web-app
from flask import Flask, request,render_template
from flask_cors import CORS
import pymysql
import json
app = Flask(__name__,static_folder='statics')
CORS(app)

#login page
@app.route("/")
def hello():
    return render_template('login.html') 

#login check
#@app.route('/login',methods=["GET", "POST"])
#TODO add the user auth
'''
def login():
    if request.method == 'POST':
        page_status = request.form['status']

        if page_status == 'signup':
            userName = request.form['username']
            email = request.form['email']
            password = request.form['password']
            uid_token = request.form['uuid']
            notification_token = request.form['token']

            db = pymysql.connect("localhost","testuser","test123","TESTDB" )
            cursor = db.cursor()
            sql = "SELECT USERID FROM USERINFO"
            
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results: 
                    if row[0] == userName:
                        return 'username exist'
                
                cursor = db.cursor()
                sql = "INSERT INTO USERINFO(USERID, PASSWORD, EMAIL) \
                    VALUES ('%s', '%s', '%s')" % \
                    (userName, password, email)

                try:
                    cursor.execute(sql)
                    db.commit()
                    s = 1

                except:
                    db.rollback()
                    s = 0
                
                if s == 1:
                    cursor = db.cursor()
                    sql = "INSERT INTO TOKENLIST \
                        VALUES ('%s', '%s', '%s')" % \
                        (userName, uid_token, notification_token)
                
                    try:
                        cursor.execute(sql)
                        db.commit()
                        return render_template("main.html", value='uid_token')
                    
                    except:
                        db.rollback()
                        return 'failed'
                
                else:
                    return 'failed'
            
            except:
                return 'failed'

        if page_status == 'login':
            userName = request.form['username']
            password = request.form['passWord']
            
            cursor = db.cursor()

            sql = "SELECT USERID FROM USERINFO \
                where USERID = '%s' AND PASSWORD = '%s'" %(userName, password)
            
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                result = cursor.fetchone()
            except:
                return 'retry'

            if result[0] == userName:            
                sql = "SELECT UUIDTOKEN FROM TOKENLIST WHERE USERID = '%s'" %userName

                try:
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    uuid = result[0]
                    return render_template("main.html", value=uuid)
                
                except:
                    return 'uuid not find'

            else:
                return "LOG_IN FAILED"
            
        
        if page_status == 'email':
            email = request.form['email']

            cursor = db.cursor()
            sql = "SELECT EMAIL FROM USERINFO \
                where EMAIL = '%s' " %email
            
            try:
                cursor.execute(sql)
                result = db.fetchone()
                if result[0] == email:
                    #TODO send email to the email address
                    valid_code = random.randint(0,1001)
                    with open(textfile) as fp:
                        # Create a text/plain message
                        msg = MIMEText(fp.read())

                    # me == the sender's email address
                    # you == the recipient's email address
                    msg['Subject'] = 'Reset Password for Diversita' 
                    msg['From'] = 'clytze20@uw.edu'
                    msg['To'] = email

                    # Send the message via our own SMTP server.
                    s = smtplib.SMTP('localhost')
                    s.send_message(msg)
                    s.quit()

                else:
                    return 'email not exist'
            
            except:
                return 'retry'

        if page_status == 'validation':
            valid_c = request.form['valid']
            if valid_c == valid_code:
                return 'verified'
            
            else:
                return 'failed'
        
        if page_status == 'reset':
            password = request.form['reset']
            sql = "UPDATE USERINFO SET PASSWORD='%s' \
                WHERE EMAIL='%s' " %s(password, email)
            
            try:
                db.execute(sql)
                db.commit()
                return 'reset success!'

            except:
                db.rollback()
                return 'failed'
        
    else:
        return render_template('login.html')
'''
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

#history page
@app.route("/index")
def index():
   return render_template('index1_backup.html')

#streaming page
@app.route("/stream")
def stream():
   return render_template('index2_backup.html')

#acquire data from database
@app.route('/fetch',methods=["POST",'GET'])
def fetch():
    db = pymysql.connect("localhost","root","gix_iot","UserInfo")
    cursor = db.cursor()
    #TODO sql command
    if request.method == 'GET':
        sql = "SELECT * FROM routesinfo"                 
        #try:
        cursor.execute(sql)
        data = cursor.fetchall()
        res = {}
        res['routes'] = {}
        for r in data:
            #print(r[-2].split('|')[-1])
            res['routes'][r[-2].split('|')[-1]] = {
                "can": r[0],
                "device_type": 3,
                "end_geocode": r[1],
                "end_lat": r[3],
                "end_lng": r[5],
                "end_time":r[7],
                "fullname": r[9],
                "hpgps": False,
                "len": r[9],
                "maxcamera": -1,
                "maxlog": -1,
                "movie": False,
                "piececount": -1,
                "proccamera": 6,
                "proclog": 6,
                "start_geocode": r[2],
                "start_lat": r[4],
                "start_lng": r[6],
                "start_time": r[8],
                "url": "https://chffrprivate.blob.core.windows.net/chffrprivate3/v2/c325c20903434c0c/e4f3aaec6f339a396887ffc0cd224f66_2018-05-02--20-47-36"
            }
        #print(res)
        result = json.dumps(res)
        return result,200,{"Content-Type":"application/json"}
        #except:
            #return "Error: unable to fecth routeId data"  
    
    if request.method == 'POST':
        routeId = request.form['routeId']
        #print('routID:', routeId)
        sql = "SELECT * FROM routesdetail WHERE instr(routeid_index, '%s')" %routeId

        #try:
        cursor.execute(sql)
        data = cursor.fetchall()
        #print(data)
        #print('----------')
        res = {}
        for r in data:
            #print(int(r[0].split('_')[-1]))
            res[int(r[0].split('_')[-1])//100] = {
                'dist': r[2],
                'lat': r[1],
                'lng': r[3],
                'speed': r[4],
                'index': int(r[0].split('_')[-1])
            }
        result = []
        for key in sorted(res.keys()):
            result.append(res[key])
        #return data
        #except:
            #return "Error: unable to fecth route details"  
        result = json.dumps(result)
        return result,200,{"Content-Type":"application/json"}
    db.close()

#upload data from device
@app.route('/streaming',methods=["POST"])
def streaming():
    db = pymysql.connect("localhost","root","gix_iot","UserInfo")
    sql = ''
    cursor = db.cursor()
    #TODO sql command
    
    
    data = cursor.fetchall()
    #return data
    
    # 关闭数据库连接
    db.close()

app.run(host='::', port=8888, debug=True)