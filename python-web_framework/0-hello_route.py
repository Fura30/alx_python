#!/usr/bin/python3
#import  Flask class
from flask import Flask
#instance of class 
app = Flask (__name__)
# app routing for our url 
@app.route('/', strict_slashes=False)
def hello():
	return "Hello HBNB"
	
if __name__ == '__main__ ':
   app.run(host='0.0.0.0', port=5000)
