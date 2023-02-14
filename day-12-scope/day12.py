# # global scope
# enemies = 1

# def increase_enemies():
#     # local scope
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")
    

# increase_enemies()
# print(f"Enemies outside function: {enemies}")


# # there is no block scope
# if 3 > 2:
#     a_variable = 10
    
    

# modifying global scope
enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    return enemies
  
increase_enemies()  
print(enemies)


# global constants
PI = 3.14159

