import numpy as np
import argparse
import glob
import cv2

def auto_canny(image, sigma=0.33):
    # compute median 
    median = np.median(image)

    # Auto canny
    lower = int(max(0, (1.0 - sigma) * median ))
    upper = int(min(255, (1.0 + sigma) * median))
    edgeImage = cv2.Canny(image, lower, upper)

    return edgeImage