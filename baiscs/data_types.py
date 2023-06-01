# Learned about DATA TYPES

print('welcome to day 2')

name = 3

if name > 6:
    print(True)
else:
    print(False)


age = input('what is your age? ')

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} left"
print(message)

print('welcome to the tip calculator')

bill = float(input('what was your total bill? $'))
bill_split_by_people = int(input('how many people to split the bill '))
tip = int(input('what percentage tip would you like to give? 10, 12 or 15? '))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / bill_split_by_people

# the both total_payment declare works the same
# total_payment = round(bill_per_person, 2)
# rounding a number to 2 decimal places

total_payment = "{:.2f}".format(bill_per_person)
payment = f'each person is going to pay: ${total_payment}'
print(payment)
