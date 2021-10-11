# Authors: Douglas Martins, Gabriel Burich e Gabriel Souza
# Date: 11/10/2021
# Pipeline to process malaria images
import cv2
from utils import black_areas_to_white, is_image_all_back


def pipeline(original_image):
    # Create a copy to not change the original image
    image_to_process = original_image.copy()
    # Convert image to gray scale to apply the threshold
    image_gray_scale = cv2.cvtColor(image_to_process, cv2.COLOR_BGR2GRAY)
    # Transforms the black edges into white
    # to not interfere with the identification of the parasite
    image_without_border = black_areas_to_white(image_gray_scale)
    # Apply the Binary inv threshold with the limit calc in 80
    # Only the parasite will be in white, the rest of the image in black
    # Images without the parasite will be all black
    ret, image_threshold = cv2.threshold(image_without_border, 80, 255, cv2.THRESH_BINARY_INV)
    # If the image isn't all black, there is a parasite
    have_the_parasite = not is_image_all_back(image_threshold)
    print("Tem o parasita: " + str(have_the_parasite))


# image = cv2.imread("/home/gburich/Downloads/cell_images/cell_images/Parasitized/C33P1thinF_IMG_20150619_121229a_cell_177.png")
image = cv2.imread("/home/gburich/Downloads/cell_images/cell_images/Uninfected/C1_thinF_IMG_20150604_104722_cell_143.png")

pipeline(image)

# cv2.imshow('Original image', image)
# cv2.imshow('Gray image', gray)
# cv2.imshow('Sem borda', without_border_image)
# cv2.imshow('Soh o parasita', thresholdImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

