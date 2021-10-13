# Authors: Douglas Martins, Gabriel Burich e Gabriel Souza
# Date: 11/10/2021
# Utility Functions to manipulate images

# Transforms the black areas into white
# Only consider absolute black [i, j] == 0
# first parameter is the image to process
# returns an image without black areas
def black_areas_to_white(img):
    # Create a copy to not change the original image
    img_to_return = img.copy()

    # Get image dimensions to manipulate
    height, width = img.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            # If the pixel is absolutely black
            if img_to_return[i, j] == 0:
                # Change to white
                img_to_return[i, j] = 255

    # returns the new image
    return img_to_return


# Creates a copy of the original image
# For each point set 0
# img_original original image
# return the new image
def create_zero_copy(img_original):
    # Create a copy to save the result
    img_out = img_original.copy()

    # Get image dimensions to manipulate
    height, width, channels = img_original.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            # run through the channels
            for c in range(channels):
                # In each point set 0
                img_out[i, j, c] = 0

    # Returns the result image
    return img_out


# Separates only the parasite on a different image
# The first parameter is a threshold image with only the parasite in white
# The second parameter is the original image to get the parasite image
# returns an image with only the parasite
def separate_parasite(image_threshold, original_image):
    # Creates a copy with all values in black
    only_parasite = create_zero_copy(original_image)

    # Get image dimensions to manipulate
    height, width = image_threshold.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            # if the value is 255
            if image_threshold[i, j] == 255:
                # set the pixel from original image on the result image
                only_parasite[i, j] = original_image[i, j]

    # returns the image with only the parasite
    return only_parasite


# Separates only the border on a different image
# The first parameter is a image in gray scale
# The second parameter is the original image to get the parasite image
# The last parameter is the value to set when identify the border
# returns an image with only the border
def separate_border(image_gray_scale, original_image, value_to_set):
    # Creates a copy with all values in black
    only_border = create_zero_copy(original_image)

    # Get image dimensions to manipulate
    height, width = image_gray_scale.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            # Identify the border with black value
            if image_gray_scale[i, j] == 0:
                # set the value on the pixel
                only_border[i, j] = value_to_set

    # returns the image with only border
    return only_border


# Highlight based on an area
# The first parameter is a image with only the area
# The second parameter is the original image to set the highlight area
# The last parameter is the color to set
def color_image_area(area, original_image, color_rgb):
    # Creates a copy with all values in black
    result_image = original_image.copy()

    # Get image dimensions to manipulate
    height, width, channel = result_image.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            # run through the channels
            for c in range(channel):
                # if the pixel in the area isn't black
                if area[i, j, c] != 0:
                    # set the color on the result image in the position
                    result_image[i, j] = color_rgb

    # returns the image with highlight area
    return result_image
