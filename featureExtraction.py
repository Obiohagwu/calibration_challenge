import time 
import cv2 

# We use this script to extract fictures from the feed..
# These features are extracted by decomposing the feed img into a grid, then applying extraction to those
# This is useful to parameterize view to perform transformations with SLAM
class FeatureExtractor(object):
    GRID_X = 16//2
    GRID_Y = 12//2
    def __init__(self):
        self.orb = cv2.ORB_create(100)

    def extract_feature(self, img):

        # decompose view into grid. Then run detect on it
        view_y = img.shape[0]//self.GRID_Y
        view_x = img.shape[1]//self.GRID_X
        intermediate = []

        for dy in range(0, img.shape[0], view_y):
            for dx in range(0, img.shape[1], view_x):
                img_chunk = img[dy: dy+view_y, dx: dx+view_x]
                kp = self.orb.detect(img_chunk, None)
                for p in kp:
                    p.pt = (p.pt[0]+ dx, p.pt[1] + dy)
                    intermediate.append(p)
        return intermediate