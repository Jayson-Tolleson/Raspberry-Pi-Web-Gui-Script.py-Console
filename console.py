#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import subprocess
from subprocess import Popen, PIPE, STDOUT
from flask import Flask, Response, request, render_template, redirect, url_for
import time
app = Flask(__name__, static_url_path='/static')
@app.route('/out/<number>')
def out(number):
  def output():
    yield """<html><style>div#container{background: black;width: 50%;margin: 100px auto;color: white;border-radius: 1em;width: 1080px;height: 720px;overflow:hidden;overflow-x:hidden;-webkit-resize:vertical;-moz-resize:vertical;} iframe#Frame,iframe#Frame2
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
<div id='container'><iframe id='Frame' scrolling='no'src='localhost:8000/cam_feed' frameborder='0'></iframe></div>
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
@app.route('/console',methods = ['POST', 'GET'])
def searchterms():
    if request.method == 'POST':
        codeblock = request.form['codeblock']
        return redirect(url_for('out', codeblock = codeblock))
    else:
        codeblock = request.args.get('codeblock')
        return """<html><style>body {background: #1339de;} #data { text-align: center; }</style><body><h1>Single Board Computer -  CONTROL CONSOLE!!!</h1><br><br><form method ='POST'>   
        OPTIONS: ...<br>   
        SBC terminal command input: <input type='text' name='Terminal Command' id='termcommand' value='sudo pip3 install your best module  --break-system-packages'><br>
        SBC GPIO Camera: <input type='radio' name='0n/0ff' id='0n/0ff'><input type='radio' name='Live Cam Feed' id='livecam'>
<br>HBridge Motor Controller: <input type='radio' name='PWMA' id='PWMA'>
<br>HBridge Motor Controller: <input type='radio' name='AIN1' id='AIN1'>
<br>HBridge Motor Controller: <input type='radio' name='AIN2' id='AIN2'>
<br>HBridge Motor Controller: <input type='radio' name='standby' id='standby'>
<br>HBridge Motor Controller: <input type='radio' name='BIN1' id='BIN1'>
<br>HBridge Motor Controller: <input type='radio' name='BIN2' id='BIN2'>
<br>HBridge Motor Controller: <input type='radio' name='PWMB' id='PWMB'><br>
        <input type='radio' name='Live Cam Feed' id='livecam'><br>   CodeBlock.py: <input type='text' name='codeblock' id='codeblock' value='#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import subprocess
from subprocess import Popen, PIPE, STDOUT
from flask import Flask, Response, request, render_template, redirect, url_for
import time'>
   <input type='submit' value='RUN Selection'></form></body></html>"""
if __name__ == "__main__":  
    app.run(host='0.0.0.0', debug=True, port=8080)
    #app.run(host='0.0.0.0', debug=True, ssl_context=('/var/security/lftr.biz.crt', '/var/security/lftr.biz.key'), port=8080) #run on web option, get cert and key
