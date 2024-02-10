from tkinter import *
calc=Tk()
btns_frame=Frame(calc)
calc.geometry("312x324")
calc.resizable(0,0)
calc.title("Calculator")
def btnclk(item):
    global expression
    expression=expression+str(item)
    input.set(expression)
def btnclr():
    global expression
    expression=""
    input.set("")
def btneql():
    global expression
    result=str(eval(expression))
    input.set(result)
    expression=""
    expression=""
    input=StringVar()
    frame=Frame(calc,width=320,height=52,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=2)
    frame.pack(side=TOP)
    input_field=Entry(frame,font=('aria',18,'bold'),textvariable=input,width=50,bg="#eee",bd=0,justify=RIGHT)
    input_field.grid(row=0,column=0)
    input_field.pack(ipady=10)
    btns_frame=Frame(calc,width=312,height=272.5,bg="gray")
    btns_frame.pack()
clr=Button(btns_frame,text='clr',fg='black',width=32,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btnclr()).grid(row=0,column=0,columnspan=3,padx=1,pady=1).pack()
# btn7=Button(btns_frame,text='7',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(7)).grid(row=1,column=0,columnspan=1,padx=1,pady=1)
# btn8=Button(btns_frame,text='8',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(8)).grid(row=1,column=1,columnspan=1,padx=1,pady=1)
# btn9=Button(btns_frame,text='9',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(9)).grid(row=1,column=2,columnspan=1,padx=1,pady=1)
# btn4=Button(btns_frame,text='4',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(4)).grid(row=2,column=0,columnspan=1,padx=1,pady=1)
# btn5=Button(btns_frame,text='5',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(5)).grid(row=2,column=1,columnspan=1,padx=1,pady=1)
# btn6=Button(btns_frame,text='6',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(6)).grid(row=2,column=2,columnspan=1,padx=1,pady=1)
# btn1=Button(btns_frame,text='1',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(1)).grid(row=3,column=0,columnspan=1,padx=1,pady=1)
# btn2=Button(btns_frame,text='2',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(2)).grid(row=3,column=1,columnspan=1,padx=1,pady=1)
# btn3=Button(btns_frame,text='3',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(3)).grid(row=3,column=2,columnspan=1,padx=1,pady=1)
# pls=Button(btns_frame,text='+',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk("+")).grid(row=3,column=3,columnspan=1,padx=1,pady=1)
# mins=Button(btns_frame,text='-',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk("-")).grid(row=2,column=3,columnspan=1,padx=1,pady=1)
# mul=Button(btns_frame,text='*',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk("*")).grid(row=1,column=3,columnspan=1,padx=1,pady=1)
# div=Button(btns_frame,text='/',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk("/")).grid(row=0,column=3,columnspan=1,padx=1,pady=1)
# eql=Button(btns_frame,text='=',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btneql("=")).grid(row=4,column=3,columnspan=1,padx=1,pady=1)
# decim=Button(btns_frame,text='.',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(".")).grid(row=4,column=2,columnspan=1,padx=1,pady=1)
# zero=Button(btns_frame,text='0',fg='black',width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btnclk(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
calc.mainloop()
    