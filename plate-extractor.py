import os
import cv2


images_path = "dataset/Khanm-Rahmani/selected/"
labels_path = "runs/detect/predict6/labels/"
output_path = "dataset/extracted-plates/"



files = os.listdir(labels_path)
# print(files)
for file in files:
    image_name = file.replace(".txt", "")+".jpg"
    label_name = file
    img = cv2.imread(images_path + image_name)


    lis = open(labels_path+label_name , "r").readlines()
    for l in lis:
        ind = int(l.split()[0])
        # print(ind , names[ind])
        h , w = img.shape[0] , img.shape[1]
        li = l.split()
        xc , yc , nw , nh = float(li[1]) , float(li[2]) , float(li[3]) , float(li[4])
        xc *= w
        yc *= h
        nw *= w
        nh *= h

        top_left = (int(xc - nw/2) , int(yc - nh/2))
        bottom_right = (int(xc + nw/2) , int(yc + nh/2))


        plate = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        plate = cv2.resize(plate, (200, 100))   
        cv2.imwrite(output_path + image_name, plate)
        # cv2.imshow("plate",plate)
        # cv2.waitKey(0)