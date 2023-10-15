from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os   
import numpy as np
from time import strftime
from datetime import datetime
import csv

class Face_Recoginition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x700+0+0")
        # self.root.attribute = ('-fullscreen', True)
        self.root.title("Face Recoginition System")
        self.root.iconbitmap(r"C:\Users\Archit\Downloads\Screenshot-2023-10-21-222650.ico")
        title_lbl = Label(self.root, text = "FACE RECOGINITION ", font =("free style",30,"bold"),bg = "black", fg ="red")
        title_lbl.place(x=0, y=0, width = 1280, height = 40)

        img_top = Image.open(r"project_images\facial_recognition-1.png")
        img_top = img_top.resize((600,655))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y =41, width =600, height = 655)

        img_bottom = Image.open(r"project_images\face1.webp")
        img_bottom = img_bottom.resize((680,655))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f2_lbl = Label(self.root, image=self.photoimg_bottom)
        f2_lbl.place(x=600,y =41, width =680, height = 655)

        b1_1 = Button(f2_lbl, text= "Face Recoginition",command=self.face_recog,  cursor = "hand2",font = ("free style",10,"bold"),bg = "darkblue", fg ="white" )
        b1_1.place(x = 242 , y=570, width= 180, height = 40)

    def mark_attendance(self, i, r, n, d,dt,d1):
            # Get the current date
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dt = now.strftime("%H:%M:%S")
            # Check if the CSV file exists
            if not os.path.exists("attendance.csv"):
                # If it doesn't exist, create it with a header row
                with open("attendance.csv", "w", newline="\n") as f:
                    header = ["ID", "Roll", "Name", "Department", "Date", "Status"]
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(header)

            # Check if an entry for the same ID and date already exists
            with open("attendance.csv", "r", newline="\n") as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    if row and row[0] == i and row[4] == d1:
                        # An entry for the same ID and date already exists, so don't add a new one
                        return

            # Now, add a new attendance record
            with open("attendance.csv", "a", newline="\n") as f:
                dtString = now.strftime("%H:%M:%S")
                status = "Present"
                csv_writer = csv.writer(f)
                csv_writer.writerow([i, r, n, d, d1,dt, status])
     # =============================  face recoginition =======================================
    def face_recog(self):
        def draw_boundary(img,classifier, scaleFactor, minNeighbors,color, text,clf):
            gray_image =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features =classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w ,y+h), (0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+h])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "face_recoginition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("select roll from student1 where id ="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select name from student1 where id ="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)                

                my_cursor.execute("select Dep from student1 where id ="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select id from student1 where id ="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt = now.strftime("%H:%M:%S")
                if confidence>77:
                    cv2.putText(img, f"ID:{i}", (x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll:{r}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}", (x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Department:{d}", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d,d1, dt )
                else:
                    cv2.rectangle(img,(x,y),(x+w ,y+h), (0,0,255),3)
                    cv2.putText(img, "Unknown Face", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord =[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade =  cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img= video_cap.read()
            img = recognize(img, clf,faceCascade)
            cv2.imshow("Welcome to Face Recoginition",img)
            
            if cv2.waitKey(1) ==13:
                break
        video_cap.release() 
        cv2.destroyAllWindows()
                    
                    
if __name__ =="__main__":
    root = Tk()
    obj = Face_Recoginition(root)
    root.mainloop()