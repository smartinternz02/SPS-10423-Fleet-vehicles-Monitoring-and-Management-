# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:33:00 2021

@author: ADITYA
"""
from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('Home.html')
@app.route('/Admin',methods=['POST','GET'])
def Admin():
    if request.method=="POST":
        return render_template('Admin.html')
    else:
        return render_template('Home.html')
@app.route('/Emp',methods=['POST','GET'])
def Emp():
    if request.method=="POST":
        return render_template('Emp.html')
    else:
        return render_template('Home.html')
if __name__ == '__main__':
    app.run()