#BMI calculation and printing weight status
"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI=round(weight/(height**2))
if(BMI<18.5):
    print(f"your BMI is{BMI},you are under weight")
elif(BMI<25):
    print(f"your BMI is {BMI},you have a normal weight")
elif(BMI<30):
     print(f"your BMI is{BMI},you are slightly over weight")
elif(BMI<35):
      print(f"your BMI is{BMI},you are obese")
else:
    print(f"your BMI is{BMI},you are clinically obese")