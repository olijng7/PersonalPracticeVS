print('***Caesar Cypher Message Encryption/Decryption***')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt():
    key = int(input('What is the key? '))
    message = input('Please enter a message to encrypt: ')
    newMessage = ''
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    print('Your encrypted message is: ', newMessage)
    again()

def decrypt():
    have = input('Do you have a key? (y/n) ')
    newMessage = ''
    if have == 'y':
        key = int(input('What is the key? '))
        message = input('Please enter a message to decrypt: ')
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                newPosition = (position - key) % 26
                newCharacter = alphabet[newPosition]
                newMessage += newCharacter
            else:
                newMessage += character
        print('Your decrypted message is: ', newMessage)
        again()
    elif have == 'n':
        message = input('Please enter a message to decrypt: ')
        print('Here are your decrypted messages: ')
    else:
        decrypt()
    def findLetter():
        newMessage = ''
        num = 0
        while num != 25:
            num += 1
            for character in message:
                if character in alphabet:
                    position = alphabet.find(character)
                    newPosition = (position - num) % 26
                    newCharacter = alphabet[newPosition]
                    newMessage += newCharacter
                else:
                    newMessage += character
            print(newMessage)
            newMessage = ''
        again()
    findLetter()

def again():
    again = input('Would you like to encrypt/decrypt again? (y/n) ')
    if again == 'y':
        while True:
            start()
    else:
        exit()

def start():
    choice = input('Encryption or decryption? (e/d) ')
    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()
start()
