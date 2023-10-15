from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x700+0+0")
        self.root.attribute = ('-fullscreen', True)
        self.root.title("Face Recoginition System")

        title_lbl = Label(self.root, text = "TRAIN DATA SET ", font =("free style",30,"bold"),bg = "white", fg ="blue")
        title_lbl.place(x=0, y=0, width = 1275, height = 40)

        
        img_top = Image.open(r"project_images\photo1.jpg")
        img_top = img_top.resize((1275,200))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y =50, width =1275, height = 200)

        b1_1 = Button(self.root, text= "Train Data",command=self.train_classifier,  cursor = "hand2",font = ("free style",20,"bold"),bg = "navyblue", fg ="white" )
        b1_1.place(x = 0 , y=250, width= 1275, height = 50)
        
        img_bottom = Image.open(r"project_images\photo2.webp")
        img_bottom = img_bottom.resize((1275,381))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0,y =300, width =1275, height = 381)
    
    def train_classifier(self):
        data_dir =("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces =[]
        ids =[]
        for image in path:
            img = Image.open(image).convert('L')   #gray scale image 
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)  #numpy give 88% more performance convert array easily

        # ============================= Train the classifier And save==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed!! ")





if __name__ =="__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()