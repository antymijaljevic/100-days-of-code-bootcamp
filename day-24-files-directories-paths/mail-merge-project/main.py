#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



letter_dir = "./Input/Letters/starting_letter.txt"
invited_names = "./Input/Names/invited_names.txt"
output_dir = "./Output/ReadyToSend"

def create_letter(content, send_to):
    with open(f"{output_dir}/{send_to}_invite.txt", mode="w") as letter:
        letter.write(content)
        
with open(letter_dir) as file:
    letter_temp = file.read()
    
with open(invited_names) as file:
    for line in file:
        name = line.strip()
        new_letter = letter_temp.replace("[name]", name)
        create_letter(new_letter, name.lower())