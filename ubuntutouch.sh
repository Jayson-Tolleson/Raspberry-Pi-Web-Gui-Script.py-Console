#!/usr/bin/env bash

sudo mount -o remount,rw /
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo apt-get update
sudo apt-get purge --auto-remove python-blinker
sudo apt install git-all
sudo python3 -m pip install git+https://github.com/npinto/opencv.git
sudo python3 -m pip install flask
