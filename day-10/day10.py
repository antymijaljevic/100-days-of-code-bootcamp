# # return keyword

# def format_name(first, last):
#     f_name = first.capitalize()
#     l_name = last.capitalize()

#     return f"{f_name} {l_name}"


# print(format_name("ante", "mijaljevic"))

# So, the main difference between capitalize() and title() is that capitalize() capitalizes 
# only the first character of a string, while title() capitalizes the first character of 
# each word in the string.


# def format_name(first, last):
#     if first == "" or last == "":
#         return "You didn't provide valid inputs"
    
#     f_name = first.capitalize()
#     l_name = last.capitalize()

#     return f"{f_name} {l_name}"


# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year) and month == 2:
#       return 29
#   return month_days[month - 1]
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# docstrings
# def format_name(first, last):
#     """
#         These are docstrings
#         blah blah
#     """
#     if first == "" or last == "":
#         return "You didn't provide valid inputs"
    
#     f_name = first.capitalize()
#     l_name = last.capitalize()

#     return f"{f_name} {l_name}"

# format_name() # docs visible here


# def add(num1, num2):
#     return num1 + num2

# def multiply(num1, num2):
#     return num1 * num2

# add(2, 2)
# multiply(4, 4)

# result = add(2, 2) + multiply(4, 4)

# print(result)

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y


# while True:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter last number: "))
#     choice = input("Type '+', '-', '*', '/': ")
    
#     if choice == '+':
#         result = add(num1, num2)
        
#     print(result)