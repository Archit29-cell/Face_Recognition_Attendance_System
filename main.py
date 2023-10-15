from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from student import Student
from train import Train
from face_recoginition1 import Face_Recoginition
from attendance1 import Attendance
from developers import Developer
from about import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x700+0+0")
        self.root.title("Face Recoginition System")
        self.root.configure(bg= "black")

        img = Image.open(r"project_images\fr.jpg")
        img = img.resize((400,130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y =0, width =400, height = 130)

        img1 = Image.open(r"project_images\fr2.jpeg")
        img1 = img1.resize((400,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400,y =0, width =400, height = 130)

        img2 = Image.open(r"project_images\fr3.webp")
        img2 = img2.resize((475,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800,y =0, width =475, height = 130)
        
        img3 = Image.open(r"project_images\baimg2.jpg")
        img3 = img3.resize((1275,570))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b_lbl = Label(self.root, image=self.photoimg3)
        b_lbl.place(x=0,y =130, width =1275, height = 570)

        title_lbl = Label(b_lbl, text = "FACE RECOGINITION ATTENDANCE SYSTEM SOFTWARE", font =("free style",30,"bold"),bg = "black", fg ="blue")
        title_lbl.place(x=0, y=0, width = 1275, height = 40)
        # student button

        img4 = Image.open(r"project_images\student.jpeg")
        img4 = img4.resize((150,150))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(b_lbl, image= self.photoimg4,command =self.student_details, cursor = "hand2" )
        b1.place(x = 100 , y=100, width= 150, height = 150)

        b1_1 = Button(b_lbl, text= "Student  Details",command = self.student_details,cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b1_1.place(x = 100 , y=220, width= 150, height = 50)
        
        # face detect button
        img5 = Image.open(r"project_images\face_detection.jpeg")
        img5 = img5.resize((150,150))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(b_lbl, image= self.photoimg5,command=self.face_data, cursor = "hand2" )
        b2.place(x = 300 , y=100, width= 150, height = 150)

        b2_1 = Button(b_lbl, text= "Face  Detector",command=self.face_data, cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b2_1.place(x = 300 , y=220, width= 150, height = 50)

        # attendance button 
        img6 = Image.open(r"project_images\attendance.jpeg")
        img6 = img6.resize((150,150))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(b_lbl, image= self.photoimg6,command=self.attendance_data, cursor = "hand2" )
        b3.place(x = 500, y=100, width= 150, height = 150)

        b3_1 = Button(b_lbl, text= "Attendance", cursor = "hand2", command= self.attendance_data,font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b3_1.place(x = 500 , y=220, width= 150, height = 50) 

        # help button 
        img7 = Image.open(r"project_images\help.jpeg")
        img7 = img7.resize((150,150))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(b_lbl, image= self.photoimg7, command=self.about,cursor = "hand2" )
        b4.place(x = 700, y=100, width= 150, height = 150)

        b4_1 = Button(b_lbl, text= "About", command=self.about,cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b4_1.place(x = 700 , y=220, width= 150, height = 50)

        # train button 
        img8 = Image.open(r"project_images\train.jpeg")
        img8 = img8.resize((150,150))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(b_lbl, image= self.photoimg8, command=self.train_data,cursor = "hand2" )
        b5.place(x = 900, y=100, width= 150, height = 150)

        b5_1 = Button(b_lbl, text= "Train Data",command= self.train_data, cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b5_1.place(x = 900 , y=220, width= 150, height = 50) 

        # photo button 
        img9 = Image.open(r"project_images\photo.jpeg")
        img9 = img9.resize((150,150))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(b_lbl, image= self.photoimg9,command=self.open_img, cursor = "hand2" )
        b6.place(x = 300, y=300, width= 150, height = 150)

        b6_1 = Button(b_lbl, text= "Photo",command=self.open_img, cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b6_1.place(x = 300 , y=420, width= 150, height = 50) 

        # developer 
        img10 = Image.open(r"project_images\developer.jpeg")
        img10 = img10.resize((150,150))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(b_lbl, image= self.photoimg10, command=self.developer,cursor = "hand2" )
        b7.place(x = 500, y=300, width= 150, height = 150)

        b7_1 = Button(b_lbl, text= "Developer", command=self.developer,cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b7_1.place(x = 500 , y=420, width= 150, height = 50)

        # exit button 
        img11 = Image.open(r"project_images\exit.jpeg")
        img11 = img11.resize((150,150))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(b_lbl, image= self.photoimg11, command=self.exit, cursor = "hand2" )
        b8.place(x = 700, y=300, width= 150, height = 150)

        b8_1 = Button(b_lbl, text= "Exit",command=self.exit, cursor = "hand2",font = ("free style",11,"bold"),bg = "black", fg ="white" )
        b8_1.place(x = 700 , y=420, width= 150, height = 50)

    def open_img(self):
        os.startfile("data")

    # button functioning
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recoginition(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    def about(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def exit(self):
        exit = messagebox.askyesno("Exit", "Do You Want to Exit") 
        if exit >0:
            return root.destroy()
        else:
            return


if __name__ =="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()