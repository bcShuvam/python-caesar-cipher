# Name: Shuvam BC
# Student Id: NP02CS4A240020

import os

def welcome():
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
    return os.path.isfile(filename)

def write_message(messages):
    with open('results.txt', 'w') as file:
        for msg in messages:
            file.write(f'{msg}\n')
    print('Output written to results.txt')
    

def message_or_file():
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

if __name__ == '__main__':
    welcome()
    message_or_file()