n=int(input("enter the number: "))
if n<0:
    print("enter a positive number")
else:
    sum=0
    while(n>0):
        sum+=n
        n-=1
    print("the sum is: ",sum)