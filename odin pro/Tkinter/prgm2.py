from tkinter import *
from tkinter import messagebox
root=Tk()
l1=Label(root,text="enter first number")
e1=Entry(root)
l1.pack()
e1.pack()
l2=Label(root,text="enter second number")
e2=Entry(root)
l2.pack()
e2.pack()
btn=Button(root,text="Add")
def anar():
    messagebox.askyesno("submit","are you sure to exit")
Button(root,text="EXIT",command=anar).pack()

l3=Label(root,text="result")

l3.pack()
root.mainloop()