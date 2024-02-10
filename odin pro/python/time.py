time=int(input("Enter the time: "))
if time>=5 and time<12:
    print("Good morning!")
elif time>=12 and time<17:
    print("Good afternoon")
elif time>=17 and time<21:
    print("Good evening")
else:
    print("Good night!")