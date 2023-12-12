#!/usr/bin/env bash
#for use on Pixel 3 Ubuntu Touch as hardware( instead of Raspberry Pi or other SBC)
sudo mount -o remount,rw /
sudo apt-get update
sudo apt install git build-essential cmake pkg-config libjpeg62-dev python3-numpy libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libv4l-dev libtbb-dev ffmpeg v4l-utils libgtk2.0-dev python3-flask
sudo git clone https://github.com/npinto/opencv.git
cd opencv
sudo mkdir build
cd build
sudo cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local
    -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON ..
sudo make
sudo make install
