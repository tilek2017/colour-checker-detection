import os
from colour import read_image
from colour_checker_detection import ROOT_RESOURCES_TESTS
path = os.path.join(ROOT_RESOURCES_TESTS,"colour_checker_detection","IMG_1967.png",)
image = read_image(path)
colour_checkers_coordinates_segmentation(image)
