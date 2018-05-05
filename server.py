from flask import Flask, render_template,redirect,request,session
import random
app = Flask(__name__)
app.secret_key="myKey"

@app.route('/')
def index():
    print session['randNum']
    return render_template("index.html",hid=1)
@app.route('/process',methods=['POST'])
def process():
    
    randNum1=session['randNum']
    compNum =request.form['number']
    if compNum == '' :
        compNum=0
    if int(randNum1) > int(compNum):
        session['incTxt']="TOO LOW"
        print "TOO LOW"
    elif int(randNum1) < int(compNum):
        session['incTxt']="TOO HIGH"
    
    else:
        session['incTxt']=str(randNum1)+" Was the Number"
    
    print compNum
    print randNum1
    
    return render_template('index.html',num=int(randNum1),cop=int(compNum))
@app.route('/reset')    
def reset():
    session.pop('randNum')
    session['randNum']=random.randrange(0,101)
    session['incTxt']=""
    print session['randNum']
    return render_template('index.html',hid=1)
app.run(debug=True)