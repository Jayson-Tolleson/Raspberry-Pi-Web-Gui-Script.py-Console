#!/usr/bin/env bash
sudo apt update
sudo apt install python3
sudo apt install git
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo python3 -m pip3 install flask
sudo python3 -m pip3 install opencv-python
sudo echo "[Unit]
Description=Custom Python Service
After=multi-user.target
Conflicts=getty@tty1.service
[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/jay/Raspbperry-Pi-Web-Gui-Script/console.py
StandardInput=tty-force
[Install]
WantedBy=multi-user.target" >  /lib/systemd/system/console.service
sudo systemctl daemon-reload
