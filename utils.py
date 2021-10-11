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


# Checks if all points in te image are black
# Only consider absolute black [i, j] == 0
# first parameter is the image to verify
# if all point is black return True
# otherwise False
def is_image_all_back(img):
    # Get image dimensions to manipulate
    height, width = img.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            # If some points isn't absolutely black
            if img[i, j] != 0:
                # Returns false
                return False

    # If all points is black, returns true
    return True
