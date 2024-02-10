ls=[]
while True:
    print("___________________________________")
    print("1-add todo")
    print("2-display todos")
    print("3-delete todo")
    print("4-exit")
    print("___________________________________")
    a=str(input("enter your choice: "))
    if a=="1":
        r=str(input("enter todo: "))
        ls.append(r)
    elif a=="2":
        print(ls)
    elif a=="3":
        y=str(input("enter todo for delete:"))
        ls.remove(y)
        print(ls)
    elif a=="4":
        print("end")  
        break
    else:
        print("invalid input")