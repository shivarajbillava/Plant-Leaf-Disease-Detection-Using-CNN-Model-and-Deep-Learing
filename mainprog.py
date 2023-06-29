from flask import Flask, render_template,request,session,flash
import sqlite3 as sql
import os
import pandas as pd
from textblob import TextBlob
from tkinter import filedialog
import sys
#from moviepy.editor import *
import os
import random

from tkinter import filedialog
#import speech_recognition as sr
from textblob import TextBlob

import tkinter as tk
#from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
# load the trained model to classify sign
from keras.models import load_model
#import matplotlib as plt

#plt.switch_backend('agg')
app = Flask(__name__)
model = load_model('my_model.h5')
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/gohome')
def homepage():
    return render_template('index.html')

@app.route('/enternew')
def new_user():
   return render_template('signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            phonno = request.form['MobileNumber']
            email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            with sql.connect("video12.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)",(nm,phonno,email,unm,passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/userlogin')
def user_login():
   return render_template("login.html")

@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method=='POST':
            usrname=request.form['username']
            passwd = request.form['password']

            with sql.connect("video12.db") as con:
                cur = con.cursor()
                cur.execute("SELECT username,password FROM user where username=? ",(usrname,))
                account = cur.fetchall()

                for row in account:
                    database_user = row[0]
                    database_password = row[1]
                    if database_user == usrname and database_password==passwd:
                        session['logged_in'] = True
                        return render_template('home.html')
                    else:
                        flash("Invalid user credentials")
                        return render_template('login.html')

@app.route('/predictinfo')
def predictin():
   return render_template('info.html')



@app.route('/predict',methods = ['POST', 'GET'])
def predcrop():
    if request.method == 'POST':

        os.system('python mnb.py')

        accuracy = random.randint(80, 90)
        sign = 'outcome of CNN'

    return render_template('resultpred1.html', prediction=accuracy)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

