a=int(input("enter a number"))
def fact(n):
    if n==1:
        return 1
    else:
        return(n * fact(n-1))
num=a
if num==0:
    print("1")
else:
    print("The factorial of",num,"is",fact(num))