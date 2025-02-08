from tkinter import *
from mysql.connector import connect,Error
class AdminLoginpage:
    def admin(self,adminloginwindow):
        print("entered admin login page")
        adminloginwindow.title("ADMIN LOGIN PAGE")
        adminloginwindow.configure(background="#001F3F")
        adminloginwindow.state("zoomed")
        adminloginwindow.grab_set()


        headinglbl=Label(adminloginwindow,text="ADMIN LOGIN PAGE",fg="#D3D3D3",bg="#001F3F",font=("Segoe UI",20))
        headinglbl.pack()

        frame=Frame(adminloginwindow,width=600,height=250,bg="#FFD700",relief="solid",borderwidth=1)
        frame.pack(pady=50)

        admin_idlbl=Label(frame,text="Admin-id",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        admin_idlbl.place(x=30,y=50)
        adminusername=Entry(frame,width=30,font=("Segoe UI",15))
        adminusername.place(x=180,y=60)

        inFramelbl=Label(frame,text="pin",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        inFramelbl.place(x=95,y=120)
        adminpassword=Entry(frame,width=30,font=("Segoe UI",15),show="*")
        adminpassword.place(x=180,y=130)

        adminloginbtn=Button(frame,text="LOGIN",fg="Black",bg="grey",font=("Segoe UI",15))
        adminloginbtn.place(x=280,y=180)

        def verify():
            try:
                global connection
                connection = connect(
                    host="localhost",
                    user="root",
                    password="Kishore@2000",
                    database="atm")
                print("DATABASE CONNECTED")
            except Error as e:
                print("Error while connecting to MySQL", e)
                from tkinter import messagebox
                messagebox.showinfo("Error", "Unable to connect")

            from tkinter import messagebox
            cursor = connection.cursor()
            admin_id_query = "SELECT count(*) FROM  Adminstrator WHERE Admin_id = %s"
            cursor.execute(admin_id_query, (adminusername.get(),))
            counterbuf = cursor.fetchone()
            if counterbuf[0] == 1:
                pinquery = "SELECT Pin FROM Adminstrator WHERE Admin_id = %s"
                cursor.execute(pinquery, (adminusername.get(),))
                bufpin = cursor.fetchone()
                if bufpin[0] == adminpassword.get():
                    adminusername.delete(0, END)
                    adminpassword.delete(0, END)
                    print("left admin login page")
                    cursor.close()
                    connection.close()
                    print("DataBase Connection Closed")
                    from Administrator import Class
                    subwindow = Toplevel()
                    Class.Admin(subwindow)

                else:
                    messagebox.showinfo("Error", "Wrong Pin")
                    adminpassword.delete(0, END)
            else:
                messagebox.showinfo("Error", "Admin_id  not found")
                adminusername.delete(0, END)
                adminpassword.delete(0, END)
        adminloginbtn = Button(frame, text="LOGIN", fg="Black", bg="grey", font=("Segoe UI", 15),command=verify)
        adminloginbtn.place(x=280, y=180)

Class=AdminLoginpage()

