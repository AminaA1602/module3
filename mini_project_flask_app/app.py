# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:29:08 2019

@author: Skitt
"""

from flask import Flask, render_template 

app = Flask(__name__)


@app.route("/")

def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
    
