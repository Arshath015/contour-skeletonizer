import cv2
import numpy as np

class Skeletonizer:
    def __init__(self, contours):
        self.contours = contours
    def skeletonize(self):
        skeleton = np.zeros((self.contours.shape[0], self.contours.shape[1]), dtype=np.uint8)
        for contour in self.contours:
            for point in contour:
                x, y = point[0]
                skeleton[y, x] = 255
        return skeleton