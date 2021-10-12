# Authors: Douglas Martins, Gabriel Burich e Gabriel Souza
# Date: 11/10/2021
# Pipeline to process malaria images
import cv2
from utils import black_areas_to_white, separate_border, separate_parasite, color_image_area


# Runs the algorithms in order to process the image
# in order to identify whether it represents an infected or not
# first parameter is the image to process
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
    # Only parasite image
    only_parasite = separate_parasite(image_threshold, original_image)
    # Only border image
    only_border = separate_border(image_gray_scale, original_image, 0)
    # Only border image with border in white
    only_border_in_white = separate_border(image_gray_scale, original_image, 255)
    # Only cell image
    only_cell = cv2.subtract(original_image, only_parasite)

    # highlight the parasite to blue
    highlight = color_image_area(only_parasite, original_image, [255, 0, 0])

    # highlight the cell to green
    highlight = color_image_area(only_cell, highlight, [0, 255, 0])

    # highlight the border to red
    highlight = color_image_area(only_border_in_white, highlight, [0, 0, 255])

    # Show the images
    cv2.imshow("Only Parasite", only_parasite)
    cv2.imshow("Only Border", only_border)
    cv2.imshow("Only Cell", only_cell)
    cv2.imshow("highlight", highlight)
    cv2.imshow("Original Image", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
img = cv2.imread("/home/gburich/PycharmProjects/malaria-cell-detector/images/all-images/C167P128ReThinF_IMG_20151201_105354_cell_238.png")
pipeline_segmentation(img)
