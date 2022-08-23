import numpy as np 
import cv2 
import torch 
import time 
import os

# To get video pop-up
import sys
import sdl2.ext
sdl2.ext.init()



# Let's try some stuff
# This calibratoin challenge seem to me like a canonical SLAM type problem

cv2.namedWindow('image', cv2.WINDOW_NORMAL)


## Have to 
W = 1920//2
H= 1080//2

 

def process_frame(img):
    img = cv2.resize(img,(W,H))
    log_events = sdl2.ext.get_events()
    cv2.imshow('live-video-feed', img)
    #cv2.waitKey(0)
    print(img.shape)
    print(img)
    window.refresh()


def test():
    print("Testing")

if __name__ == "__main__":
    cap = cv2.VideoCapture("unlabeled/7.hevc")
    
    i=0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
            i+=1
            
        else: 
            break
    print("Total number of frames:", i)
    #test()