from PIL import Image
import random

# binary_text is a string like '0b010101'
def valid_text_length_image_size_and_admissible_bits(binary_text, usable_bits, k):
    if k < 2 or k > 8:
        print("admissible bit is not right")
        return False
    if usable_bits - (len(binary_text) - 2) - 4 - 32 <= 0:
        print("image is not big enough")
        return False
    return True


def text_to_hide_with_padding(text, usable_bits, max_int):
    padding_size = usable_bits - (len(text) - 2) - 4 - 32
    result = text
    for n in range(padding_size):
        random_bin = random.randint(0, max_int)
        binary_representation = '{0:03b}'.format(random_bin)
        result = result + binary_representation
    return result


if __name__ == '__main__':
    file_name = str(input("file name"))
    if file_name.find('.bmp') == -1:
        print("image must be *.bmp")
        exit()
    input_text = str(input("text to hide"))
    admissible_bits = int(input("admissable bits"))

    text_to_hide = bin(int.from_bytes(input_text.encode(), 'big'))

    original_image = Image.open(file_name)
    width, height = original_image.size
    total_usable_bits = width * height * 3 * admissible_bits
    if not valid_text_length_image_size_and_admissible_bits(text_to_hide, total_usable_bits, admissible_bits):
        exit()

    final_text_binary = text_to_hide_with_padding(text_to_hide, total_usable_bits, (2**admissible_bits)-1)
    output_image = Image.new('RGB', [width, height], 0)

    bits_to_keep = 8 - admissible_bits
    current_text_index_from = 2
    current_text_index_to = current_text_index_from + admissible_bits

    text_length_and_admissible_bits_binary = '{0:032b}'.format(len(text_to_hide)-2) + '{0:04b}'.format(admissible_bits)
    header_from = 0
    header_to = 2
    for i in range(width):
        for j in range(height):
            r, g, b = original_image.getpixel((i, j))
            bin_R = '{0:08b}'.format(r)
            bin_G = '{0:08b}'.format(g)
            bin_B = '{0:08b}'.format(b)

            if i == 0 and j < 6:
                new_r = int(bin_R[0:6] + text_length_and_admissible_bits_binary[header_from:header_to], 2)
                header_from += 2
                header_to += 2
                new_g = int(bin_G[0:6] + text_length_and_admissible_bits_binary[header_from:header_to], 2)
                header_from += 2
                header_to += 2
                new_b = int(bin_B[0:6] + text_length_and_admissible_bits_binary[header_from:header_to], 2)
                header_from += 2
                header_to += 2
                output_image.putpixel((i, j), (new_r, new_g, new_b))
            else:
                new_r = int(bin_R[:bits_to_keep] + final_text_binary[current_text_index_from:current_text_index_to], 2)
                current_text_index_from += admissible_bits
                current_text_index_to += admissible_bits
                new_g = int(bin_G[:bits_to_keep] + final_text_binary[current_text_index_from:current_text_index_to], 2)
                current_text_index_from += admissible_bits
                current_text_index_to += admissible_bits
                new_b = int(bin_B[0:bits_to_keep] + final_text_binary[current_text_index_from:current_text_index_to], 2)
                current_text_index_from += admissible_bits
                current_text_index_to += admissible_bits
                output_image.putpixel((i, j), (new_r, new_g, new_b))

    output_name = file_name.replace('.bmp', '-stego.bmp')
    output_image.save(output_name)
