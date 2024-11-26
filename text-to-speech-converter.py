import tkinter
from gtts import gTTS

screen=tkinter.Tk()
screen.geometry("750x900")

screen.title("Text to speech converter")
screen.configure(background="green")

def convert():
    af=gTTS(text.get(),lang="en",slow=False)
    af.save("ttsa.wav")

title=tkinter.Label(screen,background="grey",text="Text to speech converter",font=("times new roman",50))
title.place(x=150,y=200)

text=tkinter.Entry(screen,background="grey",font=("times new roman",50))
text.place(x=150,y=400)

convertb=tkinter.Button(screen,background="white",command=convert,text="CONVERT",font=("times new roman",30))
convertb.place(x=300,y=600)

screen.mainloop()