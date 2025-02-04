import tkinter
import tkinter.messagebox
import random

screen=tkinter.Tk()
screen.geometry("650x600")

screen.title("ping-pong")
screen.configure(background="black")



canvas=tkinter.Canvas(screen,width=650,height=600,background="black")
canvas.grid(row=1,column=0,columnspan=5)

scoreboard=canvas.create_text(325,20,text="0:0",font=("timesnewroman",30,"normal"),fill="blue")

canvas.create_line(325,0,325,600,fill="white",width=2,smooth=True)
canvas.create_oval(250,200,400,350,width=5,outline="white")
class Ball():
    def __init__(self,p1,p2):
        self.ppball=canvas.create_oval(300,275,350,325,fill="green")
        self.magnitudenumbs=[1,2,3,4,5,-1,-2,-3,-4,-5]
        random.shuffle(self.magnitudenumbs)
        self.x=self.magnitudenumbs[0]
        self.y=self.magnitudenumbs[1] 
        self.p1score=0
        self.p2score=0
        self.p1=p1
        self.p2=p2
    def draw(self):
        canvas.move(self.ppball,self.x,self.y)
        self.coords=canvas.coords(self.ppball)
        if self.coords[1]<=0:
            self.y=self.y*-1
        if self.coords[0]<=0:
            self.x=self.x*-1
            self.p2score=self.p2score+1
            canvas.itemconfigure(scoreboard,text=str(self.p1score)+":"+str(self.p2score))
        if self.coords[3]>=600:
            self.y=self.y*-1
        if self.coords[2]>=650:
            self.x=self.x*-1
            self.p1score=self.p1score+1
            canvas.itemconfigure(scoreboard,text=str(self.p1score)+":"+str(self.p2score))
    def collision(self):
        self.playercoords=canvas.coords(self.p1.player1box)
        self.player2coords=canvas.coords(self.p2.player2box)
        if self.playercoords[3]>=self.coords[1] and self.playercoords[1]<=self.coords[3]:
            if self.playercoords[2]>=self.coords[0] and self.playercoords[0]<=self.coords[2]:
                self.x=+4
        if self.player2coords[1]<=self.coords[3] and self.player2coords[3]>=self.coords[1]:
            if self.player2coords[0]<=self.coords[2] and self.player2coords[2]>=self.coords[0]:
                self.x=-4

class Player1():
    def __init__(self):
        self.player1box=canvas.create_rectangle(0,250,20,350,fill="purple")
        self.y=0
        canvas.bind_all('w',self.moveup)
        canvas.bind_all('s',self.movedown)
    def draw(self):
        canvas.move(self.player1box,0,self.y)
        self.coords=canvas.coords(self.player1box)
        if self.coords[1]<=0:
            self.y=0
        if self.coords[3]>=600:
            self.y=0
    def moveup(self,event):
        self.y=-4
    def movedown(self,event):
        self.y=+4

class Player2():
    def __init__(self):
        self.player2box=canvas.create_rectangle(630,250,650,350,fill="purple")
        self.y=0
        canvas.bind_all('<KeyPress-Up>',self.moveup2)
        canvas.bind_all('<KeyPress-Down>',self.movedown2)
    def draw(self):
        canvas.move(self.player2box,0,self.y)
        self.coords=canvas.coords(self.player2box)
        if self.coords[1]<=0:
            self.y=0
        if self.coords[3]>=600:
            self.y=0
    def moveup2(self,event):
        self.y=-4
    def movedown2(self,event):
        self.y=+4    

player2=Player2()            
player1=Player1()
ball=Ball(player1,player2)
while True:
  ball.draw()
  player1.draw()
  player2.draw()
  ball.collision()
  screen.update_idletasks()
  screen.update()
  


screen.mainloop()


