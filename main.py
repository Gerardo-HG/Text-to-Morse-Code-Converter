# Dictionary that maps alphabetical, numeric characters and symbols to their corresponding Morse code
alphabet__numbers_simbols_to_morse={
    'A':".-",'B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....'
    ,'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','Ñ':'--.--','O':'---'
    ,'P':'.--.','Q':"--.-","R":'.-.',"S":"...","T":"-","U":"..-","V":"...-","W":".--"
    ,"X":"-..-","Y":"-.-","Z":"--..",'0':'-----','1':'.----','2':'..---','3':'...--'
    ,'4':'....-','5':'.....','6':'–....','7':'––...','8':'---..','9':'––––.'
    ,'.':'.-.-.-','?':'..--..',',':'--..--'
}

def codify_text(phrase):
    """
    Convert a text phrase to Morse code.

    Args:
        phrase (str): The phrase to convert to Morse code. The text will be converted to uppercase and spaces will not be encoded.

    Returns:
        str: The Morse code representation of the phrase, with a space between each symbol.
    """
    letter_or_num = list(phrase.upper().strip())    # Convert the phrase to uppercase and remove leading/trailing spaces
    output_list = []    # List to store the Morse code symbols
    for i in letter_or_num:
        if i in alphabet__numbers_simbols_to_morse:
            output_list.append(alphabet__numbers_simbols_to_morse[i]+" ")       # Add the Morse code for the character
        else:
            output_list.append(i+" ")       # If the character is not valid, add it as is
    return''.join(output_list)              # Return the complete Morse code as a string

def decodify_text(morse_code):
    """
    Converts a Morse code message into text.

    Args:
        morse_code (str): The Morse code to convert into text, with words separated by three spaces.

    Returns:
        str: The decoded text from the Morse code.
    """

    # Reverse the dictionary to map Morse codes back to characters
    inverse_alphabet_numbers_simbols_to_morse = {v:k for k,v in alphabet__numbers_simbols_to_morse.items()}
    output_list = []                            # List to store the decoded text
    morse_code_words = morse_code.split("   ")      # Split the Morse code into words by three spaces (word separator)


    for word in morse_code_words:
        morse_code_list = word.split(" ")       # Split each word into its Morse code characters
        for i in morse_code_list:
            if i in inverse_alphabet_numbers_simbols_to_morse:
                output_list.append(inverse_alphabet_numbers_simbols_to_morse[i])        # Add the corresponding character

        output_list.append(" ")         # Add a space between words
    return "".join(output_list).strip()         # Return the decoded text and remove any trailing spaces

def show_menu():
    print("""\t Welcome to my Program
         ##### TEXT TO MORSE CODE CONVERTER ####
        """)

    print("""
            These are your options:
         \t1. Codify a phrase.
         \t2. Decodify a morse phrase.
         \t3. Exit.
            """)
    try:
        return int(input('Select a number -> '))
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
        still_continue = True
        while still_continue:
            choice = show_menu()
            if choice == None:
                continue
            elif choice == 1:
                text = input('Enter a phrase to converter morse code:   ')
                print(codify_text(text))
            elif choice == 2:
                morse_text = input('Enter a morse code to converter to text:  ')
                print(decodify_text(morse_text))
            elif choice == 3:
                print('See you soon and Thanks for using this program 🤓🤓🤓 .')
                still_continue=False
            else:
                print("Please enter a valid option.")
main()