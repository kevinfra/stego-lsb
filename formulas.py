sumTotalR = 0
sumTotalG = 0
sumTotalB = 0
for i in range(width):
	for j in range(height):
		r,g,b = original_image.getpixel((i,j))
		s,h,c = output_image.getpixel((i,j))
		sumR = (r-s)**2
		sumG = (g-h)**2
		sumB = (b-c)**2
		sumTotalR = sumTotalR + sumR
		sumTotalG = sumTotalG + sumG
		sumTotalB = sumTotalB + sumB

meanOriginal = np.mean(np.array(original_image))
meanOutput = np.mean(np.array(output_image))
varianceOriginal = np.var(np.array(original_image))
varianceOutput = np.var(np.array(output_image))
covariance = np.cov(np.array(original_image),np.array(output_image))
dynRange = 2 ** 24 - 1
k1 = 0.01
k2 = 0.03
c1 = (k1 * dynRange) ** 2
c2 = (k2 * dynRange) ** 2
ssimT = (2 * meanOriginal * meanOutput + c1) * (2 * covariance + c2) 
ssimB = (meanOriginal ** 2 + meanOutput ** 2 + c1) * (varianceOriginal ** 2 + varianceOutput ** 2 + c2) 


errorCuadraticoMedio = (sumTotalR + sumTotalG + sumTotalB) / (3 * width * height)
peakSignalToNoiseRatio = 10 * ((log(65025 / errorCuadraticoMedio)) / (log(10)))
ssim = ssimT / ssimB