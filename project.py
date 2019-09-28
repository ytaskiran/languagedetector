# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:59:21 2019

@author: ytask
"""

from languagedetector import detectLang
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',methods=[ 'POST'])
def hello_world():
    return detectLang(request.json["text"])

