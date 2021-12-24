from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage   

class QRGenerator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,False)

        title=Label(self.root,text=" QR Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        #frame 1

        #variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_desig=StringVar()

        emp_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_frame.place(x=50,y=100,width=500,height=380)

        emptitle=Label(emp_frame,text=" Employee Details",font=("goudy old style",30),bg='#043246',fg='white',anchor='c').place(x=0,y=0,relwidth=1)

        labelEmp=Label(emp_frame,text=" Employee Id",font=("times new roman",15),bg='white',anchor='c').place(x=20,y=60)
        labelName=Label(emp_frame,text=" Name",font=("times new roman",15),bg='white',anchor='c').place(x=20,y=100)
        labelDepart=Label(emp_frame,text=" Department",font=("times new roman",15),bg='white',anchor='c').place(x=20,y=140)
        labelDesig=Label(emp_frame,text=" Designation",font=("times new roman",15),bg='white',anchor='c').place(x=20,y=180)

        txtEmp=Entry(emp_frame,font=("times new roman",15),bg='lightyellow',textvariable=self.var_id).place(x=200,y=60)
        txtlName=Entry(emp_frame,font=("times new roman",15),bg='lightyellow',textvariable=self.var_name).place(x=200,y=100)
        txtlDepart=Entry(emp_frame,font=("times new roman",15),bg='lightyellow',textvariable=self.var_department).place(x=200,y=140)
        txtDesig=Entry(emp_frame,font=("times new roman",15),bg='lightyellow',textvariable=self.var_desig).place(x=200,y=180)

        btn_gen=Button(emp_frame,text="QR generate",command=self.qrgenerate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=50,y=250,width=180,height=30)
        btn_clear=Button(emp_frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=282,y=250,width=120,height=30)

        self.msg=""
        self.msg_label=Label(emp_frame,text=self.msg,font=("goudy old style",20),bg='white',fg='green')
        self.msg_label.place(x=0,y=320,relwidth=1)

        #frame 2
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=100,width=250,height=380)

        self.qrtitle=Label(qr_frame,text=" QR Code",font=("goudy old style",30),bg='#043246',fg='white',anchor='c').place(x=0,y=0,relwidth=1)
        self.qrcode=Label(qr_frame,text="QR Code\nNot Available",font=("times new roman",15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qrcode.place(x=35,y=100,height=180,width=180)

        #function

    def clear(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_desig.set('')
        self.msg=""
        self.msg_label.config(text=self.msg)
        self.qrcode.config(image='')

    def qrgenerate(self):
        if self.var_desig.get()=='' or self.var_id.get()=='' or self.var_name.get()=='' or self.var_department.get()=='':
            self.msg="All fields are required!!"
            self.msg_label.config(text=self.msg,fg='red')
        else:

            qr_data=(f"Employee Id :{self.var_id.get()}\nEmployee Name: {self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_desig.get()}")
            qr_code=qrcode.make(qr_data)

            qr_code=resizeimage.resize_cover(qr_code,[180,180])

            self.im=ImageTk.PhotoImage(qr_code)
            self.qrcode.config(image=self.im)

            self.msg="QR Code generated successfully"
            self.msg_label.config(text=self.msg,fg='green')

        








root=Tk()
obj=QRGenerator(root)

root.mainloop()