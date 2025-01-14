import tkinter 
import tkinter.messagebox
import random

screen=tkinter.Tk()
screen.geometry("619x700")

screen.title("Tic-Tac-Toe")
screen.configure(background="blue")

def cplace():
    cap=random.choice(availableplaces)
    if cap["text"]=="":
        cap.config(text="X")
        cap.config(state="disabled")
        cap.config(fg="black")
        availableplaces.remove(cap)
    winner()

def pplace(buttonchosen):
    global next
    if buttonchosen["text"]=="":
        buttonchosen.config(text="O")
        buttonchosen.config(state="disabled")
        buttonchosen.config(fg="black")
        availableplaces.remove(buttonchosen)
    winner()     
    cplace()



def winner():
    for pss in possiblewins:
      if "X" == pss[0]["text"] and "X" == pss[1]["text"] and "X" == pss[2]["text"]:
          tkinter.messagebox.showinfo("Hi","Computer wins!")
          screen.destroy()
      if "O" == pss[0]["text"] and"O" == pss[1]["text"] and "O" == pss[2]["text"]:
          tkinter.messagebox.showinfo("Hi","Player wins!")
          screen.destroy()
      if len(availableplaces)==0:
          tkinter.messagebox.showinfo("Hi","It was a tie!")
 

P1=tkinter.Label(screen,background="grey",text="Computer : X",font=("times new roman",50))
P1.grid(row=0,column=1)
P2=tkinter.Label(screen,background="grey",text="Player : O",font=("times new roman",50))
P2.grid(row=1,column=1)
B1=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B1))
B1.grid(row=2,column=0)
B2=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B2))
B2.grid(row=2,column=1)
B3=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B3))
B3.grid(row=2,column=2)
B4=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B4))
B4.grid(row=3,column=0)
B5=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B5))
B5.grid(row=3,column=1)
B6=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B6))
B6.grid(row=3,column=2)
B7=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B7))
B7.grid(row=4,column=0)
B8=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B8))
B8.grid(row=4,column=1)
B9=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:pplace(B9))
B9.grid(row=4,column=2)

availableplaces=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
rows=[[B1,B2,B3],[B4,B5,B6],[B7,B8,B9]]
possiblewins=[(B1,B2,B3),(B1,B5,B9),(B9,B6,B3),(B9,B8,B7),(B1,B4,B7),(B3,B5,B7),(B4,B5,B6),(B2,B5,B8)]

screen.mainloop()