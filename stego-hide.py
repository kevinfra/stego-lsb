from PIL import Image
import random


HEADERS_LENGTH = 4 + 32  # 4 bits for K and 32 bits for the length of the hidden message


# binary_text is a string like '0b010101'
def valid_input(binary_text, usable_bits, k):
    if k < 2 or k > 8:
        print("LSB number is invalid. Should be between 2 and 8.")
        return False
    if usable_bits - len(binary_text) - HEADERS_LENGTH <= 0:
        print("The image is too small to hide this text.")
        return False
    return True


def add_padding(text, usable_bits, k):
    max_int = (2 ** k) - 1  # largest number with k bits
    padding_size = usable_bits - len(text) - HEADERS_LENGTH  # 36 is the size of the headers in bits
    result = text
    for n in range(padding_size):
        r = random.randint(0, max_int)
        binary_representation = '{0:03b}'.format(r)
        result = result + binary_representation
    return result


if __name__ == '__main__':

    file_name = str(input("file name"))
    if file_name.find('.bmp') == -1:
        print("image must be *.bmp")
        exit()
    text_to_hide = str(input("text to hide"))
    k = int(input("number of least significant bits to use"))

    # text to binary with complete bytes
    text_to_hide = bin(int.from_bytes(text_to_hide.encode(), 'big'))[2:]
    while len(text_to_hide) % 8 != 0:
        text_to_hide = '0' + text_to_hide

    # check if message can be hidden
    original_image = Image.open(file_name)
    width, height = original_image.size
    total_usable_bits = width * height * 3 * k
    if not valid_input(text_to_hide, total_usable_bits, k):
        exit()

    # hide
    final_text_binary = add_padding(text_to_hide, total_usable_bits, k)
    output_image = Image.new('RGB', [width, height], 0)

    bits_to_keep = 8 - k
    text_index = 0

    header = '{0:032b}'.format(len(text_to_hide)) + '{0:04b}'.format(k)
    header_index = 0
    for i in range(width):
        for j in range(height):
            r, g, b = original_image.getpixel((i, j))
            bin_R = '{0:08b}'.format(r)
            bin_G = '{0:08b}'.format(g)
            bin_B = '{0:08b}'.format(b)

            if i == 0 and j < 6:  # set headers
                new_r = int(bin_R[0:6] + header[header_index:header_index+2], 2)
                header_index += 2
                new_g = int(bin_G[0:6] + header[header_index:header_index+2], 2)
                header_index += 2
                new_b = int(bin_B[0:6] + header[header_index:header_index+2], 2)
                header_index += 2
                output_image.putpixel((i, j), (new_r, new_g, new_b))
            else:  # set hidden text
                new_r = int(bin_R[:bits_to_keep] + final_text_binary[text_index:text_index + k], 2)
                text_index += k
                new_g = int(bin_G[:bits_to_keep] + final_text_binary[text_index:text_index + k], 2)
                text_index += k
                new_b = int(bin_B[:bits_to_keep] + final_text_binary[text_index:text_index + k], 2)
                text_index += k
                output_image.putpixel((i, j), (new_r, new_g, new_b))

    output_name = file_name.replace('.bmp', '-stego.bmp')
    output_image.save(output_name)
