# Name: Shuvam BC
# Student Id: NP02CS4A240020

import os

def welcome():
    """
        This welcome function displays welcome message to the user,
        and explains what this program is made for.
    """
    print('Welcome to the Caesar Cipher')
    print('This program encrypts and decrypts text using Caesar Cipher.')

def enter_message():
    mode = ''
    shift = 0
    encryptDecryptAgain = ''
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d) : ')
        if mode in ('e', 'd'):
            break
        else:
            print('Invalid Mode')
    message = input('What message would you like to encrypt: ')
    while True:
        try:
            shift = int(input('What is the shift number: '))
            break
        except ValueError as err:
            print(f'Error: {err}')
    if mode == 'e':
        encrypt(message, shift)
    else:
        decrypt(message, shift)
    # Prompt for another message
    print()
    while True:
        encryptDecryptAgain = input('Would you like to encrypt or decrypt another message? (y/n): ')
        if encryptDecryptAgain in ('y', 'n'):
            if encryptDecryptAgain == 'y':
                message_or_file()
            else:
                print('Thanks for using the program, goodbye!')
                break
        else:
            print('Invalid Choice')

def encrypt(message, shift):
    """
        This function encrypts a message according to the shift number

        Parameters:
            message (str): The message which will be encrypted
            shift (int): The number to shift each character forward of the message
        
        Returns:
            str: The encrypted message
        
        Example:
            >>> encrypt('Hello world', 4)
            'LIPPS ASVPH'
        
        How it works:
            suppose ascii value => ord('H') -> returns 72
            and shift number is 4
            algorithm:
            = ((asciiVal - 65 + shift) % 26) + 65
            = ((72 - 65 + 4) % 26) + 65
            = (11 % 26) + 65
            = 11 + 65
            = 76
            chr(76) -> returns 'L'
    """
    encryptedMsg = ''
    for char in message:
        asciiVal = ord(char)
        # For Uppercase
        shifted = ''
        if 65 <= asciiVal <= 90:
            shifted = ((asciiVal - 65 + shift) % 26) + 65
            encryptedMsg += chr(shifted).upper()
        # For Lowercase
        elif 97 <= asciiVal <= 122:
            shifted = ((asciiVal - 97 + shift) % 26) + 97
            encryptedMsg += chr(shifted).upper()
        # For Non-alphabetic characters
        else:
            encryptedMsg += char
            # print(char, end='')
    return encryptedMsg

def decrypt(message, shift):
    """
        This function decrypts a message according to the shift number.
        It algorithm for decryption is similar as encryption 
        but in decryption instead of adding the shift number we subtract it.

        Parameters:
            message (str): The message which will be decrypted
            shift (int): The number to shift each character backward of the message
        
        Returns:
            str: The encrypted message
        
        Example:
            >>> encrypt('LIPPS ASVPH', 4)
            'HELLO WORLD'
    """
    decryptedMsg = ''
    for char in message:
        asciiVal = ord(char)
        # For Uppercase
        shifted = ''
        if 65 <= asciiVal <= 90:
            shifted = ((asciiVal - 65 - shift) % 26) + 65
            decryptedMsg += chr(shifted).upper()
        # For Lowercase
        elif 97 <= asciiVal <= 122:
            shifted = ((asciiVal - 97 - shift) % 26) + 97
            decryptedMsg += chr(shifted).upper()
        # For Non-alphabetic characters
        else:
            decryptedMsg += char
    return decryptedMsg

def process_file(filename, mode):
    """
        This function reads all the contents from the given filename.
        And calls encrypt() or decrypt() function according to the mode received from parameter.
        Then it will call the write_message(messages) function and pass list of message to it,
        and produce output to result to results.txt file.

        This function will prompt the user to enter shift number again and again,
        and checks if the shift number is an valid integer of not using while loop.

        Parameters:
            filename (str): The name of the file which contains the messages
            mode (str): The mode of operation (e for encrypt, d for decrypt)

        Returns:
            None
        
        Example:
            >>> process_file('input.txt', 'e')
            encrypts all the messages in 'input.txt' and saves them in'results.txt'
    """
    shift = 0
    messageList = []
    with open(filename, 'r') as file:
        while True:
            try:
                shift = int(input('What is the shift number: '))
                break
            except ValueError as err:
                print(f'Error: {err}')
        for line in file:
            message = ''
            line = line.strip()
            for char in line:
                message += char
            if mode == 'e':
                messageList.append(encrypt(message, shift))
            else:
                messageList.append(decrypt(message, shift))
    write_message(messageList)

def is_file(filename):
    """
        This function return boolean value to the user.

        Parameters:
            (str) as filename

        Returns:
            This function uses python's os module to verify if file exists or not.
            It will return True if the file exists and
            returns False if the file doses not exist.
    """
    return os.path.isfile(filename)

def write_message(messages):
    """
        This function writes the list of messages to results.txt file.

        This function requires one parameter as a string or list of strings
        The opens a file named results.txt
    """
    with open('results.txt', 'w') as file:
        for msg in messages:
            file.write(f'{msg}\n')
    print('Output written to results.txt')
    

def message_or_file():
    """
        This function prompts the user to enter values as asked in the console.

        This function uses while loop to check if the user correct input or not,
        and calls the respective functions according to the input values entered by user.

        At the end the function will ask the user to exit or continue cesar cipher the program.
        If the user enters (e) to exit, the program will terminate, 
        and if user enters (y) to continue then it will continue the program.
    """
    mode = ''
    fileName = ''
    readFromFileOrConsole = ''
    message = ''
    shift = 0
    while True:
        mode = input('Would you like to encrypt (e) or decrypt (d) : ')
        if mode in ('e', 'd'):
            break
        else:
            print('Invalid Mode')
    while True:
        readFromFileOrConsole = input('Would you like to read from a file (f) or the console (c)? ')
        if readFromFileOrConsole in ('f', 'c'):
            break
        else:
            print('Invalid Read Option')
    if readFromFileOrConsole == 'f':
        while True:
            fileName = input('Enter a filename: ')
            if is_file(fileName):
                message = process_file(fileName, mode)
                break
            else:
                print('Invalid Filename')
    else:
        message = input('What message would you like to encrypt: ')
        while True:
            try:
                shift = int(input('What is the shift number: '))
                break
            except ValueError as err:
                print(f'Error: {err}')
        if mode == 'e':
            print(encrypt(message, shift))
        else:
            print(decrypt(message, shift))
    print()
    while True:
        encryptDecryptAgain = input('Would you like to encrypt or decrypt another message? (y/n): ')
        if encryptDecryptAgain == 'y':
                message_or_file()
                break
        elif encryptDecryptAgain == 'n':
            print('Thanks for using the program, goodbye!')
            break
        else:
            print('Invalid Choice')

def main():
    """
        This main function is calls welcome and message_or_file() function.
        It will run the whole cesar cipher program.
    """
    welcome()
    message_or_file()

if __name__ == '__main__':
    main()