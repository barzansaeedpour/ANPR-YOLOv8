import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import cv2

names = {0:'License'}
lis = open("./runs/detect/predict6/labels/frame-1-0001145.txt" , "r").readlines()
for l in lis:
  ind = int(l.split()[0])
  print(ind , names[ind])

li = lis[0].split()
xc , yc , nw , nh = float(li[1]) , float(li[2]) , float(li[3]) , float(li[4])

image_path = './dataset/Khanm-Rahmani/selected_mini/frame-1-0001145.jpg'
img = cv2.imread(image_path)
h , w = img.shape[0] , img.shape[1]

xc *= w
yc *= h
nw *= w
nh *= h
top_left = (int(xc - nw/2) , int(yc - nh/2))
bottom_right = (int(xc + nw/2) , int(yc + nh/2))

print(top_left , bottom_right)

img = cv2.rectangle(img , top_left , bottom_right , (0 , 255 , 0) , 2)
cv2.imwrite('./temp.png',img)
# cv2.imshow()
# cv2.waitKey(0)

# # Load the image
# image = Image.open(image_path)

# # Create a figure and axis
# fig, ax = plt.subplots(1)

# # Display the image
# ax.imshow(image)

# # Define the label and bounding box coordinates (assuming label and coordinates are provided)
# label = 'License'
# bbox = [0.463675, 0.343213, 0.053155, 0.0241372]

# # Create a rectangle patch
# rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=1, edgecolor='r', facecolor='none')

# # Add the rectangle to the axis
# ax.add_patch(rect)

# # Add the label to the image
# plt.text(bbox[0], bbox[1], label, color='r', fontsize=10, ha='left', va='top')

# # Show the image with the bounding box and label
# plt.show()
