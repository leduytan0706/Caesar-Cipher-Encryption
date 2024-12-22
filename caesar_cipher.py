FIRST_CHAR_CODE_UPPER = 65
LAST_CHAR_CODE_UPPER = 90
FIRST_CHAR_CODE_LOWER = 97
LAST_CHAR_CODE_LOWER = 122
CHAR_RANGE = 26



def caesar_encrypt(message, shift):
    # encryption result 
    code=""
    # Go through each of the characters in the message
    for char in message:
        if char.isalpha():
            # convert the character to ASCII code
            char_ascii = ord(char)
            new_char_ascii = char_ascii + shift

            if (char_ascii <= 90):
                # new_char_ascii - FIRST_CHAR_CODE_UPPER: get the distance
                # % CHAR_RANGE: get the position (index)
                # + FIRST_CHAR_CODE_UPPER: get the new ASCII code
                new_char_ascii = ((new_char_ascii - FIRST_CHAR_CODE_UPPER) % CHAR_RANGE) + FIRST_CHAR_CODE_UPPER 

            elif (char_ascii >= 97):
                new_char_ascii = ((new_char_ascii - FIRST_CHAR_CODE_LOWER) % CHAR_RANGE) + FIRST_CHAR_CODE_LOWER 

            new_char = chr(new_char_ascii)

            code += new_char

            # print(char, char_ascii, new_char_ascii, new_char)

        else:
            code += char

    print(code)

caesar_encrypt("Hello, World!", 7)
caesar_encrypt("Boy, it's not THAT complicated!", 13)


