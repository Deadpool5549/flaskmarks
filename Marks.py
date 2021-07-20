# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:32:12 2021

@author: Sai Manoj
"""

from flask import Flask,redirect,request,url_for,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to results page"

@app.route("/passed")
def passed():
    return "Congrats ,You passed"

@app.route("/fail")
def fail():
    return "Sorry ,you failed"

@app.route("/bug")
def bug():
    return "Sorry ,bug"

@app.route("/results",methods=['POST','GET'])
def results():
    if request.method=='POST':
        marks=request.form['mark']
        if int(marks) >= 40:
            return redirect(url_for('passed'))
        else:
            return redirect(url_for('fail'))
    else:
        return render_template("results.html")
        
if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)