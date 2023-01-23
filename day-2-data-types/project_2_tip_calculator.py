print("Welcome to the tip calculator!")
bill = float(input("What was total bill? $"))
tip = int(input("How much tip? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill
total_bill = bill + bill_with_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")
