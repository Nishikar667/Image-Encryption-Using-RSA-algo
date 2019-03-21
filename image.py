from PIL import Image
import numpy as np
from pylab import * 
#encryption
img1 = (Image.open('image.jpeg').convert('L')) 
img1.show()

img = array((Image.open('image.jpeg').convert('L')))
img16 = np.array(img, dtype=np.uint32)
#img = Image.fromarray(img)
#img.save('img.bmp')
#img = array((Image.open('img.bmp').convert('i')))
a,b = img.shape
print('\n\nOriginal image: ')
print(img16)
print((a,b))
tup = a,b

for i in range (0, tup[0]):
	for j in range (0, tup[1]):
		x = img16[i][j] 
		x = (pow(x,3)%25777)
		img16[i][j] = x
print('\n\nEncrypted image: ')
print(img16)
imgOut = Image.fromarray(img16)
imgOut.show()
##imgOut.save('img.bmp')

#decryption

##img2 = (Image.open('img.bmp').convert('L'))
##img2.show()
img3_16 = img16
img3_16 = np.array(img, dtype=np.uint32)
print('\n\nEncrypted image: ')
print(img3_16)
a1,b1 = img3_16.shape
print((a1,b1))
tup1 = a1,b1

for i1 in range (0, tup1[0]):
	 for j1 in range (0, tup1[1]):
		 x1 = img3_16[i1][j1] 
		 x1 = (pow(x,16971)%25777)	
		 img3_16[i][j] = x1
		 #img3[i1][j1]= (img3[i1][j1] % 256)
print('\n\nDecrypted image: ')
print(img3_16)
imgOut1 = Image.fromarray(img3_16)
imgOut1.show()
print(type(img3_16))
#imgOut1.save('img1.bmp')

