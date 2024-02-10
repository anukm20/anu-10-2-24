#a=lambda a,b:a*b
#print(a(2,4))


def fun(a):
    return lambda b:a+b
c=fun(2)
print(c(4))