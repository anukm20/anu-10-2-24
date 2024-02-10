from tkinter import *
class myclass:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()    
        self.okbtn=Button(frame,text="ok",command=self.anar)
        self.okbtn.pack()  
        self.btn=Button(frame,text="quit",command=frame.quit)
        self.btn.pack()
    def anar(self):
        print("gulugulu")
root=Tk()
obj=myclass(root)     
root.mainloop()