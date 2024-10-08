import tkinter
import tkinter.ttk
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("900x1000")

screen.title("Times Tables")
screen.configure(background="pink")

radioc=tkinter.IntVar()


numbers=[]
for i in range(1,100):
    numbers.append(i)

def generate():
    result1=""
    num1=num.get()
    tkinter.messagebox.showinfo("Hi","Number is "+num1)
    radionum=radioc.get()
    for i in range(1,radionum+1):
        result1+=str(num1)+"x"+str(i)+"="+str(int(num1)*i)+"\n"
    result.configure(text=result1)
        

result=tkinter.Label(screen,background="grey",text="",font=("times new roman",15))        
result.place(x=225,y=450)

fm=tkinter.Label(screen,background="grey",text="Enter your first number",font=("times new roman",50))
fm.place(x=225,y=150)

num=tkinter.ttk.Combobox(screen,background="white",font=("times new roman",50))
num["values"]=numbers
num.place(x=225,y=250)

range1=tkinter.ttk.Radiobutton(screen,text="10",variable=radioc,value=10)
range1.place(x=800,y=250)

range2=tkinter.ttk.Radiobutton(screen,text="20",variable=radioc,value=20)
range2.place(x=800,y=275)

range3=tkinter.ttk.Radiobutton(screen,text="30",variable=radioc,value=30)
range3.place(x=800,y=300)

radioc.set(10)

genb=tkinter.Button(screen,background="white",text="Generate",command=generate,font=("times new roman",50))
genb.place(x=350,y=350)




screen.mainloop()