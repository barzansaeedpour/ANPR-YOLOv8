import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import cv2

names = {0:'0', 1:'1', 2:'2',3:'3', 4:'4', 5:'5',
          6:'6',7:'7', 8:'8', 9:'9',10:'re'}
# lis = open("./runs/detect/predict6/labels/frame-1-0002175.txt" , "r").readlines()
# image_path = './dataset/Khanm-Rahmani/selected_mini/frame-1-0002175.jpg'
lis = open("./generate_plate/generated/temp0.txt" , "r").readlines()
image_path = './generate_plate/generated/temp0.png'
img = cv2.imread(image_path)

for l in lis:
    ind = int(l.split()[0])
    print(ind , names[ind])

    h , w = img.shape[0] , img.shape[1]
    li = l.split()
    xc , yc , nw , nh = float(li[1]) , float(li[2]) , float(li[3]) , float(li[4])
    xc *= w
    yc *= h
    nw *= w
    nh *= h

    top_left = (int(xc - nw/2) , int(yc - nh/2))
    bottom_right = (int(xc + nw/2) , int(yc + nh/2))

    print(top_left , bottom_right)

    org = (top_left[0],int(top_left[1]-(0.01*top_left[1])))
    cv2.putText(img, text = names[ind], 
        org = org, 
        fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
        fontScale = 0.8,
        color = (0 , 255 , 0),
        thickness = 2,)
    # img = cv2.putText(img,"Hello World!!!", top_left)
    img = cv2.rectangle(img , top_left , bottom_right , (0 , 255 , 0) , 2)
    
# cv2.imwrite('./temp.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

