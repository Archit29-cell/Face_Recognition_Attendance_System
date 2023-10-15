from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Help:
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

        title_lbl = Label(self.root, text = "ABOUT", font =("free style",30,"bold"),bg = "red", fg ="black")
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
        

        f1 = Frame(second_frame, width=1250,height = 2000,bd =4,bg ='black')
        f1.pack()
        l1 = Label(f1, text="Real-World Applications of Face Recognition",font= ("free style",30,"bold"),bg = 'black',fg ='white',justify=LEFT )
        l1.place(x=0, y=0, width =850)
        l2 = Label(f1, text ='''Face recognition is currently being used to make the world safer, smarter, and more convenient.\n
Some of its most common use cases include finding missing persons, solving retail crime, security\nidentification, identifying accounts on social media, school attendance systems, and recognizing drivers\nin cars.
\nThere are several methods to perform facial recognition depending on the performance and complexity.''',font= ("free style",16),bg ='black',fg ='white',justify='left')
        l2.place(x=-15,y=50,width =1000)
        my_canvas.create_window((0,0),window=second_frame, anchor = "nw")
        l3 = Label(f1, text="Traditional Face Recognition Algorithms",font= ("free style",30,"bold"),bg ='black',fg = 'white',justify=LEFT )
        l3.place(x=-40, y=240, width =850)

        l4 = Label(f1, text =
'''During the 1990s, holistic approaches were used for face recognition. Handcrafted local descriptors 
became popular In the early 1920s, and then the local feature learning approaches were followed in the 
late 2000s. Nowadays, face recognition and face detection algorithms that are widely used and are 
implemented in OpenCV are as follows:''',font= ("free style",16),bg ='black',fg ='white',justify='left')
        l4.place(x=-15,y=290,width =1000)

        img3 = Image.open(r"project_images\facial_representation.png")
        img3 = img3.resize((600,300))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(f1, image=self.photoimg3, justify=CENTER)
        
        f_lbl.place(x=300,y =450, width =600, height = 300)

if __name__ =="__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()