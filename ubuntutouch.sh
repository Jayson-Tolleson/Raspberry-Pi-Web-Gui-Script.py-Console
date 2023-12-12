#!/usr/bin/env bash

sudo mount -o remount,rw /
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo python3 -m pip3 install flask
sudo apt update
sudo apt install git
sudo git clone https://github.com/npinto/opencv.git
cd opencv
sudo make
sudo make install
cd ..
sudo echo "[Unit]
Description=Custom Python Service
After=multi-user.target
Conflicts=getty@tty1.service
[Service]
Type=simple
ExecStart=/usr/bin/python3 ~/Documents/CommandConsole/console.py
StandardInput=tty-force
[Install]
WantedBy=multi-user.target" >  /lib/systemd/system/console.service
sudo systemctl daemon-reload
sudo systemctl enable console.service
sudo systemctl start console.service
sudo python3 console.py
