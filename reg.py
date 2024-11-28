from tkinter import*

base=Tk()

base.geometry("500x500")

lb1=Label(base,text="Name",width=10,font=("arial",12))

lb1.place(x=20,y=120)

en1=Entry(base)

en1.place(x=140,y=120)

lb2=Label(base,text="Email",width=13,font=("arial",12))

lb2.place(x=20,y=200)

en2=Entry(base)
en2.place(x=140,y=200)

lb3=Label(base,text="Password",width=10,font=("arial",12))

lb3.place(x=20,y=280)

en3=Entry(base)
en3.place(x=140,y=280)

Button(base,text="Submit",width=10).place(x=60,y=360)

base.mainloop()