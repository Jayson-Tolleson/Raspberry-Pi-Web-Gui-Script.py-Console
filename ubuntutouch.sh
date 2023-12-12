#!/usr/bin/env bash
#for use on Pixel 3 Ubuntu Touch as hardware( instead of Raspberry Pi or other SBC)

sudo mount -o remount,rw /
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo python3 -m pip install git+https://github.com/npinto/opencv.git
sudo python3 -m pip install flask
