#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to he tip calculator!")
bill_amount = float(input("What was the total bill?"))
tip_percent = float(input("How much tip would you like to give?"))
final_tip_percent = bill_amount * (tip_percent / 100) + bill_amount

split_amt = float(input("How many people to split the bill?"))

each_person = final_tip_percent / split_amt 

print(round(each_person , 2))