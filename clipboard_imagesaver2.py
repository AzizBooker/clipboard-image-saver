from time import sleep
import tkinter as tk
from PIL import ImageGrab,Image,ImageChops
from datetime import datetime

path=''
images=[]
lastImg
lastIndex=0

def store_single_image(image):
    img=image
    img.save(path+get_current_time()+'.gif')
    print('Image Saved at:'+path)
    
    
def get_current_time():
    time=datetime.now()
    dt_string = time.strftime("%d-%m-%Y %H-%M-%S")
    return dt_string
def increment_index():
   global lastIndex
   lastIndex=lastIndex+1 

def setup():
    global images
    img=ImageGrab.grabclipboard()
    if img is not None:
        store_single_image(img)
        imgClass=Images(img,datetime.now(),0)
        lastImg=imgClass
        increment_index()
        images.append(imgClass)
         




class Images:
    global lastIndex
    index=None
    img=None
    time=None
    def __init__(self,img,time,index):
        self.index=index
        self.img=img
        self.time=time
    def check_index(self,index):
        if self.index > index:
            return True
        else:
            return False

    


def main():
    global lastImg
    global images
    setup()
    while True:
        img=ImageGrab.grabclipboard()
       if img is not None:
           img
           
            
if __name__=="__main__":
    main()