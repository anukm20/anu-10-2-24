from tkinter import *
root=Tk()
Button1=Button(root,text="login",bg="red",fg="white")
Button1.pack(fill="x")
Button2=Button(root,text="login",bg="yellow",fg="white")
Button2.pack(fill="y",side="left")
Button3=Button(root,text="login",bg="red",fg="white")
Button3.pack(fill="x",side="bottom")
Button4=Button(root,text="login",bg="yellow",fg="white")
Button4.pack(fill="y",side="right")


root.mainloop()