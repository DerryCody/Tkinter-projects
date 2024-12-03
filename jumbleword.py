import tkinter
import random
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("500x600")

screen.title("Jumbleword")
screen.configure(background="black")

words=["apple","watermelon","chairs","microphone","impossible","insane","supercalifragilistic","pocahontas"]
jumblewords=["pleap","lemontware","shairc","enmocripoh","sibimposle","ennsia","lifrcapurseilsictgis","shpoacnta"]
score=0
jumbleword=""
wordchosen=""

def pickword():
    global jumbleword,wordchosen
    wordchosen=random.choice(words)
    i=words.index(wordchosen)
    jumbleword=jumblewords[i]
    word.config(text=jumbleword)


def check():
    global score,words,jumblewords,jumbleword
    if guess.get()==wordchosen:
        score=score+1
        jumblewords.remove(jumbleword)
        words.remove(wordchosen)
        if words==[] and reset:
          tkinter.messagebox.showinfo("Hi","Well done! You guessed the words correctly")
          checkb.config(state="disabled")
        else:
          pickword()
    else:
        score=score-1
    scorel.config(text=score)

def reset():
    global words,jumblewords
    words.extend(["apple","watermelon","chairs","microphone","impossible","insane","supercalifragilistic","pocahontas"])
    jumblewords.extend(["pleap","lemontware","shairc","enmocripoh","sibimposle","ennsia","lifrcapurseilsictgis","shpoacnta"])
    checkb.config(state="normal")

title=tkinter.Label(screen,background="grey",text="Jumbleword game",font=("times new roman",50))
title.grid(row=0,column=0,pady=20)

word=tkinter.Label(screen,background="grey",font=("times new roman",50))
word.grid(row=1,column=0,pady=20)

guess=tkinter.Entry(screen,fg="white",font=("times new roman",50))
guess.grid(row=2,column=0,pady=20)

checkb=tkinter.Button(screen,background="white",command=check,text="Check",font=("times new roman",30))
checkb.grid(row=3,column=0,pady=20)

resetb=tkinter.Button(screen,background="white",command=reset,text="Reset",font=("times new roman",30))
resetb.grid(row=4,column=0,pady=20)

scorel=tkinter.Label(screen,background="grey",font=("times new roman",30))
scorel.grid(row=5,column=0,pady=20)


pickword()
screen.mainloop()