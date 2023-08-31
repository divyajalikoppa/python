#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")
x=int(age)
day=(90-x)*365
week=(90-x)*52
month=(90-x)*12
print(f"you have {day} days,{week} weeks,{month} months")
