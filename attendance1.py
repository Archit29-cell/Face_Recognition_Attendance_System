from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import os 
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1275x690+0+0")
        self.root.attribute = ('-fullscreen', True)
        self.root.title("Face Recoginition System")

        self.var_atten_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_attendance = StringVar()


        title_lbl = Label(self.root, text = "Attendance Sheet ", font =("free style",30,"bold"),bg = "white", fg ="red")
        title_lbl.place(x=0, y=0, width = 1275, height = 50)

        main_frame = Frame(self.root, bd =8, relief='solid' ,bg = 'white')
        main_frame.place(x = 1, y=51, width = 1275,height=639 )

        # left_frame = Frame(main_frame, text = "Student Attendance Details",font = ("times new roman",10, "bold"),bd =8, relief=RIDGE ,bg = 'white')
        self.left_frame = LabelFrame(main_frame, bd =4,bg ="white", relief = SOLID, text = "Student Attendance Details", font = ("times new roman",10, "bold"))
        self.left_frame.place(x = 0, y=0, width = 621,height=620 )

        img_left = Image.open(r"project_images\Attendace.png")
        img_left = img_left.resize((618,100))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.left_frame, image=self.photoimg_left, bd=2, relief='solid')
        f_lbl.place(x=0,y =0, width =615, height = 100)
        left_inside_frame = Frame(self.left_frame,bd=2, relief='solid',bg = 'white')
        left_inside_frame.place(x = 0, y=101, width = 615,height=80 )

        
        name_label = Label(left_inside_frame, text = " Name:", font= ("times new roman", 10, "bold"),bg = "white")
        name_label.grid(row =0, column = 2,padx=10,pady=5,sticky=W)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_name,width =20,font= ("times new roman", 10, "bold"))
        name_entry.grid(row=0, column =3, padx =10,pady=5, sticky= W)

        # roll no
        roll_no_label = Label(left_inside_frame, text = "Roll No.:", font= ("times new roman", 10, "bold"),bg = "white")
        roll_no_label.grid(row =0, column = 0,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(left_inside_frame,textvariable=self.var_roll, width =20,font= ("times new roman", 10, "bold"))
        roll_no_entry.grid(row=0, column =1, padx =10,pady=5, sticky= W)

       

        search_button = Button(left_inside_frame, text="Search", command=self.searchStudent, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        search_button.grid(row=1, column=2,columnspan=3, padx=10, pady=5)

        button_frame = Frame(self.left_frame, bd =1,bg ="white", relief = SOLID)
        button_frame.place(x =0,y =182, width = 615, height=29)

        button1_frame = Frame(self.left_frame, bd =2,bg ="white", relief = SOLID)
        button1_frame.place(x =0,y =212, width = 615, height=326+68)

        import_btn = Button(button_frame,width =20,height=1, text = 'Import CSV',command=self.importCSV,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        import_btn.grid(row = 0, column =0)

        export_btn = Button(button_frame,width =20,height=1, text = 'Export CSV',command=self.exportCSV,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        export_btn.grid(row = 0, column =1)

        update_btn = Button(button_frame,width =21,height=1,text = 'Update',command=self.update,font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        update_btn.grid(row = 0, column =2)

        reset_btn = Button(button_frame,width =21,command=self.reset,height=1, text = 'Reset',font= ("times new roman", 10, "bold"),bg = "blue", fg = "white")
        reset_btn.grid(row = 0, column =3)

        right_frame = LabelFrame(main_frame, bd =4,bg ="white", relief = SOLID, text = "Attendance Details", font = ("times new roman",10, "bold"))
        right_frame.place(x =622,y =0, width = 637, height=620)

        table_frame = Frame(right_frame,bd=2, relief='solid',bg = 'white')
        table_frame.place(x = 0, y=0, width = 630,height=450 )

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable =ttk.Treeview(table_frame,columns=('id','roll','name','dept','time','date','attendance'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id', text='Attendance Id')
        self.AttendanceReportTable.heading('name', text='Name')
        self.AttendanceReportTable.heading('roll', text='Roll No.')
        self.AttendanceReportTable.heading('dept', text='Department')
        self.AttendanceReportTable.heading('time', text='Time')
        self.AttendanceReportTable.heading('date', text='Date')
        self.AttendanceReportTable.heading('attendance', text='Attendance')

        self.AttendanceReportTable.column('id',width=100)
        self.AttendanceReportTable.column('name',width=100)
        self.AttendanceReportTable.column('roll',width=100)
        self.AttendanceReportTable.column('dept',width=100)
        self.AttendanceReportTable.column('time',width=100)
        self.AttendanceReportTable.column('date',width=100)
        self.AttendanceReportTable.column('attendance',width=100)

        self.AttendanceReportTable['show'] ='headings'
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.getCursor)
        self.loadInitialCSV()
        

        self.search_results_table = ttk.Treeview(button1_frame, columns=('id', 'roll', 'name', 'dept', 'date', 'time', 'attendance'))
        self.search_results_table.place(x=0, y=0,width =610, height=1000)
        x_scrollbar = ttk.Scrollbar(button1_frame, orient=HORIZONTAL)
        x_scrollbar.pack(side=BOTTOM, fill=X)
        x_scrollbar.config(command=self.search_results_table.xview)

        # Create vertical scrollbar
        y_scrollbar = ttk.Scrollbar(button1_frame, orient=VERTICAL,command= self.search_results_table.yview)
        y_scrollbar.pack(side= RIGHT, fill=Y)
        # y_scrollbar.config(command=self.search_results_table.yview)

        # Configure the table to use the scrollbars
        self.search_results_table.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
        # Create a new Treeview widget to display search results

        self.search_results_table.heading('id', text='Attendance Id')
        self.search_results_table.column('id', width=90)

        self.search_results_table.heading('name', text='Name')
        self.search_results_table.column('name', width =100)
        self.search_results_table.heading('roll', text='Roll No.')
        self.search_results_table.column('roll', width =100)
        self.search_results_table.heading('dept', text='Dept')
        self.search_results_table.column('dept', width =80)
        self.search_results_table.heading('date', text='Date')
        self.search_results_table.column('date', width =80)
        self.search_results_table.heading('time', text='Time')
        self.search_results_table.column('time', width =80)
        self.search_results_table.heading('attendance', text='Attendance')
        self.search_results_table.column('attendance', width =100)
        self.search_results_table['show'] ='headings'

    def loadInitialCSV(self):
        initial_csv_file = "attendance.csv"  # File in the same directory as the source code
        try:
            with open(initial_csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                data = [row for row in reader]
                self.fetch_data(data)
            
        except FileNotFoundError:
            # Handle the case when the initial CSV file is not found
            print("Initial CSV file not found.")

    def update(self):
        file_path = "attendance.csv"  # Replace with the path to your "attendance.csv" file
        with open(file_path, 'r') as myfile:
            csvread = csv.reader(myfile)
            mydata.clear()
            for i in csvread:
                mydata.append(i)
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for data in mydata:
                self.AttendanceReportTable.insert("", END, values=data)

    def saveToCSV(self, file_path, data):
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)
        except Exception as e:
            # Handle the exception (e.g., file not found, permission denied)
            print(f"Failed to save data to {file_path}: {str(e)}")

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END, values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)
    
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found", parent=self.root)
                return False

            # Ask the user for the destination file using a file dialog
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root,
            )

            if fln:
                # Save the data to the selected CSV file
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export", "Your Data has been exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", "An error occurred while exporting data", parent=self.root)

    def getCursor(self,event =""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_name.set(rows[2])
        self.var_roll.set(rows[1])
        self.var_dept.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_attendance.set(rows[6])

    def searchStudent(self):
        roll_to_search = self.var_roll.get()
        name_to_search = self.var_name.get()

        if not roll_to_search and not name_to_search :
            messagebox.showerror("Error", "Please enter a Roll Number or Name to search.")
            return
        self.search_results_table.delete(*self.search_results_table.get_children())
        
        found = False
        for row in mydata:
            if (roll_to_search and row[1] == roll_to_search) or (name_to_search and row[2].lower() == name_to_search.lower()):
                found = True
                self.search_results_table.insert("", END, values=row)

        if not found:
            messagebox.showinfo("Not Found", "No record found for the provided Roll Number.")
        else:
            # Store a reference to the search results table so that it can be cleared later
            self.self.search_results_table = self.search_results_table
    
    def reset(self):
        self.var_atten_id.set()
        self.var_name.set()
        self.var_roll.set()
        self.var_dept.set()
        self.var_date.set()
        self.var_time.set()
        self.var_attendance.set()
    
    
if __name__ =="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()