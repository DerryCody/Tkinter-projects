import tkinter
import tkinter.filedialog

screen=tkinter.Tk()
screen.geometry("750x900")

screen.title("Memorizer")
screen.configure(background="blue")

food=["Apple","Banana","Cherry","Dragonfruit","Eggplant","Fruit","Grapes"]

def openf():
   of=tkinter.filedialog.askopenfile()
   fr=of.readlines()
   for l in fr:
      list1.insert(tkinter.END,l)


def deletef():
   items=list1.curselection()
   for item in reversed(items):
      list1.delete(item)

def savef():
   f=tkinter.filedialog.asksaveasfile()
   for i in list1.get(0,tkinter.END):
      print(i.strip(),file=f)
   list1.delete(0,tkinter.END)
   

def addf():
   inputv=input1.get()
   list1.insert(tkinter.END,inputv)
   input1.delete(0,tkinter.END)

open=tkinter.Button(screen,background="white",command=openf,text="OPEN",font=("times new roman",50))
open.place(x=50,y=50)

delete=tkinter.Button(screen,background="white",command=deletef,text="DELETE",font=("times new roman",50))
delete.place(x=250,y=50)

save=tkinter.Button(screen,background="white",command=savef,text="SAVE",font=("times new roman",50))
save.place(x=500,y=50)

add=tkinter.Button(screen,background="white",command=addf,text="ADD",font=("times new roman",50))
add.place(x=550,y=150)

input1=tkinter.Entry(screen,fg="white",font=("times new roman",50))
input1.place(x=50,y=150)

list1=tkinter.Listbox(screen,width=50,height=30,selectmode=tkinter.MULTIPLE)
list1.place(x=50,y=250)
for fruits in food:
   list1.insert(tkinter.END,fruits)

screen.mainloop()