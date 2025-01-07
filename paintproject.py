import tkinter

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
        self.screen.mainloop()
    def penchoice(self):
        pass
    def colourchoice(self):
        pass
    def brushchoice(self):
        pass
    def eraserchoice(self):
        pass
    def size(self):
        pass

Brush()