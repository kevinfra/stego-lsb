import os
from PIL import Image


if __name__ == '__main__':

	image_path = input ("Enter path of image to decode \n")
	if image_path.find('.bmp') == -1:
		print("Image must be *.bmp")
		exit()

	input_image = Image.open(image_path)
	width, height = input_image.size

	# para obtener los headers, se usa un standard de k = 2 bits	
	header = ''
	text_size = '' # tamaño del texto en bits
	int_k = ''
	text = ''

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
				#proceso el resto de la imagen
				text = text + r_bits[-int_k:] + g_bits[-int_k:] + b_bits[-int_k:]
				

	hidden_message = int('0b'+text, 2)
	hidden_message = hidden_message.to_bytes((hidden_message.bit_length() + 7) // 8, 'big').decode()
	print("The hidden message is: '", hidden_message, "'")



	