import tkinter
from tkinter.colorchooser import askcolor

class Brush():
    def __init__(self):
        self.screen=tkinter.Tk()
        self.screen.geometry("619x700")
        self.screen.title("Paint-Project")
        self.screen.configure(background="white")
        self.pen=tkinter.Button(self.screen,background="white",text="pen",font=("times new roman",30),command=self.penchoice)
        self.pen.grid(row=0,column=0)
        self.colour=tkinter.Button(self.screen,background="white",text="colour",font=("times new roman",30),command=self.colourchoice)
        self.colour.grid(row=0,column=1)
        self.brush=tkinter.Button(self.screen,background="white",text="brush",font=("times new roman",30),command=self.brushchoice)
        self.brush.grid(row=0,column=2)
        self.eraser=tkinter.Button(self.screen,background="white",text="eraser",font=("times new roman",30),command=self.eraserchoice)
        self.eraser.grid(row=0,column=3) 
        self.pensize=tkinter.Scale(self.screen,background="white",font=("times new roman",30),from_=1,to=10,orient="horizontal",fg="black")
        self.pensize.grid(row=0,column=4)
        self.canvas=tkinter.Canvas(self.screen,width=619,height=550,background="white")
        self.canvas.grid(row=1,column=0,columnspan=5)
        self.setup()
        self.screen.mainloop()
    def penchoice(self):
        self.activatebutton(self.pen)
        self.eraseron=False
    def colourchoice(self):
        self.colour=askcolor()[1]
    def brushchoice(self):
        self.activatebutton(self.brush)
        self.eraseron=False
    def eraserchoice(self):
        self.activatebutton(self.eraser)
        self.eraseron=True
    def activatebutton(self,on):
        self.activebutton.config(relief=tkinter.RAISED)
        self.activebutton=on
        self.activebutton.config(relief=tkinter.SUNKEN)
    def size(self):
        pass
    def draw(self,event):
        self.thickness=self.pensize.get()
        if self.eraseron==True:
            self.pencolour="white"
        else:
            self.pencolour=self.colour
        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,fill=self.pencolour,width=self.thickness,smooth=True)
        self.oldx=event.x
        self.oldy=event.y
    def stopd(self,event):
        self.oldx=None
        self.oldy=None
    def setup(self):
        self.thickness=5
        self.colour="black"
        self.eraseron=False
        self.activebutton=self.pen
        self.oldx=None
        self.oldy=None
        self.canvas.bind("<B1-Motion>",self.draw)
        self.canvas.bind("<ButtonRelease-1>",self.stopd)

Brush()