bill=0
height=float(input("what is your height in cm?"))
if(height>=120):
    print("congrats! you can ride")
    age=int(input("what is your age?"))
    if(age<=12):
        print("child ticket is of $5")
        bill=5
    elif(age>12):
        print("your ticket is of $8")
        bill=8
    else:
        print("adult ticket is of $12")
        bill=12
    want_pics=str(input("do you want pictures? Y or N"))
    bill_total=bill+3
    if(want_pics=="N"):
        print("your total bill is:",bill)
    else:
        print("your total bill is:",bill_total)
else:
    print("grow taller to ride")
