import pytest
from src.contour_skeletonizer import ContourSkeletonizer

def test_contour_skeletonizer):
    skeletonizer = ContourSkeletonizer()
    skeletonizer.generate_cad_blueprint('test_image.jpg')
    assert cv2.imread('cad_blueprint.png') is not None

def test_contour_skeletonizer_edge_case):
    skeletonizer = ContourSkeletonizer()
    skeletonizer.generate_cad_blueprint('edge_case_image.jpg')
    assert cv2.imread('cad_blueprint.png') is not None