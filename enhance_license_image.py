import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy

path = './dataset/image.png'
img = cv2.imread(path,0)

threshold = 80

x = img.shape[0]
y = img.shape[1]

img2 = np.zeros([x,y])
for i in range(x):
    for j in range(y):
        if img[i,j] < threshold:
            img2[i,j] = 255
            # img2[i,j] = img[i,j] 
        else:
            img2[i,j]= 0



cv2.imwrite('./dataset/image2.png',img2)

# vertical_hist = np.sum(img2, axis= 0, keepdims=True)/255
# vertical_hist = img.shape[0] - np.sum(img2, axis=0, keepdims= True)/255
# # cv2.imwrite('./dataset/vertical_hist.png', vertical_hist)
# plt.plot(vertical_hist)
# plt.savefig('./dataset/vertical_hist.png')

# Plotting the vertical histogram
vertical_histogram = np.sum(img2, axis=1)
max = np.max(vertical_histogram)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(vertical_histogram[::-1], range(len(vertical_histogram)))
plt.title('Vertical Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Y-coordinate')

# Plotting the horizontal histogram
horizontal_histogram = np.sum(img2, axis=0)
plt.subplot(1, 2, 2)
plt.semilogy(range(len(horizontal_histogram)), horizontal_histogram)
plt.title('Horizontal Histogram')
plt.xlabel('X-coordinate')
plt.ylabel('Pixel Intensity')

plt.tight_layout()
plt.savefig('./dataset/vertical_hist.png')
# plt.show()

# temp = np.zeros.deepcopy(img2)

# temp = np.zeros([x,y])
flag = False
for i in range(len(horizontal_histogram)):
    # if horizontal_histogram[i]!=0:
    if horizontal_histogram[i]>=900:
        if flag == False:
            temp = np.zeros([x,y])
        temp[:,i] = img2[:,i]        
        flag = True
    else:
        if flag == True:
            cv2.imwrite(f'./dataset/{i}.png', temp)
        flag = False
