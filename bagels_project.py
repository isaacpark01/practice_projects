import random


NUM_DIGITS = 3 
MAX_GUESSES = 10 
def main():
    print(''' I am thinking of a {} -digit number with no repeated digits. Try to guess what it is. here are some clues:
    whien i say: that means' 
    Pico   ONe digit is correct but in the wrong position.
    Fermi One digit is correct and in the right positon. 
    Bagels   No digit is correct.
    for example, if the secret number was 248 and your guess 843, the clues would be Fermi PIc. '''.format(NUM_DIGITS))

    while True: #main game loop.
    #This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1 
        while numGuesses <= MAX_GUESSES:
            guess = ''

        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('guess #{}: '.format(numGuesses))
            guess = input('> ')

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            break #they are correct, sobreak out of this loop.
        if numGuesses > MAX_GUESSES:
            print('you rang out of guesses.')
            print('the answer was {}. '.format(secretNum))

    #ask player if they want to play again.
        print('Do you want to play again? (yes or nO)')
        if not input('> ').lower().startswith('y'):
            break

    print('thanks for playing!')

def getSecretNum():
    """Returns a string amde up of Num_digits unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)
# Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """returns a string with the pic, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'you got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        #Sort the clues into alphabetical order so their original order doesn't give information away. 
        clues.sort()
        #Make a single string from the list of string clues. 
        return ' '.join(clues)

if __name__ == '__main__':
    main()