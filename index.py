# Date: 11/10/2021
# Pipeline to process malaria images

import cv2

# Melhorar legal esse código, criar metoto has parasite slá, que verifica se a imagem não é toda preta
# ou chamar o metodo de is_image_only_black tambem resolve.

# para as bordas pretas da imagem não serem reconhecidas como o parasita.
def black_to_white(img):
    img_to_return = img.copy()

    # Get image dimensions to manipulate
    height, width = img.shape

    # run through the lines
    for i in range(height):
        # run through the columns
        for j in range(width):
            if img_to_return[i, j] == 0:
                img_to_return[i, j] = 255

    return img_to_return

image = cv2.imread("/home/gburich/Downloads/cell_images/cell_images/Parasitized/C33P1thinF_IMG_20150619_121229a_cell_177.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tem como manter o preto preto?
# converter tudo que é preto para branco em um step antes
without_border_image = black_to_white(gray)
ret, thresholdImage = cv2.threshold(without_border_image, 80, 255, cv2.THRESH_BINARY_INV)


cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)
cv2.imshow('Sem borda', without_border_image)
cv2.imshow('Soh o parasita', thresholdImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

