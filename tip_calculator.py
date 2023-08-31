#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print('welcome to tip calculator')
bill=float(input('what was the total bill?$'))
tip = int(input('how much tip would u like to give? 10,12,or 15?'))
people=int(input('how many people to split the bill?'))
tip_as_percent=tip/100
tip_as_amount=bill*tip_as_percent
total_bill= bill+tip_as_amount
total_people=total_bill/people
print(round(total_people,2))


