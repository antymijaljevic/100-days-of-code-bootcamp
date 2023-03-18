# reading from file

# # old method
# file = open("my-file.txt")
# content = file.read()
# print(content)
# file.close() # saves ram memory

# better method
with open("my-file.txt") as file: # read
    content = file.read()
    print(content)
      
# writing to file
with open("my-file.txt", mode="w") as file: # mode read-only by default
    file.write("ojala!")
    
# writing to file
with open("my-file.txt", mode="a") as file: # append
    file.write("\nojala!")
    
# create a new file
with open("new-file.txt", mode="w") as file:
    file.write("meh..")