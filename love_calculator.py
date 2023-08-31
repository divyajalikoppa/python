print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name=name1+name2
S=name.lower()
t=S.count("t")
r=S.count("r")
u=S.count("u")
e=S.count("e")
true=t+r+u+e
l=S.count("l")
o=S.count("o")
v=S.count("v")
e=S.count("e")
love=l+o+v+e
true_love=int(str(true)+str(love))
if (true_love<10) or (true_love>90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif (true_love<=40) and (true_love>=50):
    print(f"Your score is {true_love} , you are alright together.")
else:
    print(f"your score is{true_love}")
