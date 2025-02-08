from tkinter import *
from mysql.connector import connect,Error
class Administrator:
    def Admin(self,subwindow):
        print("Entered ADMIN PAGE")
        subwindow.title("ADMINSTRATOR")
        subwindow.configure(background="#001F3F")
        subwindow.state("zoomed")
        subwindow.grab_set()
        headinglbl=Label(subwindow,text="ADMINISTRATOR",fg="#D3D3D3",bg="#001F3F",font=("Segoe UI",20))
        headinglbl.pack()

        frame=Frame(subwindow,width=700,height=480,bg="#FFD700",relief="solid",borderwidth=1)
        frame.pack(pady=50)

        inFramelbl=Label(frame,text="Create ATM Account for Customer",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        inFramelbl.place(x=130,y=10)

        card_numlbl=Label(frame,text="Card Number",fg="Black",bg="#FFD700",font=("Segoe UI",20,))
        card_numlbl.place(x=50,y=100)
        def allowonlynum(char,action,current_text):
            if action == '1':
                if not char.isdigit():
                    return False
            if len(current_text) >= 13:
                return False
            return True
        validate_cmd = subwindow.register(allowonlynum)
        card_nument=Entry(frame,width=30,bg="white",fg="black",font=("Segoe UI",15,),validate="key",validatecommand=(validate_cmd,"%S", "%d", "%P"))
        card_nument.place(x=300,y=105)

        card_hol_namelbl=Label(frame,text="Name",fg="Black",bg="#FFD700",font=("Segoe UI",20,))
        card_hol_namelbl.place(x=50,y=150)
        def allowonlyalpha(char,action):
            if action == '1':
                return char.isalpha() or char.isspace()
            return True
        validate_cmd = subwindow.register(allowonlyalpha)
        card_hol_nameent=Entry(frame,width=30,bg="white",fg="black",font=("Segoe UI",15,),validate="key",validatecommand=(validate_cmd,"%S", "%d"))
        card_hol_nameent.place(x=300,y=155)

        user_idlbl=Label(frame,text="User Id",fg="Black",bg="#FFD700",font=("Segoe UI",20,))
        user_idlbl.place(x=50,y=200)
        def notallowspaces(char):
            return char != " "
        spc_cmd = subwindow.register(notallowspaces)
        user_ident=Entry(frame,width=30,bg="white",fg="black",font=("Segoe UI",15,),validate="key",validatecommand=(spc_cmd,"%S"))
        user_ident.place(x=300,y=205)
        atmsubslbl=Label(frame,text="@atm.com",fg="Black",bg="white",font=("Segoe UI",10,))
        atmsubslbl.place(x=560,y=210)


        def allownum(char,current_text):
            return char.isdigit() and len(current_text) <= 4
        passconf = (subwindow.register(allownum), '%S', '%P')

        passwdlbl=Label(frame,text="Password",fg="Black",bg="#FFD700",font=("Segoe UI",20,))
        passwdlbl.place(x=50,y=250)
        passwdent=Entry(frame,width=30,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=passconf)
        passwdent.place(x=300,y=255)

        confirm_passwdlbl=Label(frame,text="Confirm Password",fg="Black",bg="#FFD700",font=("Segoe UI",20,))
        confirm_passwdlbl.place(x=50,y=300)
        confirm_passwdent=Entry(frame,width=30,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=passconf)
        confirm_passwdent.place(x=300,y=305)

        def submit():
            def verify():
                from tkinter import messagebox
                if passwdent.get() == confirm_passwdent.get():
                    if len(card_nument.get()) == 12 and len(card_hol_nameent.get()) > 0 and len(user_ident.get()) > 0:
                        try:
                            global connection
                            connection = connect(
                                host="localhost",
                                user="root",
                                password="Kishore@2000")
                            mycursor = connection.cursor()
                            mycursor.execute("CREATE DATABASE IF NOT EXISTS atm")
                            mycursor.close()
                            connection.database = "atm"
                            print("Atm holders is DATABASE CONNECTED")
                            cursor=connection.cursor()
                            checquery="Select count(*) from ATMHOLDERS where CARD_NUMBER = %s"
                            cursor.execute(checquery,(card_nument.get(),))
                            counterbuf=cursor.fetchone()
                            if counterbuf[0] == 0:
                                if "@atm.com" not in user_ident.get():
                                    userid=user_ident.get()+"@atm.com"
                                else:
                                    userid=user_ident.get()
                                cursor.execute("CREATE TABLE IF NOT EXISTS ATMHOLDERS(CARD_NUMBER VARCHAR(12) PRIMARY KEY,NAME VARCHAR(100),USER_ID VARCHAR(100),PIN VARCHAR(4),BALANCE INT DEFAULT 0)")
                                cursor.execute("INSERT INTO ATMHOLDERS VALUES(%s,%s,%s,%s,%s)",(card_nument.get(),card_hol_nameent.get(),userid,passwdent.get(),0))
                                connection.commit()
                                messagebox.showinfo("Success","Account Created Successfully")
                                card_nument.delete(0,END)
                                card_hol_nameent.delete(0,END)
                                user_ident.delete(0,END)
                                passwdent.delete(0,END)
                                confirm_passwdent.delete(0,END)
                                cursor.close()
                                connection.close()
                                print("Atm holders DataBase Connection Closed")
                            else:
                                messagebox.showinfo("Error","Card Number already exists")
                                card_nument.delete(0,END)
                                cursor.close()
                        except Error as e:
                            print("Error while connecting to MySQL", e)
                            messagebox.showinfo("Error","Unable to create account")
                    else:
                        messagebox.showinfo("Success","Fill all the fields")
                else:
                    messagebox.showinfo("Error","Password Mismatch")

            verify()

        submitbtn=Button(frame,text="Submit",fg="Black",bg="grey",font=("Segoe UI",15),command=submit)
        submitbtn.place(x=300,y=370)


Class=Administrator()
