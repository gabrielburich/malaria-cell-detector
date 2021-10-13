# Authors: Douglas Martins, Gabriel Burich e Gabriel Souza
# Date: 11/10/2021
# Pipeline to process malaria images
import cv2
from utils import black_areas_to_white, separate_border, separate_parasite, color_image_area


# Runs the algorithms in order to process the image
# segmental in background, cell and parasite.
# In addition to creating an image with each of
# these parts highlighted
# first parameter is the image to process
# returns an array with these images in order
# only_parasite, only_border, only_cell, highlight
def pipeline_segmentation(original_image):
    # Create a copy to not change the original image
    image_to_process = original_image.copy()
    # Convert image to gray scale to apply the threshold
    image_gray_scale = cv2.cvtColor(image_to_process, cv2.COLOR_BGR2GRAY)
    # Transforms the black edges into white
    # to not interfere with the identification of the parasite
    image_without_border = black_areas_to_white(image_gray_scale)
    # Apply the Binary inv threshold with the limit calc in 130
    # Only the parasite will be in white, the rest of the image in black
    # Images without the parasite will be all black
    ret, image_threshold = cv2.threshold(image_without_border, 130, 255, cv2.THRESH_BINARY_INV)
    # Creates only parasite data based on threshold
    only_parasite = separate_parasite(image_threshold, original_image)
    # Creates Only border data based on gray scale image
    only_border = separate_border(image_gray_scale, original_image, 0)
    # Creates Only border data based on gray scale image with border in white
    # This will be used to highlight de border
    only_border_in_white = separate_border(image_gray_scale, original_image, 255)
    # Creates Only cell image, based on original image - only parasite image
    only_cell = cv2.subtract(original_image, only_parasite)

    # highlight the parasite with blue color
    highlight = color_image_area(only_parasite, original_image, [255, 0, 0])

    # highlight the cell with green color
    highlight = color_image_area(only_cell, highlight, [0, 255, 0])

    # highlight the border with red color
    highlight = color_image_area(only_border_in_white, highlight, [0, 0, 255])

    # return the images into an array
    return [only_parasite, only_border, only_cell, highlight]
