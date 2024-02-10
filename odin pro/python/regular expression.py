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
import re
terms="^anurag+$"
a=re.search(terms,"anuraggg")
if a:
    print("matched")
else:
    print("not matched")