import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import cv2
import os

# names = {0:'0', 1:'1', 2:'2',3:'3', 4:'4', 5:'5',
#           6:'6',7:'7', 8:'8', 9:'9',10:'re'}
# names= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'be', 'dal', 'ein', 'gaf', 'ghaf', 'h', 'he', 'jim', 'lam', 'mim', 'noon', 'sad', 'sin', 'ta', 'te', 'waw', 'ye']
names= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'be', 'dal', 'ein', 'ghaf', 'h', 'he', 'jim', 'lam', 'mim', 'noon', 'sad', 'sin', 'ta', 'te', 'waw', 'ye']

# lis = open("./runs/detect/predict6/labels/frame-1-0002175.txt" , "r").readlines()
# image_path = './dataset/Khanm-Rahmani/selected_mini/frame-1-0002175.jpg'

path = './dataset/temp/train/'
# path = './dataset/temp/valid/'
# path = './dataset/temp/test/'
output_path = './dataset/char-all-check/'
for file in os.listdir(f'{path}images/'):
    
    image_path = f'{path}images/{file}'
    label_path = f'{path}labels/{file.replace(".jpg",".txt")}'

    lis = open(label_path , "r").readlines()
    img = cv2.imread(image_path)
    img = cv2.resize(img, (600, 200)) 

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

        org = (top_left[0],int(top_left[1]-(0.1*top_left[1])))
        cv2.putText(img, text = names[ind], 
            org = org, 
            fontFace = cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale = 1.0,
            color = (0 , 255 , 0),
            thickness = 2,)
        # img = cv2.putText(img,"Hello World!!!", top_left)
        img = cv2.rectangle(img , top_left , bottom_right , (0 , 255 , 0) , 2)
        
    cv2.imwrite(f'{output_path}{file}',img)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

