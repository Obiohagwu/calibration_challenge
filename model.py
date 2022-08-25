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
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)

from feed_display import FeedDisplay
from featureExtraction import FeatureExtractor

## Have to 
W = 1920//2
H= 1080//2


display = FeedDisplay(W,H)
#window = sdl2.ext.Window("SLAM-FEED", size=(W, H), position=(-500,500))
#window.show() 

feature_extractor = FeatureExtractor()

def process_frame(img):
    img = cv2.resize(img,(W,H))
    matches = feature_extractor.extract_feature(img)
    
    print("%d matches found! " % (len(matches)))
    for pt1, pt2 in matches:
        u1,v1 = map(lambda x: int(round(x)), pt1)
        u2, v2 = map(lambda x: int(round(x)), pt2)
        cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
        cv2.line(img, (u1, v1), (u2, v2), color=(255, 0, 0))



   
    display.make(img)
#    log_events = sdl2.ext.get_events()
#    for event in log_events:
#        if event.type == sdl2.SDL_QUIT:
#            exit(0)
#    print(dir(window))
#    surf = sdl2.ext.pixels2d(window.get_surface())
#    surf[:] = img.swapaxes(0,1)[:, :, 0]
#    window.refresh()
    #cv2.imshow('FEED', img)
    #cv2.waitKey(0)
    #print(img.shape)
    #print(img)
    


def test():
    print("Testing")

if __name__ == "__main__":
    cap = cv2.VideoCapture("unlabeled/8.hevc")
    
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