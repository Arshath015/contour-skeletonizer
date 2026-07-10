from .contour_detection import ContourDetector
from .skeletonizer import Skeletonizer

class ContourSkeletonizer:
    def __init__(self):
        pass
    def generate_cad_blueprint(self, image_path):
        image = cv2.imread(image_path)
        detector = ContourDetector(image)
        contours = detector.detect_contours()
        skeletonizer = Skeletonizer(contours)
        skeleton = skeletonizer.skeletonize()
        cv2.imwrite('cad_blueprint.png', skeleton)