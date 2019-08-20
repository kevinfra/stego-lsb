import os
from PIL import Image


def find_hidden_message(input_image):
	# to obtain header info, we set a standard of k = 2 bits	
	int_k = ''
	header = ''
	text_size = '' #hidden message size in bits
	hidden_message = ''
	width, height = input_image.size


	for i in range(width):
		for j in range(height):
			r,g,b  = input_image.getpixel((i,j))

			r_bits = '{0:08b}'.format(r)
			g_bits = '{0:08b}'.format(g)
			b_bits = '{0:08b}'.format(b)

			if j < 6 and i == 0:
				#taking first 36 pixels, text-size in bits and 4 bits for k
				header = header + r_bits[-2:] + g_bits[-2:] + b_bits[-2:]
				if j == 5 and i == 0:
					#separate header 
					text_size = int(text_size + header[0:32], 2)
					int_k = int(int_k + header[32:36], 2)
			else:
				#getting the hidden message
				left_to_process = text_size - len(hidden_message)
				info_in_pixel = r_bits[-int_k:] + g_bits[-int_k:] + b_bits[-int_k:]

				if(left_to_process < int_k*3): #bits that are info in a pixel that is not full with info
					hidden_message = hidden_message + info_in_pixel[:left_to_process]
					return hidden_message

				else:
					hidden_message = hidden_message + info_in_pixel
					
	return hidden_message
################################################################################				


if __name__ == '__main__':

	image_path = input ("Enter path of image to decode \n")
	if image_path.find('.bmp') == -1:
		print("Image must be *.bmp")
		exit()

	input_image = Image.open(image_path)

	hidden_message = find_hidden_message(input_image)

	hidden_message = int('0b' + hidden_message, 2)
	hidden_message = hidden_message.to_bytes((hidden_message.bit_length() + 7) // 8, 'big').decode()
	print("The hidden message is: '", hidden_message, "'")



	
