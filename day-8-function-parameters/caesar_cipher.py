from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(input_text, shift_num, cipher_direction):
    processed_text = ""
    
    if cipher_direction == "decode":
        shift_num *= -1
    
    for letter in input_text:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            cipher_index = letter_position + shift_num
            processed_text += alphabet[cipher_index]
        else:
            processed_text += letter
            
    print(f"The {cipher_direction}d text is: {processed_text}\n")

print(logo)

stop = True
while stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    cipher(input_text=text, shift_num=shift, cipher_direction=direction)
    
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no' to quit\n").lower()
    if user_input == "no":
        stop = False
        print("Program terminated!")
        
    
    
    