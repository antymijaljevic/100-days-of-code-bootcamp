# loops

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
    
# print(fruits)


# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# sum_of = 0
# count   = 0

# for height in student_heights:
#     count += 1
#     sum_of += height

# average = round(sum_of / count)
# print(average)

# # 156 178 165 171 187
# # 171


# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# max_score = 0

# for num in student_scores:
#     if num > max_score:
#         max_score = num

# print("The highest score in the class is:", max_score)

# # 78 65 89 86 55 91 64 89
# # 91

# for num in range(1, 11, 2):
#     print(num)

# total = 0
# for num in range(1, 101):
#     total += num
    
# print(total)

# #Write your code below this row 👇
# total = 0
# for num in range(0, 101, 2):
#     total += num

# print(total)

# #Write your code below this row 👇
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
