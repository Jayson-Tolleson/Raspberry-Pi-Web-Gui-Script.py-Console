#!/usr/bin/env python3
import subprocess
from flask import Flask, render_template, Response
import cv2
import pigpio

###Terminal Command
termcommand = str(sys.argv[1])
print (termcommand)
subprocess.call(termcommand, shell=True, stderr=subprocess.STDOUT)

###Motor Controller Board
pi = pigpio.pi() 
#set gpio pins
pi.set_mode(7, pigpio.OUTPUT)  #pin 7 as output pwma
pi.set_mode(11, pigpio.OUTPUT) #pin 11 as output ain1
pi.set_mode(12, pigpio.OUTPUT) #pin 12 as output ain2
pi.set_mode(13, pigpio.OUTPUT) #pin 13 as output stdby
pi.set_mode(15, pigpio.OUTPUT) #pin 15 as output bin1
pi.set_mode(16, pigpio.OUTPUT) #pin 16 as output bin2
pi.set_mode(18, pigpio.OUTPUT) #pin 18 as output pwmb
#reset all gpio pins
pi.write(11, 0) #reset pin11 ain1
pi.write(12, 0) #reset pin12 ain2
pi.write(7, 0) #reset pin7 pwma
pi.write(13, 0) #reset pin13 stdby
pi.write(15, 0) #reset pin15 bin1
pi.write(16, 0) #reset pin16 bin2
pi.write(18, 0) #reset pin18 pwmb

###Video Camera Feed
app = Flask(__name__, static_url_path='/static')
video = cv2.VideoCapture(0)
@app.route('/')
def gen():
    while(video.isOpened()):
        rval, frame = video.read()
        if rval:
            video.set(3, 1080)
            video.set(4, 720)
            cv2.imwrite('t.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')
        else:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
@app.route('/cam_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, ssl_context=('/static/lftr.biz.crt', '/static/lftr.biz.key'), port=8000, threaded=True)
    
