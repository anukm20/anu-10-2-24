row=int(input("enter the rows: "))
col=int(input("enter the columns: "))
result=[[0 for col in range(col)]for row in range(row)]
result[row][col]=row*col
print(result)
