from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x700+0+0")
        self.root.attribute = ('-fullscreen', True)
        self.root.title("Face Recoginition System")

        # ======variables=====Department','Course','Year','Sem','ID','Name','Div','Roll','Gender','DOB','Email','Phone','Address','Teacher','Photo' 
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
                

        img = Image.open(r"project_images\clg1.jpeg")
        img = img.resize((400,130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y =0, width =400, height = 130)

        img1 = Image.open(r"project_images\clg2.jpeg")
        img1 = img1.resize((400,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400,y =0, width =400, height = 130)

        img2 = Image.open(r"project_images\clg3.jpeg")
        img2 = img2.resize((475,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800,y =0, width =475, height = 130)
        # background image

        img3 = Image.open(r"project_images\college.jpeg")
        img3 = img3.resize((1275,570))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b_lbl = Label(self.root, image=self.photoimg3)
        b_lbl.place(x=0,y =130, width =1275, height = 570)

        title_lbl = Label(b_lbl, text = "STUDENT MANAGEMENT SYSTEM ", font =("free style",30,"bold"),bg = "red", fg ="white")
        title_lbl.place(x=0, y=0, width = 1275, height = 40)

        main_frame = Frame(b_lbl, bd =2,bg ="white")
        main_frame.place(x =5, y =50, width = 1250, height = 600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd =4,bg ="white", relief = RIDGE, text = "Student Details", font = ("times new roman",10, "bold"))
        left_frame.place(x =10,y =0, width = 615, height=500)

        img_left = Image.open(r"project_images\baimg1.webp")
        img_left = img_left.resize((605,100))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y =0, width =605, height = 100)

        
        current_course_frame = LabelFrame(left_frame, bd =2,bg ="white", relief = RIDGE, text = "Current Course Information", font = ("times new roman",10, "bold"))
        current_course_frame.place(x =5,y =105, width = 600, height=100)

        #  department 
        dep_label = Label(current_course_frame, text = "Department", font= ("times new roman", 10, "bold"),bg = "white")
        dep_label.grid(row =0, column = 0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font= ("times new roman", 10, "bold"),state="readonly")
        dep_combo["values"]=("Select Department", "CSE", "IT", "EEE","ECE")
        dep_combo.current(0)
        dep_combo.grid(row =0, column =1 ,padx =5, pady =5)

        # course
         
        course_label = Label(current_course_frame, text = "Course", font= ("times new roman", 10, "bold"),bg = "white")
        course_label.grid(row =0, column = 2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font= ("times new roman", 10, "bold"),state="readonly")
        course_combo["values"]=("Select Course", "B.Tech","BE")
        course_combo.current(0)
        course_combo.grid(row =0, column =3 ,padx =5, pady =5)
        # year 
        year_label  = Label(current_course_frame, text = "Year", font =("times new roman", 10, "bold"), bg = "white" )
        year_label.grid(row =1, column=0,padx =10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font =("times new roman", 10, "bold"),state="readonly")
        year_combo["values"]=("Select year", "2015-2019","2016-2020","2017-2021","2018-2022","2019-2023","2020-2024")
        year_combo.current(0)
        year_combo.grid(row =1, column =1 ,padx =5, pady =5)
        # semester
        Semester_label = Label(current_course_frame, text = "Semester", font= ("times new roman", 10, "bold"),bg = "white")
        Semester_label.grid(row =1, column = 2,padx=10,sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem,font= ("times new roman", 10, "bold"),state="readonly")
        Semester_combo["values"]=("Select Semester", "First","Second","Third","Fourth", "Fifth","Sixth","Seventh","Eighth")
        Semester_combo.current(0)
        Semester_combo.grid(row =1, column =3 ,padx =5, pady =5)

# class student information
        class_student_frame = LabelFrame(left_frame, bd =2,bg ="white", relief = RIDGE, text = "Class Student Information", font = ("times new roman",10, "bold"))
        class_student_frame.place(x =5,y =210, width = 600, height=265)

        # Student id
        StudentID_label = Label(class_student_frame, text = "Student ID:", font= ("times new roman", 10, "bold"),bg = "white")
        StudentID_label.grid(row =0, column = 0,padx=10,sticky=W)

        StudentID_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_id,font= ("times new roman", 10, "bold"))
        StudentID_entry.grid(row=0, column =1, padx =10,pady=5, sticky= W)
        # Student Name
        StudentName_label = Label(class_student_frame, text = "Student Name:", font= ("times new roman", 10, "bold"),bg = "white")
        StudentName_label.grid(row =0, column = 2,padx=10,pady=5,sticky=W)

        StudentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_name, width =20,font= ("times new roman", 10, "bold"))
        StudentName_entry.grid(row=0, column =3, padx =10,pady=5, sticky= W)

        # class Division
        class_div_label = Label(class_student_frame, text = "Class Division:", font= ("times new roman", 10, "bold"),bg = "white")
        class_div_label.grid(row =1, column = 0,padx=10,pady=5,sticky=W)

        # class_div_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_div,font= ("times new roman", 10, "bold"))
        # class_div_entry.grid(row=1, column =1, padx =10,pady=5, sticky= W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font= ("times new roman", 10, "bold"),state="readonly",width=18)
        div_combo["values"]=("A", "B","C")
        div_combo.current(0)
        div_combo.grid(row =1, column =1 ,padx =5, pady =5)

        # roll number
        roll_no_label = Label(class_student_frame, text = "Roll No.:", font= ("times new roman", 10, "bold"),bg = "white")
        roll_no_label.grid(row =1, column = 2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_roll,font= ("times new roman", 10, "bold"))
        roll_no_entry.grid(row=1, column =3, padx =10,pady=5, sticky= W)

        # gender
        gender_label = Label(class_student_frame, text = "Gender:", font= ("times new roman", 10, "bold"),bg = "white")
        gender_label.grid(row =2, column = 0,padx=10,pady=5,sticky=W)


        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font= ("times new roman", 10, "bold"),state="readonly" )
        gender_combo["values"]=("Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row =2, column =1 ,padx =5, pady =5)        

        # DOB
        dob_label = Label(class_student_frame, text = "DOB:", font= ("times new roman", 10, "bold"),bg = "white")
        dob_label.grid(row =2, column = 2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_dob,font= ("times new roman", 10, "bold"))
        dob_entry.grid(row=2, column =3, padx =10,pady=5, sticky= W)

        # Email
        email_label = Label(class_student_frame, text = "Email:", font= ("times new roman", 10, "bold"),bg = "white")
        email_label.grid(row =3, column = 0,padx=10,sticky=W)

        email_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_email,font= ("times new roman", 10, "bold"))
        email_entry.grid(row=3, column =1, padx =10,pady=5, sticky= W)

        # Phone Number
        phone_no_label = Label(class_student_frame, text = "Phone No.:", font= ("times new roman", 10, "bold"),bg = "white")
        phone_no_label.grid(row =3, column = 2,padx=10,pady=5,sticky=W)

        phone_no_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_phone,font= ("times new roman", 10, "bold"))
        phone_no_entry.grid(row=3, column =3, padx =10,pady=5, sticky= W)
        # Address
        address_label = Label(class_student_frame, text = "Address:", font= ("times new roman", 10, "bold"),bg = "white")
        address_label.grid(row =4, column = 0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_address,font= ("times new roman", 10, "bold"))
        address_entry.grid(row=4, column =1, padx =10,pady=5, sticky= W)

        #Teacher Name
        teacherName_label = Label(class_student_frame, text = "Teacher Name:", font= ("times new roman", 10, "bold"),bg = "white")
        teacherName_label.grid(row =4, column = 2,padx=10,pady=5,sticky=W)

        teacherName_entry = ttk.Entry(class_student_frame, width =20,textvariable=self.var_teacher,font= ("times new roman", 10, "bold"))
        teacherName_entry.grid(row=4, column =3, padx =10,pady=5, sticky= W)

        # radio Button
        self.var_radio1 =StringVar() 
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text ="take photo sample", value = "Yes")
        radiobtn1.grid(row = 6, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text ="no photo sample", value = "No")
        radiobtn2.grid(row = 6, column=1)

        # button frame
        button_frame = Frame(class_student_frame, bd =4,bg ="white", relief = RIDGE)
        button_frame.place(x =0,y =175, width = 595, height=35)

        save_btn = Button(button_frame,width =20, text = 'Save',command=self.add_data,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        save_btn.grid(row = 0, column =0)

        update_btn = Button(button_frame,width =20, text = 'Update',command=self.update_data,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        update_btn.grid(row = 0, column =1)

        delete_btn = Button(button_frame,width =20,text = 'Delete',command=self.delete_data,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        delete_btn.grid(row = 0, column =2)

        reset_btn = Button(button_frame,width =19, text = 'Reset',command=self.reset,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        reset_btn.grid(row = 0, column =3)
        # button frame 2
        button_frame1 = Frame(class_student_frame, bd =4,bg ="white", relief = RIDGE)
        button_frame1.place(x =0,y =205, width = 595, height=35)
        take_photo_btn = Button(button_frame1,width =41, text = 'Capture Picture',command=self.generate_data_set,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        take_photo_btn.grid(row = 0, column =0)
        update_photo_btn = Button(button_frame1,width =41, text = 'Update Picture',font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        update_photo_btn.grid(row = 0, column =1)


        # right label frame
        right_frame = LabelFrame(main_frame, bd =4,bg ="white", relief = RIDGE, text = "Student Details", font = ("times new roman",10, "bold"))
        right_frame.place(x =625,y =0, width = 615, height=500)
        
        img_right = Image.open(r"project_images\baimg1.webp")
        img_right = img_right.resize((605,100))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y =0, width =605, height = 100)

        # =============  search system  =============

        search_frame = LabelFrame(right_frame, bd =2,bg ="white", relief = RIDGE, text = "Search System", font = ("times new roman",10, "bold"))
        search_frame.place(x =5,y =105, width = 600, height=70)


        search_label = Label(search_frame, text = "Search by:", font= ("times new roman", 10, "bold"),bg = "black", fg = "white")
        search_label.grid(row =0, column = 0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(search_frame,font= ("times new roman", 10, "bold"),state="readonly")
        search_combo["values"]=("Select", "Name","Roll No", "Phone No", "Email Id","Student Id")
        search_combo.current(0)
        search_combo.grid(row =0, column =1 ,padx =0, pady =0)

        search_entry = ttk.Entry(search_frame, width =15,font= ("times new roman", 10, "bold"))
        search_entry.grid(row=0, column =2, padx =2,pady=0, sticky= W)
        
        search_btn = Button(search_frame,width =12, text = 'Search',font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        search_btn.grid(row = 0, column =3,padx =2, pady =0)

        showAll_btn = Button(search_frame,width =12,text = 'Show All',font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        showAll_btn.grid(row = 0, column =4,padx =2, pady =0)

        # table 
        table_frame = Frame(right_frame,bd =2, bg ="white", relief=RIDGE)
        table_frame.place(x =5,y =175, width = 600, height=300)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column =('Department','Course','Year','Sem','ID','Name','Roll','Gender','DOB','Div','Email','Phone','Address','Teacher','Photo' ),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side =BOTTOM, fill=X )
        scroll_y.pack(side =RIGHT, fill=Y )
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        

        self.student_table.heading("Department", text ="Department")
        self.student_table.heading("Course", text ="Course")
        self.student_table.heading("Year", text ="Year")
        self.student_table.heading("Sem", text ="Semester")
        self.student_table.heading("ID", text ="Student ID")
        self.student_table.heading("Name", text ="Name")
        self.student_table.heading("Div", text ="Division")
        self.student_table.heading("Roll", text ="Roll") 
        self.student_table.heading("Gender", text ="Gender")
        self.student_table.heading("DOB", text ="DOB")
        self.student_table.heading("Email", text ="Email")
        self.student_table.heading("Phone", text ="Phone")
        self.student_table.heading("Address", text ="Address")
        self.student_table.heading("Teacher", text ="Teacher")
        self.student_table.heading("Photo", text ="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width =100)
        self.student_table.column("Course", width =100)
        self.student_table.column("Year", width =100)
        self.student_table.column("Sem", width =100)
        self.student_table.column("ID", width =100)
        self.student_table.column("Name", width =100)
        self.student_table.column("Div", width =100)
        self.student_table.column("Roll", width =100)
        self.student_table.column("Gender", width =100)
        self.student_table.column("DOB", width =100)
        self.student_table.column("Email", width =100)
        self.student_table.column("Phone", width =100)
        self.student_table.column("Address", width =100)
        self.student_table.column("Teacher", width =100)
        self.student_table.column("Photo", width =100)


        self.student_table.pack(fill = BOTH, expand =1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # ========  function declaration  =======
    def add_data(self):
        if self.var_dep.get() =="Select Department" or self.var_name.get() =="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent =self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "face_recoginition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                            ))
                self.reset()
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent = self.root)

    #==========  fetch data  =======
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "face_recoginition_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select* from student1")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values=i)
            conn.commit()
        conn.close()
    # ============  get cursot  =====================

    def get_cursor(self,event =""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_div.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # ==============  update function  ==========
    def update_data(self):
        if self.var_dep.get() =="Select Department" or self.var_name.get() =="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent =self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do yo want to update student details", parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "face_recoginition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student1 set Dep =%s, Course =%s, year =%s,sem=%s,name = %s,roll =%s, gender= %s,dob =%s, divi =%s,email=%s,phone =%s, address=%s,teacher =%s, photosample = %s where id =%s ",(
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_id.get()
                                                                                                                                                                                                    ))
                    self.reset()

                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success", "Student details update successfully", parent =self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)


    # ===============  Delelte  ============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Student ID must be required", parent = self.root)
        else:
            try:
                Delete = messagebox.askyesno("Student Delete Page","Do you want to delete student's details")
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "face_recoginition_system")
                    my_cursor = conn.cursor()
                    sql ="delete from student1 where id =%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql,val)
                    self.reset()
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)
   

    # ====================  Reset  =============================
    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Divisio")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
# =======================  Generate data set Take photo sample  ================= 
    def generate_data_set(self):
        if self.var_dep.get() =="Select Department" or self.var_name.get() =="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent =self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "face_recoginition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select* from student1")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id +=1
                my_cursor.execute("update student1 set Dep =%s, Course =%s, year =%s,sem=%s,roll =%s, gender= %s,dob =%s, divi =%s,email=%s,phone =%s, address=%s,teacher =%s, photosample = %s where id =%s ",(
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_id.get() ==id+1
                                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                # ======================  load predefined data on face frontals from opencv  ==================
                face_classifier =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor =1.5 , minimum neighbour =5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id =0
                while True:
                    ret,myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id +=1
                        face =cv2.resize(face_cropped(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1) ==13 or int(img_id) ==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!!!")
            except Exception as es:
                messagebox.showerror("Error","All Fields are Required", parent =self.root)


if __name__ =="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()