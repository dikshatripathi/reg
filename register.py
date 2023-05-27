from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:   
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==============================variables===================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_que=StringVar()
        self.var_security_ans=StringVar()
        self.var_pass=StringVar()
        self.var_confirm_pass=StringVar()
      

        #----------------->bg image<------------------------------
        self.bg = ImageTk.PhotoImage(file="C:/Users/diksh/OneDrive/Desktop/FaceRecognitionSystem/images_/p3.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,width=1530,height=720)

       #---------------------------->left image<--------------------
        self.bg1=ImageTk.PhotoImage(file="C:/Users/diksh/OneDrive/Desktop/FaceRecognitionSystem/images_/regbag.png") #add image 
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)


       #----------------->main frame<----------------
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)
        

        #===================label and entry=========================


        #-------------------------------------row1----------------------------------------------------
        
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # First Name
        f_name = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        f_name.place(x=50, y=100)

        self.f_name_entry = ttk.Entry(frame, font=("times new roman", 15),textvariable=self.var_fname)
        self.f_name_entry.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.l_name_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
        self.l_name_entry.place(x=370, y=130, width=250)

        # Contact No
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.contact_entry.place(x=50, y=200, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.email_entry = ttk.Entry(frame, font=("times new roman", 15),textvariable=self.var_email)
        self.email_entry.place(x=370, y=200, width=250)

        # Select Security Questions
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15), state="readonly",textvariable=self.var_security_que)
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First School", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=280, width=250)
        self.combo_security_Q.current(0)

        # Security Answer
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.security_A_entry = ttk.Entry(frame, font=("times new roman", 15),textvariable=self.var_security_ans)
        self.security_A_entry.place(x=370, y=280, width=250)

        # Password
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=320)

        self.pswd_entry = ttk.Entry(frame, font=("times new roman", 15),textvariable=self.var_pass,show="*")
        self.pswd_entry.place(x=50, y=350, width=250)

        # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=320)

        self.confirm_pswd_entry = ttk.Entry(frame, font=("times new roman", 15),textvariable=self.var_confirm_pass,show="*")
        self.confirm_pswd_entry.place(x=370, y=350, width=250)



        #===================checkButton==================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),onvalue=1,offvalue=0,bg="white",variable=self.var_check)
        checkbtn.place(x=50,y=400)
       
       
        # ========================Buttons=====================
        img = Image.open("C:/Users/diksh/OneDrive/Desktop/FaceRecognitionSystem/images_/reg.png")
        img = img.resize((160, 80), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white",bg="white",command=self.register_data1)
        b1.place(x=545, y=440, width=200)
       



        # =====================================function===================================
    def register_data1(self):
        if self.var_fname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_security_que.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confirm_pass.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Dik024sha@", database="registeration")
            my_cursor = conn.cursor()
            query=("select * from users where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Already Exist, Please try another email")
            else:
                my_cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_que.get(),
                    self.var_security_ans.get(),
                    self.var_pass.get()
                    
                ))
            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                    



         
       



















        
















if __name__== "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
        