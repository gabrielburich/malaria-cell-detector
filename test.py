# Authors: Douglas Martins, Gabriel Burich e Gabriel Souza
# Date: 13/10/2021
# Run tests
import cv2
from pipeline_segmentation import pipeline_segmentation
from os import getcwd


# segments the images from images folder based on a prefix
# the first parameter is a string: infected or uninfected
# runs the pipeline and at end shows the result in the screen
def segments_images_and_show_result(prefix):
    current_dir = getcwd()
    for index in range(1, 6):
        img = cv2.imread(current_dir + "/images/" + prefix + "-" + str(index) + ".png")
        only_parasite, only_border, only_cell, highlight = pipeline_segmentation(img)

        # Show the images
        cv2.imshow("Only Parasite", only_parasite)
        cv2.imshow("Only Border", only_border)
        cv2.imshow("Only Cell", only_cell)
        cv2.imshow("highlight", highlight)
        cv2.imshow("Original Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# Execute the tests
segments_images_and_show_result("infected")
segments_images_and_show_result("uninfected")
