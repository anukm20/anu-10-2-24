from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
if __name__=="__main__":
    calc=Tk()
    calc.configure(background="light green")
    calc.title("Calculator")
    calc.geometry("270x150")
    equation=StringVar()
    expression.grid(columspan=4,ipadx=70)

btn1=Button(calc,text='1',fg='white',bg='gray',command=lambda:press(1),height=1,width=7)
btn1.grid(row=2,column=0)
btn2=Button(calc,text='2',fg='white',bg='gray',command=lambda:press(2),height=1,width=7)
btn2.grid(row=2,column=1)
btn3=Button(calc,text='3',fg='white',bg='gray',command=lambda:press(3),height=1,width=7)
btn3.grid(row=2,column=2)
btn4=Button(calc,text='4',fg='white',bg='gray',command=lambda:press(4),height=1,width=7)
btn4.grid(row=3,column=0)
btn5=Button(calc,text='5',fg='white',bg='gray',command=lambda:press(5),height=1,width=7)
btn5.grid(row=3,column=1)
btn6=Button(calc,text='6',fg='white',bg='gray',command=lambda:press(6),height=1,width=7)
btn6.grid(row=3,column=2)
btn7=Button(calc,text='7',fg='white',bg='gray',command=lambda:press(7),height=1,width=7)
btn7.grid(row=4,column=0)
btn8=Button(calc,text='8',fg='white',bg='gray',command=lambda:press(8),height=1,width=7)
btn8.grid(row=4,column=1)
btn9=Button(calc,text='9',fg='white',bg='gray',command=lambda:press(9),height=1,width=7)
btn9.grid(row=4,column=2)
btn0=Button(calc,text='0',fg='white',bg='gray',command=lambda:press(0),height=1,width=7)
btn0.grid(row=5,column=0)
pls=Button(calc,text='+',fg='white',bg='gray',command=lambda:press("+"),height=1,width=7)
pls.grid(row=5,column=3)
mins=Button(calc,text='-',fg='white',bg='gray',command=lambda:press("-"),height=1,width=7)
mins.grid(row=3,column=3)
mul=Button(calc,text='*',fg='white',bg='gray',command=lambda:press("*"),height=1,width=7)
mul.grid(row=4,column=3)
div=Button(calc,text='/',fg='white',bg='gray',command=lambda:press("/"),height=1,width=7)
div.grid(row=2,column=3)
eql=Button(calc,text='=',fg='white',bg='gray',command=equalpress,height=1,width=7)
eql.grid(row=5,column=2)
clr=Button(calc,text='clr',fg='white',bg='gray',command=clear,height=1,width=7)
clr.grid(row=5,column=1)
decim=Button(calc,text='.',fg='white',bg='gray',command=lambda:press('.'),height=1,width=7)
decim.grid(row=6,column=0)
calc.mainloop()