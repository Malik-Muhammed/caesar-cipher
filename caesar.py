
alphabet = ["a", "b", "c", "d", "e",
            "f", "g", "h", "i", "j",
            "k", "l","m", "n", "o",
            "p", "q", "r", "s","t", 
            "u", "v", "w", "x", "y",
            "z"
            ]

def caesar(user_particular_task, user_text, user_shift_number):

    caesar_text = ""

    if user_particular_task == "decode":
        user_shift_number = -user_shift_number

    for eachChar in user_text:

        if eachChar in alphabet:
            index = (alphabet.index(eachChar) + user_shift_number) % len(alphabet)
            caesar_text += alphabet[index]
        else:
            caesar_text += eachChar


      
    print(f"The {user_task}d text is {caesar_text}")


continuity_determinant = True

while continuity_determinant:

    user_task = input("Type 'encode' to encrypt, type 'decode' to decrypt:")

    text = input("Type your message: ").lower()

    shift_number = int(input("Type the shift number: "))


    caesar(user_task, text, shift_number)

    continuity_determinant_que = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")

    if continuity_determinant_que == "no":
        continuity_determinant = False
    print("Goodbye")