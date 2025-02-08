from tkinter import *
from mysql.connector import connect, Error
class Login_window:
    def loginwindow(self,Mypanel):
        print("Entered LOGIN PAGE")
        Mypanel.title("LOGIN")
        Mypanel.state("zoomed")
        Mypanel.configure(background="#001F3F")
        Mypanel.grab_set()

        try:
            global connection
            connection = connect(
                host="localhost",
                user="root",
                password="Kishore@2000",
                database="atm")
            print("Login page DATABASE CONNECTED")
        except Error as e:
            print("Error while connecting to MySQL", e)
            from tkinter import messagebox
            messagebox.showinfo("Error","Unable to connect to login page database")

        headinglbl=Label(Mypanel,text="LOGIN PAGE",fg="#D3D3D3",bg="#001F3F",font=("Segoe UI",20))
        headinglbl.pack(pady=10)

        frame=Frame(Mypanel,width=500,height=250,bg="#FFD700",relief="solid",borderwidth=1)
        frame.pack(pady=20)

        inFramelbl=Label(frame,text="Enter your Card details",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        inFramelbl.place(x=100,y=10)

        acct_lbl=Label(frame,text="Card Number",fg="Black",bg="#FFD700",font=("Segoe UI",15))
        acct_lbl.place(x=50,y=75)
        def allow_only_num(char):
            return char.isdigit() or char == ""

        vcmd = Mypanel.register(allow_only_num)
        acct_entry=Entry(frame,width=20,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=(vcmd,'%P'))
        acct_entry.place(x=250,y=80)

        def allow_only_dig(char,current_text):
            return char.isdigit() and len(current_text) <= 4
        pin = Mypanel.register(allow_only_dig)

        pin_lbl=Label(frame,text="Pin",fg="Black",bg="#FFD700",font=("Segoe UI",15))
        pin_lbl.place(x=140,y=125)
        pin_entry=Entry(frame,width=20,bg="white",fg="black",font=("Segoe UI",15),show="*",validate="key",validatecommand=(pin,"%S","%P"))
        pin_entry.place(x=250,y=130)

        def verify():
            from tkinter import messagebox
            cursor=connection.cursor()
            cardquery="SELECT count(*) FROM  ATMHOLDERS WHERE CARD_NUMBER = %s"
            cursor.execute(cardquery,(acct_entry.get(),))
            counterbuf=cursor.fetchone()
            if counterbuf[0]==1:
                pinquery="SELECT PIN FROM ATMHOLDERS WHERE CARD_NUMBER = %s"
                cursor.execute(pinquery,(acct_entry.get(),))
                bufpin=cursor.fetchone()
                if bufpin[0] == pin_entry.get():
                    crd=acct_entry.get()
                    acct_entry.delete(0, END)
                    pin_entry.delete(0, END)
                    from Atmservicespage import Class
                    mypanel = Toplevel()
                    Class.D1_servicespage(mypanel,crd)
                    cursor.close()
                    connection.close()
                    print("login page DataBase Connection Closed")
                else:
                    messagebox.showinfo("Error","Wrong Pin")
                    pin_entry.delete(0, END)
            else:
                messagebox.showinfo("Error","Card not found")
                acct_entry.delete(0, END)
                pin_entry.delete(0, END)

        loginbtn=Button(frame,text="Login",fg="Black",bg="grey",font=("Segoe UI",14),command=verify)
        loginbtn.place(x=250,y=180)



Class=Login_window()


