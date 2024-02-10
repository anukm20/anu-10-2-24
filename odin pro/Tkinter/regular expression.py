# import re
# terms="gulugulu"
# a=re.search(terms,"hallo gulugulu")
# print(a)


"""re matched or notmachted"""
# import re
# terms="['a-zA-Z0-9']nurag"
# a=re.match(terms,"anurag")
# if a:
#     print("matched")
# else:
#     print("not matched")



"""dot anu charector"""
# import re
# terms="['a-zA-Z0-9']....."
# a=re.match(terms,"anurag")
# if a:
#     print("matched")
# else:
#     print("not matched")



""" """
# import re
# terms="^anurag+$"
# a=re.search(terms,"anuraggg")
# if a:
#     print("matched")
# else:
#     print("not matched")


"""date"""
# import re
# a=str(input("enter tha date: "))
# terms="^[012]\d|3[01]-[0]\d|1[012]-\d{4}$"
# b=re.search(terms,a)
# if b:
#     print("valid")
# else:
#     print("not valid")


"""date ZERO not"""
# import re
# a=str(input("enter tha date: "))
# terms="^([^00]|[0][1,9]|[12][1,9]|3[1]|[123][0])(-|.|/)([^00]|[0][1,9]|1[012])(-|.|/)([^0000]\d{4})$"
# b=re.search(terms,"11-11-0000")
# if b:
#     print("valid")
# else:
#     print("not valid")


"""email validation"""
# import re
# a=str(input("enter tha email: "))
# terms="^([a-zA-Z].+)@([a-zA-Z]{2,})(\.[a-zA-Z]{2,})$"
# b=re.search(terms,a)
# if b:
#     print("valid")
# else:
#     print("not valid")


"""password validation"""
# import re
# a=str(input("enter the password: "))
# terms="^([A-Z]\w{3,})(\W\w{2,})$"
# b=re.search(terms,a)
# if b:
#     print("valid")
# else:
#     print("not valid")


"""vowels"""
# import re
# a=str(input("enter the sentence: "))
# terms="(a|e|i|o|u|A|E|I|O|U)"
# b=re.findall(terms,a)
# print(b)
# print(len(b))


"""username,email and password"""
import re
d=str(input("enter the user name: "))
terms="^([A-Za-z]\w{4,20})$"
r=re.search(terms,d)
a=str(input("enter tha email: "))
terms="^([a-zA-Z].+)@([a-zA-Z]{2,})(\.[a-zA-Z]{2,})$"
b=re.search(terms,a)
a=str(input("enter the password: "))
terms="^([A-Z]\w{3,})(\W\w{2,})$"
c=re.search(terms,a)
if r:
    print("username valid")
else:
    print("username not valid")
if b:
    print("email valid")
else:
    print("email not valid")

if c:
    print("password valid")
else:
    print("password not valid")