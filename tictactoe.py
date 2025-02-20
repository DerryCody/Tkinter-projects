import tkinter 
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("619x700")

screen.title("Tic-Tac-Toe")
screen.configure(background="blue")
availableplaces=["","","","","","","","",""]
next=1
possiblewins=[(0,1,2),(0,4,8),(8,5,2),(8,7,6),(0,4,8),(2,4,6),(3,4,5),(1,4,7)]


def p1place(buttonchosen,buttonpos):
    global next
    if next==1 and availableplaces[buttonpos-1]=="":
        buttonchosen.config(text="X")
        availableplaces[buttonpos-1]="X"
        next=next+1
    elif next==2 and availableplaces[buttonpos-1]=="":
        buttonchosen.config(text="O")
        availableplaces[buttonpos-1]="O"
        next=next-1   
    winner()     

def winner():
    for pss in possiblewins:
      if "X" == availableplaces[pss[0]] and "X" == availableplaces[pss[1]] and "X" == availableplaces[pss[2]]:
          tkinter.messagebox.showinfo("Hi","Player 1 wins!")
          screen.destroy()
      if "O" == availableplaces[pss[0]] and"O" == availableplaces[pss[1]] and "O" == availableplaces[pss[2]]:
          tkinter.messagebox.showinfo("Hi","Player 2 wins!")
          screen.destroy()
    print(availableplaces)
 

P1=tkinter.Label(screen,background="grey",text="Player 1 : X",font=("times new roman",50))
P1.grid(row=0,column=1)
P2=tkinter.Label(screen,background="grey",text="Player 2 : O",font=("times new roman",50))
P2.grid(row=1,column=1)
B1=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B1,1))
B1.grid(row=2,column=0)
B2=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B2,2))
B2.grid(row=2,column=1)
B3=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B3,3))
B3.grid(row=2,column=2)
B4=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B4,4))
B4.grid(row=3,column=0)
B5=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B5,5))
B5.grid(row=3,column=1)
B6=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B6,6))
B6.grid(row=3,column=2)
B7=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B7,7))
B7.grid(row=4,column=0)
B8=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B8,8))
B8.grid(row=4,column=1)
B9=tkinter.Button(screen,background="white",font=("times new roman",30),width=10,height=5,command=lambda:p1place(B9,9))
B9.grid(row=4,column=2)


screen.mainloop()