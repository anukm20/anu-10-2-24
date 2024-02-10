#file=open("anar.txt","r")
#a=file.readline()
#print(a)
#file.close()



with open("anar.txt","r")as file:
    a=file.read()
    print(a)