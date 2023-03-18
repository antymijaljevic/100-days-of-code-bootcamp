# # absoulte path
# /home/some_user/Desktop/Courses/100-days-of-code-bootcamp/day-24-files-directories-paths/absolute-relative-path/main.py

# # relative path
# day-24-files-directories-paths/absolute-relative-path

# # current working directory to file
# ./absolute-relative-path/main.py

# # one directory back and file within
# ../report.pp

# # run file within current working directory
# ./main.py or main.py

with open("/home/amijaljevic/Desktop/file.txt") as file:
    a = file.read()
    print(a)
    
with open("./file.txt") as file:
    a = file.read()
    print(a)
    
with open("file.txt") as file:
    a = file.read()
    print(a)
    
with open("../../../../file.txt") as file:
    a = file.read()
    print(a)