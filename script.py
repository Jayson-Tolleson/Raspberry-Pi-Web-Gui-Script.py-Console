#!/usr/bin/env python3
import subprocess
import sys
from flask import Flask, render_template, Response
import cv2

###Terminal Command
termcommand = str(sys.argv[1]).strip("'")
print (termcommand)
subprocess.call(termcommand, shell=True, stderr=subprocess.STDOUT)
###Video Camera Feed
app = Flask(__name__, static_url_path='/static')
cap = cv2.VideoCapture(0)
@app.route('/')
def index():
    return render_template('index.html')
def gen():
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imwrite('static/t.jpg', frame)
        yield (b'--frame\r\n'          b'Content-Type: image/jpeg\r\n\r\n' + open('static/t.jpg', 'rb').read() + b'\r\n')
@app.route('/cam_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True, ssl_context=('static/lftr.biz.crt', 'static/lftr.biz.key'), port=8000, threaded=True) #run on web option, get cert and key
    app.run(host='0.0.0.0',port=8000, threaded=True) #run on web option, get cert and key
