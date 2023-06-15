import os
import cv2
import time
import uuid

IMAGE_PATH='Collectimg'

labels=['Thanks','Hello','IloveYou','Yes','No','Please','Ask','Help','Home','Wait','Victory','Thumbsup','Thumbsdown','Okay','Namaste','Callme','Salute','Dance','Looser','Danger']

number_of_images=100

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(30)
    for imgnum in range(number_of_images):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(1)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()