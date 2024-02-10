str="malayalam"
a= {b : str.count(b) for b in set(str )}
print(str(a))