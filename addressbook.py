import tkinter
import tkinter.filedialog

screen=tkinter.Tk()
screen.geometry("750x900")

screen.title("My address book")
screen.configure(background="white")

data={}
def lu():
  global data
  Names1=data.keys()
  Names.delete(0,tkinter.END)
  for Name in Names1:
    Names.insert(tkinter.END,Name)
def openf():
  pass
def savef():
  pass
def edit():
  pass
def delete():
  pass
def update():
  global data
  namev=namei.get()
  addressv=addressi.get()
  mobilev=mobilei.get()
  emailv=emaili.get()
  birthdayv=birthdayi.get()
  data[namev]=[addressv,mobilev,emailv,birthdayv]
  lu()

title=tkinter.Label(screen,background="grey",text="My address book",font=("times new roman",30))
title.grid(row=0,column=1)

open=tkinter.Button(screen,background="white",command=openf,text="OPEN",font=("times new roman",30))
open.grid(row=0,column=2)

Names=tkinter.Listbox(screen,width=40,height=30,selectmode=tkinter.SINGLE)
Names.grid(row=1,column=0,rowspan=5,columnspan=2)

editb=tkinter.Button(screen,background="white",command=edit,text="EDIT",font=("times new roman",30))
editb.grid(row=6,column=0)

deleteb=tkinter.Button(screen,background="white",command=delete,text="DELETE",font=("times new roman",30))
deleteb.grid(row=6,column=1)

namel=tkinter.Label(screen,background="grey",text="Name:",font=("times new roman",30))
namel.grid(row=1,column=2)

namei=tkinter.Entry(screen,fg="white",font=("times new roman",30))
namei.grid(row=1,column=3)

addressl=tkinter.Label(screen,background="grey",text="Address:",font=("times new roman",30))
addressl.grid(row=2,column=2)

addressi=tkinter.Entry(screen,fg="white",font=("times new roman",30))
addressi.grid(row=2,column=3)

mobilel=tkinter.Label(screen,background="grey",text="Mobile:",font=("times new roman",30))
mobilel.grid(row=3,column=2)

mobilei=tkinter.Entry(screen,fg="white",font=("times new roman",30))
mobilei.grid(row=3,column=3)

emaill=tkinter.Label(screen,background="grey",text="Email:",font=("times new roman",30))
emaill.grid(row=4,column=2)

emaili=tkinter.Entry(screen,fg="white",font=("times new roman",30))
emaili.grid(row=4,column=3)

birthdayl=tkinter.Label(screen,background="grey",text="Birthday:",font=("times new roman",30))
birthdayl.grid(row=5,column=2)

birthdayi=tkinter.Entry(screen,fg="white",font=("times new roman",30))
birthdayi.grid(row=5,column=3)

updateb=tkinter.Button(screen,background="white",command=update,text="UPDATE",font=("times new roman",30))
updateb.grid(row=6,column=3,)

saveb=tkinter.Button(screen,background="white",command=savef,width=20,text="SAVE",font=("times new roman",30))
saveb.grid(row=7,column=1,columnspan=2)


screen.mainloop()