from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x700+0+0")
        self.root.attribute = ('-fullscreen', True)
        self.root.title("Face Recoginition System")
        self.root.configure(bg= "black")

        img = Image.open(r"project_images\developer.jpeg")
        img = img.resize((400,130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y =0, width =400, height = 130)

        img1 = Image.open(r"project_images\developer2.jpg")
        img1 = img1.resize((400,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400,y =0, width =400, height = 130)

        img2 = Image.open(r"project_images\images.jpeg")
        img2 = img2.resize((475,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800,y =0, width =475, height = 130)

        title_lbl = Label(self.root, text = "ABOUT DEVELOPERS ", font =("free style",30,"bold"),bg = "red", fg ="black")
        title_lbl.place(x=0, y=130, width = 1275, height = 40)


        developer = Frame(self.root, bd =4,bg ="black", relief = RIDGE)
        developer.place(x=0, y = 171, width = 1275, height = 529)

        my_canvas = Canvas(developer)
        my_canvas.pack(side=LEFT, fill = BOTH, expand= 1)

        my_scrollbar = Scrollbar(developer,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill= Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)

        # my_img = Image.open(r"project_images\my_img.jpg")
        # my_img = my_img.resize((180,75))
        # self.photo1 = ImageTk.PhotoImage(my_img)
        
        # lbl = Label(second_frame,  width=1275, height=120,bg = 'black')
        # lbl.pack()
        # lbl1 = Label(lbl, image = self.photo1, width=180, height=75)
        # lbl1.grid(row =0, column=0)
        # lbl2 = Label(lbl, text ="my name is Archit Khandelwal", font=("times new roman",10,"bold"),bg = 'black', fg= 'white', height=5)
        # lbl2.grid(row=0, column = 1)

        l1 = Frame(second_frame, width=1250,height = 200,bd =4, relief="solid",bg ='white')
        l1.pack()
        my_img = Image.open(r"project_images\my_img.jpg")
        my_img = my_img.resize((180,160))
        self.photo1 = ImageTk.PhotoImage(my_img)

        lbl1 = Label(l1, image = self.photo1, width=180, height=160,bd =2, relief=SOLID)
        lbl1.place(x =0, y=0)
        lbl2 = Label(l1, text = 'ARCHIT KHANDELWAL',  font =("free style",10,"bold"),bg ='white',fg ='black')
        lbl2.place(x =2, y=172, width=180, height=20)
        about1 =Label(l1, text ='Name : Archit Khandelwal\nEnrollment No. : 01713203120', font=("free style",15,"bold"),bg ='white',fg ='black',justify=LEFT)
        about1.place(x =185, y=2)
        about11 = Label(l1, text= 'ROLE : ', font=("free style",16,"bold"),bg ='white',fg ='black',justify=LEFT)
        about11.place(x = 185, y = 50)
        about12 = Label(l1,text =
'''I have developed a modal employing sophisticated algorithms, including Haarcascade in OpenCV for 
object detection and LBPH in OpenCV for facial recognition. This advanced approach facilitates rob-
ust and accurate identification and classification, enhancing the overall performance and capabili-
ties of the system.''', font=("free style",15),bg ='white',fg ='black',justify=LEFT)
        about12.place(x = 230+30,y =50, width = 900) 
        l2 = Frame(second_frame, width=1250,height = 200,bd =4, relief="solid",bg ='black')
        l2.pack()
        my_img1 = Image.open(r"project_images\image.jpg")
        my_img1 = my_img1.resize((180,160))
        self.photo11 = ImageTk.PhotoImage(my_img1)

        lbl11 = Label(l2, image = self.photo11, width=180, height=160)
        lbl11.place(x =1000+50, y=0)
        lbl21 = Label(l2, text = 'AAYUSH SHARMA',  font =("free style",10,"bold"),bg ='black',fg ='white')
        lbl21.place(x =1000+50, y=171, width=180, height=20)
        about2 =Label(l2, text ='Name : Aayush Sharma\nEnrollment No. : 00213203120', font=("free style",15,"bold"),fg ='white',bg ='black',justify=LEFT)
        about2.place(x =0, y=2)
        about11 = Label(l2, text= 'ROLE : ', font=("free style",16,"bold"),fg ='white',bg ='black',justify=LEFT)
        about11.place(x = 0, y = 50)
        about12 = Label(l2,text =
'''I proficiently managed the project's database, seamlessly integrating it with MySQL. This meticulous
oversight ensured efficient data handling, optimizing accessibility and reliability. Synchronizing our
database with MySQL maintained a robust foundation, enhancing overall performance and reliability.''', font=("free style",15),fg ='white',bg ='black',justify=LEFT)
        about12.place(x =50+30,y =50, width = 900) 
        

        l3 = Frame(second_frame, width=1250,height = 200,bd =4, relief="solid",bg ='white')
        l3.pack()
        my_img2 = Image.open(r"project_images\dheeraj (2).png")
        my_img2 = my_img2.resize((180,160))
        self.photo12 = ImageTk.PhotoImage(my_img2)

        lbl11 = Label(l3, image = self.photo12, width=180, height=160,bd =2, relief=SOLID)
        lbl11.place(x =0, y=0)
        lbl21 = Label(l3, text = 'DHEERAJ SHARMA',  font =("free style",10,"bold"),bg ='white',fg ='black')
        lbl21.place(x =2, y=171, width=180, height=20)
        about2 =Label(l3, text ='Name : Dheeraj Sharma\nEnrollment No. : 03013203120', font=("free style",15,"bold"),bg ='white',fg ='black',justify=LEFT)
        about2.place(x =185, y=2)
        about11 = Label(l3, text= 'ROLE : ', font=("free style",16,"bold"),bg ='white',fg ='black',justify=LEFT)
        about11.place(x = 185, y = 50)
        about12 = Label(l3,text =
'''I have adeptly curated and structured the student data extracted from our attendance system 
within an Excel spreadsheet. This meticulous management ensures accurate records and streamline
access to essential information for effective tracking and analysis''', font=("free style",15),bg ='white',fg ='black',justify=LEFT)
        about12.place(x = 230+30,y =50, width = 900)
        l3 = Frame(second_frame, width=1250,height = 200,bd =4, relief="solid",bg ='black')
        l3.pack()
        my_img3 = Image.open(r"project_images\ARYAN.jpg")
        my_img3 = my_img3.resize((180,160))
        self.photo31 = ImageTk.PhotoImage(my_img3)

        lbl13 = Label(l3, image = self.photo31, width=180, height=160)
        lbl13.place(x =1050, y=0)
        lbl23 = Label(l3, text = 'ARYAN CHOUDHARY',  font =("free style",10,"bold"),bg ='black',fg ='white')
        lbl23.place(x =1052, y=171, width=180, height=20)
        about2 =Label(l3, text ='Name : Aryan Choudhary\nEnrollment No. : 01813203120', font=("free style",15,"bold"),fg ='white',bg ='black',justify=LEFT)
        about2.place(x =0, y=2)
        about11 = Label(l3, text= 'ROLLE : ', font=("free style",16,"bold"),fg ='white',bg ='black',justify=LEFT)
        about11.place(x = 0, y = 50)
        about12 = Label(l3,text =
'''I have developed an interactive user interface with Tkinter for a cutting-edge facial recognition 
system. This state-of-the-art application seamlessly integrates face recognition technology, providi-
ng users with a powerful and user-friendly tool for identity verification and access control''', font=("free style",15),fg ='white',bg ='black',justify=LEFT)
        about12.place(x = 80,y =50, width = 900)
        my_canvas.create_window((0,0),window=second_frame, anchor = "nw")

        
if __name__ =="__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()