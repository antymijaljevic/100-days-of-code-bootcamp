# dictionary

# {"key":"value"}

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again"
# }


# # retrieving items
# print(programming_dictionary["Bug"])

# # adding items
# programming_dictionary["ForLoop"] = "similar to while loop"

# # create an empty dictionary or wipe an existing dictionary
# new_dictionary = {}

# # edit an item
# programming_dictionary["Bug"] = "a new value for Bug key"

# # loop through a dictionary (will give keys)
# for thing in programming_dictionary:
#     print(thing)

# # print values
# for key in programming_dictionary:
#     print(programming_dictionary[key])

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] >= 91:
#         student_grades[key] = "Outstanding"    
#     elif student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# # nesting a list in a dict
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }


# # nesting a dict into a dict
# travel_log = {
#     "France": {"Visited_cities": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_I_like": ["Berlin", "Hamburg", "Stuttgart"], "cities_I_donot": ["Cologne"]}
# }

# # nesting dict in a list
# travel_log = [
#     {
#         "Country": "France", 
#         "Visited_cities": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "Country": "Germany", 
#         "Cities_I_like": ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 13
#     }
# ]


# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     travel_log.append({"country": country, "visits": visits, "cities": cities })

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)