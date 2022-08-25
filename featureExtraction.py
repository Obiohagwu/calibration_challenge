import time 
import cv2 
import numpy as np
from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform



# We use this script to extract fictures from the feed..
# These features are extracted by decomposing the feed img into a grid, then applying extraction to those
# This is useful to parameterize view to perform transformations with SLAM
class FeatureExtractor(object):
    GRID_X = 16//2
    GRID_Y = 12//2
    def __init__(self):
        self.orb = cv2.ORB_create(100)
        # For matcher
        self.bf_matcher = cv2.BFMatcher()
        self.end = None

    def extract_feature(self, img):

        # For feature detection
        features = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)

        # To extract features
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in features]
        kps, des = self.orb.compute(img, kps)

        # For matching extracted features
        intern = []
        #matches = None
        if self.end is not None:
            matches = self.bf_matcher.knnMatch(des, self.end["des"], k=2) #impolement brute force mathcing eith knn cluster where k=2
            #print(matches)
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    kp1 = kps[m.queryIdx].pt
                    kp2 = self.end['kps'][m.trainIdx].pt
                    intern.append((kp1, kp2))
                    
        # Fundamental matrix filter governs how points correspond to each other in euclidean 3d space
        # Wiki -  FMF is a 3*3 matrrix which relates points in stero images
        # We use ransac estimator to stay within bounds of FMF eqn
        if len(intern)>0:
            intern = np.array(intern)
            model, inliners = ransac((intern[:, 0], intern[:, 1]), FundamentalMatrixTransform, min_samples=8, residual_threshold=1, max_trials=100)
            



            intern = intern[inliners]
        self.end = {'kps': kps, 'des': des}

        #print(features)
        #return kps, des, matches

        
        return intern
        #return features