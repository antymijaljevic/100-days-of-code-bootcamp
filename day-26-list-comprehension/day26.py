numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

name = "Anglea"
new_list = [letter for letter in name]
print(new_list)

double_it = [number * 2 for number in range(1, 5)]
print(double_it)

names = ["Ante", "Mike", "Zuzu", "Pero", "Vesna", "Xuxuxux"]
short_names = [x for x in names if len(x) < 5]
print(short_names)

cap_names = [y.upper() for y in short_names]
print(cap_names)



# exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
#Write your 1 line code 👇 below:
squared_numbers = [num * num for num in numbers]
#Write your code 👆 above:
print(squared_numbers)


# exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
#Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 == 0]
#Write your code 👆 above:
print(result)


# exercise 3
with open("file1.txt") as file1:
    # file_1_list = [line.strip() for line in file1]
    file_1_list = file1.readlines()
    
with open("file2.txt") as file2:
    file_2_list = file2.readlines()
    

result = [int(num) for num in file_1_list if num in file_2_list]

# Write your code above 👆
print(result)