#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import subprocess
from subprocess import Popen, PIPE, STDOUT
from flask import Flask, Response, request, render_template, redirect, url_for
import time
import socket
def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]

app = Flask(__name__, static_url_path='/static')
@app.route('/out/<motoron>/<codeblock>/<termcommand>/<camlive>/<PWMA>/<AIN1>/<AIN2>/<standby>/<BIN1>/<BIN2>/<PWMB>')
def out(motoron,codeblock,termcommand,camlive,PWMA,AIN1,AIN2,standby,BIN1,BIN2,PWMB):
  def output():
    yield """<html><style>div#container{background: black;width: 50%;margin: 100px auto;color: white;border-radius: 1em;width: 1080px;height: 720px;overflow:hidden;overflow-x:hidden;-webkit-resize:vertical;-moz-resize:vertical;} iframe#Frame
{  
    width:1500px;       /* set this to approximate width of entire page you're embedding */
    height:1200px;      /* determines where the bottom of the page cuts off */
    margin-left:00px; /* clipping left side of page */
    margin-top:0px;  /* clipping top of page */
    overflow:hidden;
    /* resize seems to inherit in at least Firefox */
    -webkit-resize:none;
    -moz-resize:none;
    resize:none;
}
</style><body style='color:MediumSeaGreen;'><h1><div id='data' style='text-align: center;'>nothing received yet...for </div></h1><script>var div = document.getElementById('data');</script><script type='text/javascript'>
   setInterval(refreshIframe, 12000);
   function refreshIframe() {
       var frame = document.getElementById('Frame');
       frame.src = frame.src; }
</script>
<div id='container'><iframe id='Frame' scrolling='no'src='http://"""+getNetworkIp()+""":8000' frameborder='0'></iframe></div>
</body></html>"""
    file1 = open('codeblock.py', 'w')
    s = str(codeblock)
    file1.write(s)
    file1.close()
    p = subprocess.Popen('sudo python3 codeblock.py && sudo python3 script.py '+str(termcommand), shell=True, stdout=subprocess.PIPE, stderr=STDOUT)
    while True:
        out = ((p.stdout.readline()).strip()) 
        out =str(out)
        if out != "b''":
            print (out)
            yield """<html><body><h1><script>div.innerHTML = "OUTPUT: """+out+""" "</script></h1></body></html>"""
  return Response(output())
@app.route('/consoleGUI',methods = ['POST', 'GET'])
def searchterms():
    if request.method == 'POST':
        termcommand = request.form['termcommand'] 
        camlive = request.form['livecam']       
        motoron=request.form['motoron']      
        PWMA = request.form['PWMA']
        AIN1 = request.form['AIN1']
        AIN2 = request.form['AIN2']
        standby  = request.form['standby']
        BIN1 = request.form['BIN1']
        BIN2 = request.form['BIN2']
        PWMB = request.form['PWMB']
        codeblock = request.form['codeblock']
        return redirect(url_for('out',motoron=motoron,codeblock = codeblock,termcommand = termcommand,camlive=camlive,PWMA=PWMA,AIN1=AIN1,AIN2=AIN2,standby=standby,BIN1=BIN1,BIN2=BIN2,PWMB=PWMB))
    else:
        motoron=request.args.get('motoron')
        codeblock = request.args.get('codeblock')
        termcommand = request.args.get('termcommand')
        camlive = request.args.get('livecam')
        PWMA = request.args.get('PWMA')
        AIN1 = request.args.get('AIN1')
        AIN2 = request.args.get('AIN2')
        standby  = request.args.get('standby')
        BIN1 = request.args.get('BIN1')
        BIN2 = request.args.get('BIN2')
        PWMB = request.args.get('PWMB')
        return """<html><style>body {background: #1339de;} #data { text-align: center; }</style><body><h1>Single Board Computer -  CONTROL CONSOLE!!!</h1><br><br><form method ='POST'>   
        OPTIONS: ...<br>   
        SBC terminal command input: <input type='text' name='termcommand' id='termcommand' value='sudo lsusb'><br>
        SBC GPIO Camera: <label>LiveFeed(on-1/off-0)</label><input type='text' name='livecam' id='livecam' value='0'>
        <br>HBridge Motor Controller: <label>on/off-(1/0)</label><input type='text' name='motoron' id='motoron' value ='0'>
<br>HBridge Motor Controller: <label>PWMA on/off</label><input type='text' name='PWMA' id='PWMA'  value ='0'>
<br>HBridge Motor Controller: <label>AIN1 on/off</label><input type='text' name='AIN1' id='AIN1'  value ='0'>
<br>HBridge Motor Controller: <label>AIN2 on/off</label><input type='text' name='AIN2' id='AIN2'  value ='0'>
<br>HBridge Motor Controller: <label>Standby on/off</label><input type='text' name='standby' id='standby'  value ='0'>
<br>HBridge Motor Controller: <label>BIN1 on/off</label><input type='text' name='BIN1' id='BIN1'  value ='0'>
<br>HBridge Motor Controller: <label>BIN2 on/off</label><input type='text' name='BIN2' id='BIN2'  value ='0'>
<br>HBridge Motor Controller: <label>PWMB on/off</label><input type='text' name='PWMB' id='PWMB'  value ='0'><br>
CodeBlock.py: <input type='text' name='codeblock' id='codeblock' value=' '><br>
   <input type='submit' value='RUN Selection'></form></body></html>"""
if __name__ == "__main__":  
   # app.run(host='0.0.0.0', debug=True, ssl_context=('static/lftr.biz.crt', 'static/lftr.biz.key'), port=8080) #run on web option, get cert and key
   
    app.run(host='0.0.0.0', port=8080)
