
"""local"""
#def abc():
#    a=20
#    print(a)
#abc()

"""global"""
#a=20
#def abc():
#    print(a)
#abc()


"""enclosed"""
#def abc():
#    a=20
#    def adc():
#        print(a)
#    adc()
#abc()


"""recurction"""
#a=1
#def abc(b):
#    if b<=20:
#        print(b)
#        b=b+1
#        abc(b)
#abc(a)


"""factorial"""
#def fact(n):
#    if n==5:
#        return 120
#    else:
#        return n*fact(n-1)
#res=fact(5)
#print(res)

a=100
def ala(b):
    if b>=1:
        print(b)
        b=b-1
        ala(b)
ala(a)