from tkinter import *
class C_HOMEPAGE:
    def D1_Homepage_Creation(self):
        print("entered homepage")
        mainwindow=Tk()
        mainwindow.state("zoomed")
        mainwindow.title("HOME")
        mainwindow.configure(background="#001F3F")
        headinglbl=Label(mainwindow,text="ATM SERVICE",fg="#D3D3D3",bg="#001F3F",font=("Segoe UI",20))
        headinglbl.pack()

        frame=Frame(mainwindow,width=500,height=200,bg="#FFD700",relief="solid",borderwidth=1)
        frame.pack(pady=50)

        inFramelbl=Label(frame,text="Select a services",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        inFramelbl.place(x=148,y=10)

        def login_page():
            from Login_window import Class
            Mypanel = Toplevel()
            Class.loginwindow(Mypanel)

        bankingbtn=Button(frame,text="Banking",fg="Black",bg="grey",font=("Segoe UI",20),command=login_page)
        bankingbtn.place(x=70,y=80)

        def admin_login():
            from adminlog import Class
            adminloginwindow = Toplevel()
            Class.admin(adminloginwindow)

        signupbtn=Button(frame,text="Admin",fg="Black",bg="grey",font=("Segoe UI",20),command=admin_login)
        signupbtn.place(x=300,y=80)

        def clsbtn():
            mainwindow.destroy()
            print("Left Homepage")
        Closingbtn=Button(mainwindow,text="Close",fg="Black",bg="grey",font=("Segoe UI",15),command=clsbtn)
        Closingbtn.place(x=740,y=320)

        mainwindow.mainloop()

Class= C_HOMEPAGE()
Class.D1_Homepage_Creation()