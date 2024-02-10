#ls=[]
#for i in range(1,101):
 #   if i%3==0:
  #      i="fizz"
   # ls.append(i)
#print(ls)



ls=[]
for i in range(1,101):
     if i%3==0 and i%5==0:
        ls.append("fizzbuzz")
     elif i%5==0:
        ls.append("buzz")
     elif i%3==0:
        ls.append("fizz")
     else:
         ls.append(i)
     
print(ls)
