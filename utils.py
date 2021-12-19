def black_areas_to_white(img):
    img_to_return = img.copy()
    height, width = img.shape

    for i in range(height):        
        for j in range(width):            
            if img_to_return[i, j] == 0:                
                img_to_return[i, j] = 255
    
    return img_to_return

def create_zero_copy(img_original):    
    img_out = img_original.copy()
    height, width, channels = img_original.shape
    
    for i in range(height):        
        for j in range(width):            
            for c in range(channels):                
                img_out[i, j, c] = 0
    
    return img_out

def separate_parasite(image_threshold, original_image):    
    only_parasite = create_zero_copy(original_image)

    height, width = image_threshold.shape
    
    for i in range(height):        
        for j in range(width):            
            if image_threshold[i, j] == 255:                
                only_parasite[i, j] = original_image[i, j]
    
    return only_parasite

def separate_border(image_gray_scale, original_image, value_to_set):    
    only_border = create_zero_copy(original_image)    
    height, width = image_gray_scale.shape
    
    for i in range(height):        
        for j in range(width):            
            if image_gray_scale[i, j] == 0:                
                only_border[i, j] = value_to_set
    
    return only_border

def color_image_area(area, original_image, color_rgb):    
    result_image = original_image.copy()
    
    height, width, channel = result_image.shape
    
    for i in range(height):        
        for j in range(width):            
            for c in range(channel):                
                if area[i, j, c] != 0:                    
                    result_image[i, j] = color_rgb
    
    return result_image
