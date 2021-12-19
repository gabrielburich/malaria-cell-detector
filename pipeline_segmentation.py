import cv2
from utils import black_areas_to_white, separate_border, separate_parasite, color_image_area

def pipeline_segmentation(original_image):
    image_to_process = original_image.copy()
    image_gray_scale = cv2.cvtColor(image_to_process, cv2.COLOR_BGR2GRAY)
    image_without_border = black_areas_to_white(image_gray_scale)

    ret, image_threshold = cv2.threshold(image_without_border, 130, 255, cv2.THRESH_BINARY_INV)

    only_parasite = separate_parasite(image_threshold, original_image)
    only_border = separate_border(image_gray_scale, original_image, 0)
    only_border_in_white = separate_border(image_gray_scale, original_image, 255)
    only_cell = cv2.subtract(original_image, only_parasite)

    highlight = color_image_area(only_parasite, original_image, [255, 0, 0])
    highlight = color_image_area(only_cell, highlight, [0, 255, 0])
    highlight = color_image_area(only_border_in_white, highlight, [0, 0, 255])

    return [only_parasite, only_border, only_cell, highlight]
