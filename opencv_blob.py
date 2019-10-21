#%%
# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread('./banner_connected_areas.jpg',0)
# cv2.imshow('abc',im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255))
 
# Show keypoints
print(keypoints)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
