from tkinter import *
from tkinter import messagebox
from mysql.connector import connect,errors

class C_ATMSERVICES:
    def D1_servicespage(self,mypanel,crd):
        print("Entered Services Page")
        mypanel.title("Services")
        mypanel.state("zoomed")
        mypanel.configure(background="#001F3F")
        mypanel.grab_set()

        frame1=Frame(mypanel,width=600,height=100,bg="#FFD700",relief="solid",borderwidth=1)
        frame2=Frame(mypanel,width=600,height=180,bg="#FFD700",relief="solid",borderwidth=1)
        frame3=Frame(mypanel,width=600,height=180,bg="#FFD700",relief="solid",borderwidth=1)
        frame4=Frame(mypanel,width=600,height=180,bg="#FFD700",relief="solid",borderwidth=1)
        frame5=Frame(mypanel,width=800,height=100,bg="#FFD700",relief="solid",borderwidth=1)
        frame6=Frame(mypanel,width=800,height=400,bg="#FFD700",relief="solid",borderwidth=1)

        frame1.pack(pady=20)
        frame2.place(x=20,y=150)
        frame3.place(x=20,y=370)
        frame4.place(x=20,y=590)
        frame5.place(x=700,y=150)
        frame6.place(x=700,y=370)

        headinglbl=Label(frame1,text="ATM SERVICES",fg="#D3D3D3",bg="#001F3F",font=("Segoe UI",40))
        headinglbl.pack()

        try:
            connection = connect(host='localhost', user='root', password='Kishore@2000', database='atm')
            mycursor = connection.cursor()
            print("main database connection established\nongoing")
        except errors.Error as e:
            messagebox.showinfo("Error", e)

        hd2lbl=Label(frame2,text="Credit Amount",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        hd2lbl.place(x=10,y=0)

        def query():
            tblqury="CREATE TABLE IF NOT EXISTS transactions (Card_Number VARCHAR(13) NOT NULL,transaction_datetime DATETIME NOT NULL,transaction_type VARCHAR(10) NOT NULL,amount INT NOT NULL)"
            mycursor.execute(tblqury)
            connection.commit()

        def onlynum(char,current_text):
            return char.isdigit() and len(current_text) <= 13

        validate_cmd = mypanel.register(onlynum)

        numer = (mypanel.register(onlynum), '%S', '%P')
        credlbl=Label(frame2,text="Enter Amount",fg="Black",bg="#FFD700",font=("Segoe UI",17))
        credlbl.place(x=10,y=63)
        crdentry=Entry(frame2,width=30,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=numer)
        crdentry.place(x=210,y=70)
        def cred():
            if len(crdentry.get()) >= 1:
                query()
                credquery = "Insert into transactions (Card_Number,transaction_datetime,transaction_type,amount) values (%s,now(),'Credit',%s)"
                mycursor.execute(credquery, (crd,crdentry.get(),))
                updamtquery = "UPDATE ATMHOLDERS SET BALANCE = BALANCE + %s WHERE CARD_NUMBER = %s"
                mycursor.execute(updamtquery, (crdentry.get(), crd))
                connection.commit()
                crdentry.delete(0, END)
                chkbal()
            else:
                messagebox.showinfo("Error", "Invalid Amount")
        crdbtn=Button(frame2,text="Credit",fg="Black",bg="grey",font=("Segoe UI",14),command=cred)
        crdbtn.place(x=210,y=115)


        hd3lbl=Label(frame3,text="Debit Amount",fg="Black",bg="#FFD700",font=("Segoe UI",17))
        hd3lbl.place(x=10,y=0)
        debitlbl=Label(frame3,text="Enter Amount",fg="Black",bg="#FFD700",font=("Segoe UI",17))
        debitlbl.place(x=10,y=63)
        debitentry=Entry(frame3,width=30,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=numer)
        debitentry.place(x=210,y=70)
        def debit():
            if len(debitentry.get()) >= 1:
                chkbalquery = "SELECT BALANCE FROM ATMHOLDERS WHERE CARD_NUMBER = %s"
                mycursor.execute(chkbalquery, (crd,))
                bal = mycursor.fetchone()
                if bal[0] > int(debitentry.get()):
                    query()
                    dbtquery = "Insert into transactions (Card_Number,transaction_datetime,transaction_type,amount) values (%s,now(),'Debit',%s)"
                    mycursor.execute(dbtquery, (crd, debitentry.get(),))
                    updamtquery = "UPDATE ATMHOLDERS SET BALANCE = BALANCE - %s WHERE CARD_NUMBER = %s"
                    mycursor.execute(updamtquery, (debitentry.get(), crd))
                    connection.commit()
                    debitentry.delete(0, END)
                    chkbal()
                else:
                    messagebox.showinfo("Error", "Insufficient Balance")
                    debitentry.delete(0, END)
            else:
                messagebox.showinfo("Error", "Invalid Amount")

        debitbtn=Button(frame3,text="Debit",fg="Black",bg="grey",font=("Segoe UI",14),command=debit)
        debitbtn.place(x=210,y=115)

        mnytrf=Label(frame4,text="MONEY TRANSFER",fg="Black",bg="#FFD700",font=("Segoe UI",20))
        mnytrf.place(x=10,y=0)
        cardnotrf=Label(frame4,text="Enter Card Number",fg="Black",bg="#FFD700",font=("Segoe UI",17))
        cardnotrf.place(x=10,y=63)
        amountrf=Label(frame4,text="Enter Amount",fg="Black",bg="#FFD700",font=("Segoe UI",17))
        amountrf.place(x=10,y=108)
        cardnoent=Entry(frame4,width=20,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=numer)
        amtent=Entry(frame4,width=20,bg="white",fg="black",font=("Segoe UI",15),validate="key",validatecommand=numer)
        cardnoent.place(x=250,y=70)
        amtent.place(x=250,y=115)
        def send():
            if len(cardnoent.get()) >= 1:
                if len(amtent.get()) >= 1:
                    srchq="SELECT count(*) FROM ATMHOLDERS WHERE CARD_NUMBER = %s"
                    mycursor.execute(srchq, (cardnoent.get(),))
                    myresult = mycursor.fetchone()
                    if myresult[0] == 1:
                        chkbalquery = "SELECT BALANCE FROM ATMHOLDERS WHERE CARD_NUMBER = %s"
                        mycursor.execute(chkbalquery, (crd,))
                        myresult = mycursor.fetchone()
                        if myresult[0] > int(amtent.get()):
                            updamtquery1 = "UPDATE ATMHOLDERS SET BALANCE = BALANCE - %s WHERE CARD_NUMBER = %s"
                            mycursor.execute(updamtquery1, (amtent.get(), crd,))
                            updamtquery2 = "UPDATE ATMHOLDERS SET BALANCE = BALANCE + %s WHERE CARD_NUMBER = %s"
                            mycursor.execute(updamtquery2, (amtent.get(), cardnoent.get(),))
                            trnsfquerydeb = "Insert into transactions (Card_Number,transaction_datetime,transaction_type,amount) values (%s,now(),'Debit',%s)"
                            trnsfqueryced = "Insert into transactions (Card_Number,transaction_datetime,transaction_type,amount) values (%s,now(),'Credit',%s)"
                            mycursor.execute(trnsfquerydeb, (crd, amtent.get(),))
                            mycursor.execute(trnsfqueryced, (cardnoent.get(), amtent.get(),))
                            connection.commit()
                            chkbal()
                            cardnoent.delete(0, END)
                            amtent.delete(0, END)
                        else:
                            messagebox.showinfo("Error", "Insufficient Balance")
                    else:
                        messagebox.showinfo("Error", "Invalid Card Number")
                        cardnoent.delete(0, END)
                else:
                    messagebox.showinfo("Error", "Invalid Amount")
                    amtent.delete(0, END)
            else:
                messagebox.showinfo("Error", "Invalid Card Number")
                cardnoent.delete(0, END)

        sendbtn=Button(frame4,text="Send",fg="Black",bg="grey",font=("Segoe UI",14),command=send)
        sendbtn.place(x=500,y=100)


        def chkbal():
            txtfld.config(state=NORMAL)
            txtfld.delete(0.0,END)
            chkbalquery="SELECT BALANCE FROM ATMHOLDERS WHERE CARD_NUMBER = %s"
            mycursor.execute(chkbalquery, (crd,))
            bal=mycursor.fetchone()
            txtfld.insert(INSERT,"Current balance : " + str(bal[0]) )
            txtfld.config(state=DISABLED)

        chkblnbtn=Button(frame5,text="Check Balance",fg="Black",bg="grey",font=("Segoe UI",14),command=chkbal)
        chkblnbtn.place(x=20,y=28)
        txtfld=Text(frame5,width=50,height=1.4,bg="white",fg="black",font=("Segoe UI",15))
        txtfld.place(x=200,y=35)
        txtfld.config(state=DISABLED)

        def acdt():
            text_field.config(state=NORMAL)
            text_field.delete(1.0,END)
            acdtquery="SELECT Card_Number,NAME,USER_ID  FROM ATMHOLDERS WHERE CARD_NUMBER = %s"
            mycursor.execute(acdtquery, (crd,))
            acdt=mycursor.fetchall()
            for i in acdt:
                text_field.insert(INSERT, "Card Number : "+str(i[0])+"\n"+"Name : "+str(i[1])+"\n"+"User ID : "+str(i[2])+"\n")
                text_field.insert(INSERT, "\n")
            text_field.config(state=DISABLED)
        accdtbtn=Button(mypanel,text="Account Details",fg="Black",bg="grey",font=("Segoe UI",20),command=acdt)

        def minst():
            text_field.config(state=NORMAL)
            text_field.delete(1.0,END)
            minstqry="SELECT Transaction_datetime, transaction_type, amount FROM (SELECT * FROM transactions WHERE Card_Number = %s ORDER BY transaction_datetime DESC LIMIT 5) AS last_transactions ORDER BY transaction_datetime ASC"
            mycursor.execute(minstqry, (crd,))
            minst=mycursor.fetchall()
            text_field.insert(INSERT,"Transaction Datetime" + (10 * " ") + "Transaction Type" + (10 * " ") + "Amount" + "\n")
            for i in minst:
                text_field.insert(INSERT, str(i[0]) + (20 * " ") + str(i[1]) + (20 * " ") + str(i[2]) + "\n")
        minstbtn = Button(mypanel, text="MINI STATEMENT", fg="Black", bg="grey", font=("Segoe UI", 20),command=minst)
        def bnkst():
            text_field.config(state=NORMAL)
            text_field.delete(1.0,END)
            bnkstmqry="Select transaction_datetime,transaction_type,amount from transactions where Card_Number = %s"
            mycursor.execute(bnkstmqry, (crd,))
            bnkst=mycursor.fetchall()
            text_field.insert(INSERT,"Transaction Datetime" + (10*" ") + "Transaction Type" + (10*" ") + "Amount" +"\n")
            for i in bnkst:
                text_field.insert(INSERT,str(i[0]) + (20*" ") + str(i[1]) + (20*" ") + str(i[2]) +"\n")
            text_field.config(state=DISABLED)
        bnkstbtn = Button(mypanel, text="BANK STATEMENT", fg="Black", bg="grey", font=("Segoe UI", 20),command=bnkst)
        text_field = Text(frame6, width=70, height=12, font=("Segoe UI", 16), wrap="word", borderwidth=2)
        scrollb = Scrollbar(frame6, orient="vertical", command=text_field.yview)
        scrollb.place(x=764, y=17, height=362, width=20)
        text_field.configure(yscrollcommand=scrollb.set)
        text_field.config(state=DISABLED)

        accdtbtn.place(x=700, y=265)
        minstbtn.place(x=970, y=265)
        bnkstbtn.place(x=1255, y=265)
        text_field.place(x=10, y=15)

        def clsdb():
            connection.close()
            print("main Database Closed")
            mypanel.destroy()
            print("left Atm services page ")
        clsbtn=Button(mypanel,text="Close",fg="Black",bg="grey",font=("Segoe UI",20),command=clsdb)
        clsbtn.place(x=1400,y=30)

        mypanel.mainloop()



Class=C_ATMSERVICES()
