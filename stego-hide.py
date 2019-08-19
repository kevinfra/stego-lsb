import os
from PIL import Image


# binary_text is a string like '0b010101'
def valid_text_length_image_size_and_admissible_bits(binary_text, width, height, k):
    if k < 2 or k > 8:
        print("admissible bit is not right")
        return False
    total_bites = width * height * 3 * 8
    if total_bites - (len(binary_text) - 2) - 4 - 32 <= 0:
        print("image is not big enough")
        return False
    return True


if __name__ == '__main__':
    file_name = str(input())
    text = str(input())
    admissible_bits = int(input())

    text_to_hide = bin(int.from_bytes(text.encode(), 'big'))

    original_image = Image.open(file_name)
    width, height = original_image.size
    if not valid_text_length_image_size_and_admissible_bits(text_to_hide, width, height, admissible_bits):
        exit()
    output_image = Image.new('RGB', [width, height], 0)


    for i in range(width):
        for j in range(height):
            r,g,b = original_image.getpixel((i,j))
            #hide_text_in_pixel(rgba)
            output_image.putpixel((i,j), [r,g,b])
