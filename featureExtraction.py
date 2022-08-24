import time 
import cv2 
import numpy as np

# We use this script to extract fictures from the feed..
# These features are extracted by decomposing the feed img into a grid, then applying extraction to those
# This is useful to parameterize view to perform transformations with SLAM
class FeatureExtractor(object):
    GRID_X = 16//2
    GRID_Y = 12//2
    def __init__(self):
        self.orb = cv2.ORB_create(100)

    def extract_feature(self, img):

        features = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        print(features)
        return features