from flask import Flask, render_template, request
from app import app
import requests
import json
import os

import method_test;

os.makedirs(os.path.join(app.instance_path, 'tobeProcessed'), exist_ok=True)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"



@app.route('/run')
def run():
    return method_test.sa();
    # return "running"



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save("./toprocess/" + f.filename)
      f.save(os.path.join(app.instance_path, "tobeProcessed", f.filename))
      return 'file uploaded successfully'

@app.route('/process', methods = ['GET', 'POST'])
def getsignedUrl():
    r = requests.get(
        'https://p821k8wid6.execute-api.ap-southeast-1.amazonaws.com/dev/presignedurls?folder=test&file=mango')
    print(r.json()["input"]["url"])

    # PROCESS THE IMAGE HERE

    requests.put(r.json()["input"]["url"], open(os.path.join(app.instance_path, "tobeProcessed", "todelete"), 'rb'))
    return "DONE";

# curl --location --request POST '127.0.0.1:5000/uploader' \
# --header 'Content-Type: multipart/form-data; boundary=--------------------------317668598226741062001227' \
# --form 'file=@/Users/sima/Downloads/res (1).png'
