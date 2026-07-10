import pytest
from src.contour_detection import ContourDetector

def test_contour_detection):
    detector = ContourDetector(cv2.imread('test_image.jpg'))
    contours = detector.detect_contours()
    assert len(contours) > 0

def test_contour_detection_edge_case):
    detector = ContourDetector(cv2.imread('edge_case_image.jpg'))
    contours = detector.detect_contours()
    assert len(contours) > 0