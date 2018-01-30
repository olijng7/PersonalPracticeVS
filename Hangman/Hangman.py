print("Welcome to hangman! V")
print('-----------------------')

import getpass
word = getpass.getpass("What's the word? ")
for character in word:
    answer = word
    print('_ ', end='')

print("")
print("Ok, let's go!")
print('-------')
print('|     |')
print('|')
print('|')
print('|')
print('|')
print('-------')

def guess():
    letter = input('Guess a letter. ')
    return letter
guess = guess()

def findLetter(word):
    if guess in word:
        print(guess + ' is in the word!')
        character.find(word)
        if character == guess:
            print(guess, end='')
        else:
            print('_ ', end='')
        print('')
        guess()
    else:

findLetter(word)
