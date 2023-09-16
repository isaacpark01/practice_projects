import random, sys 
JAPANESE_NUMBERS = {
    1: "ICHI", 2: "NI", 3: "SAN", 4: "SHI", 5: "GO", 6: "ROKU"
}

purse = 5000

while True:
    #place your bet
    
    while True:
        print('You have', purse, 'mon. how mcuh do you bet? or quit')
        pot = input('> ')
        if pot.upper() == "QUIT":
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enought to make that bet.')
        else:
            #this is a valid bet.
            pot = int(pot)
            break
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print('the dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the flor, still covering the dice and ask for your bet.')
        print()
        print('Cho is and han is odd?')

        while True:
            bet = input('> ').upper()
            if bet != 'CHO' and bet != 'HAN':
                print('Please enter either "CHO" or "HAN" ')
                continue
            else:
                break
        print('the dealer lifts the cup to reveal:')
        print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])

        print('   ', dice1, '-', dice2)

        #determine if the player won 
        rollIsEven = (dice1+dice2) %2 == 0

        if rollIsEven:
            correctBet = "CHO"
        else:
            correctBet = "HAN"
        
        playerWon = bet == correctBet 

        if playerWon:
            print('You won! You take', pot, 'mon.')
            purse = purse + pot 
            print("The hosue collects a", pot // 10, "mon fee.")
            purse = purse - (pot//10)
        else:
            purse = purse - pot
            print('You lost!')

        if purse == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()    
        