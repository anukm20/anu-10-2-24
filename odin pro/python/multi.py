sub1=float(input("enter the mark of english"))
sub2=float(input("enter the mark of hindi"))
sub3=float(input("enter the mark of malayalam"))
sub4=float(input("enter the mark of physics"))
sub5=float(input("enter the mark of maths"))
Total=sub1+sub2+sub3+sub4+sub5
print("Total mark is",Total)
percentage=(Total/500)*100
print("percentage is",percentage)
if percentage<45:
    print("fail")
elif percentage>=45 and percentage<60:
    print("pass")
elif percentage>=65 and percentage>75:
    print("good")
elif percentage>=75 and percentage>85:
    print("very good")
elif percentage>=85 and percentage<100:
    print("excellent")
else:
    print("error")