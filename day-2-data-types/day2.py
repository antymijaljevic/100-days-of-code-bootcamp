# data types

# string
print("Hello"[1])

print("Hello" + "234")

# integer
print(123 + 122)

# more readable
print(22_233_111)

# float
print(3.222)

# boolean
print(True, False)

# won't work
# len(22232)

# check type
# num_char = len(input("What is your name?"))
# print(type(num_char))

# convert type
# str(num_char)


a = 123
a = str(123)
a = float(123)
print(type(a))
print(70 + float("100.5"))

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# a = int(two_digit_number[0])
# b = int(two_digit_number[1])
# print(a + b)


3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

print(type(6 / 3))

# PEMDAS stands for:

#     Parentheses ()
#     Exponents **
#     Multiplication *
#     Division / 
#     Addition +
#     Subtraction -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# height = int(height)
# weight = float(weight)
# bmi = weight / height ** 2
# print(int(bmi))


# rounding float
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 3))
print(8 // 3)

# adding number
score = 0
score += 1
score -= 1
score = score + 1

# f-string
print(f"Your score is {score}")

# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# years_left = 90 - int(age)
# days = years_left * 365
# weeks = years_left * 52
# months = years_left * 12

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")