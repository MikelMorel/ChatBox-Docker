from flask import Flask
from flask import render_template,request
import os
from datetime import datetime
import mysql as sql

app = Flask(__name__)

config = {
	'user': 'root',
	'password': 'root',
	'host' : 'db' , 
	'port' : '3306' ,
	'database' : 'chatlog'
}
mysql = MySQL(app)



@app.route('/',methods=['GET'])
def hello_world():
	return render_template("index.html")

@app.route('/<room>',methods=['GET'])
def room(room):
	return render_template("index.html")

@app.route('/api/chat/<room>', methods=['POST','GET'])
def roompost(room):
	if request.method == 'GET':
		return render_template("index.html")
	else: request.method == 'POST':
		username = request.form'username']
		message = request.form['msg']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO log VALUES (%s , %s)",(username,message))
		mysql.connection.commit()
		cur.close
		return 'success'
	
	
	
	
	
	
	
	
	
	
	
	#data=""
	#if request.method == "POST":
	#	fileName = "/rooms" + room + ".txt" 
	#	with open(fileName, "a") as f:
	#		print (fileName)
	#		f.write("[{}] {}: {}\n".format(str(datetime.now()),request.form['username'],request.form['msg']))
	#	return render_template("index.html")
	#fileName = "/rooms" + room + ".txt"
	#if os.path.exists(fileName): 
	#	with open (fileName, "r") as f:
	#		data=f.read()
	#return (data) 

if __name__ =='__main__':
	app.run(host='0.0.0.0')
