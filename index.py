# Authors: Douglas Martins, Gabriel Burich e Gabriel Souza
# Date: 11/10/2021
# Pipeline to process malaria images
import cv2
from utils import black_areas_to_white, is_image_all_back
from os import listdir, getcwd
from os.path import isfile, join
from shutil import copyfile


# Runs the algorithms in order to process the image
# in order to identify whether it represents an infected or not
# first parameter is the image to process
def pipeline_have_the_parasite(original_image):
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
    # If the image isn't all black, there is a parasite
    have_the_parasite = not is_image_all_back(image_threshold)
    # print("Have the parasite: " + str(have_the_parasite))
    return have_the_parasite


# separate the images in infected and uninfected
# based on the pipeline_have_the_parasite function
# first parameter is the image to process
def separate_the_images(base_dir):
    all_images_dir = base_dir + "/all-images"
    infected_images_dir = base_dir + "/infected"
    uninfected_images_dir = base_dir + "/uninfected"
    image_files = [file for file in listdir(all_images_dir) if isfile(join(all_images_dir, file)) and file.endswith(".png")]

    for image_name in image_files:
        image_dir = all_images_dir + "/" + image_name
        image = cv2.imread(image_dir)
        have_the_parasite = pipeline_have_the_parasite(image)
        if have_the_parasite:
            # move para infectado
            copyfile(image_dir, infected_images_dir + "/" + image_name)
        else:
            # move para não infectado
            copyfile(image_dir, uninfected_images_dir + "/" + image_name)


# Call the function

current_dir = getcwd()
separate_the_images(current_dir + "/images")
