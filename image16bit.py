import cv2 as cv 
import numpy as np
import png
import imageio 
import time
from tqdm import tqdm 

start = time.time()

img = cv.imread('images.jpeg', 0)
#print(type(img))
img = img.astype(np.uint16)
a,b = img.shape
print('\n\nOriginal image: ')
print(img)
print((a,b))
tup = a,b

for i in tqdm(range(0, tup[0])):
	for j in tqdm(range(0, tup[1])):
		x = img[i][j] 
		x = (pow(x,3)%25777)
		img[i][j] = x

print('\n\nEncrypted Image:\n\n')
print(img)
#cv.imshow('EnImage', img)
cv.imwrite('EnImg.png', img)



img1 = imageio.imread('EnImg.png')
print('\n\nReading Encrypted Image again:\n\n')
print(img1)

#for g in tqdm(range(100)):
img1= img1.tolist()
print('Decrypting....')
for i1 in tqdm(range(len(img1))):
	for j1 in tqdm(range(len(img1[i]))):
		x1 = img1[i1][j1] 
		x1 = (pow(x1,16971)%25777)
		img1[i1][j1] = x1

img1 = np.array(img1)#.reshape(184,275)
print('\n\nDecrypted Image:\n\n')
print(img1)
#cv.imshow('DeImage', img1)
cv.imwrite('DeImage.png', img1)

end = time.time()
eTime = end - start

print(eTime)
