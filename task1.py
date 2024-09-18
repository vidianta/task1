import random
number = random.randint(1, 100)
attempt = 0
print(number)

print('\n\tWELLCOME TO NUMBER GUESSER')

print('Guess the random number from 1 to 100 and each guess would give you hints if your guess is higher or lower then the number')

while attempt < 3:
    if attempt == 0:
        print('please pick your first guess')
        answer =int(input())
        attempt += 1
        if answer == number:
            print('your guess of {} is CORRECT!!!!'.format(answer))
            break
        else:
            if answer < number:
                print('\nTHINK BIGGER')
            elif answer > number:
                print('\nGO SMALLER!!!!')
            print('your guess is incorect please try again')
    else:
        print('\nplease type your next guess!!!')
        answer = int(input())
        attempt += 1
        if answer == number:
            print('\nAMAZING {} IS CORRECT'.format(answer))
            break
        else:
            if attempt < 3:
                if answer < number:
                    print('your guess is still TOOO SMALLL')
                elif answer > number:
                    print('WAYYYY TO BIGGGG BRO')
                print('your guess is STILL INCORRECT TRY AGAIN')
            elif attempt == 3:
                print('\nALL LIVES USED, YOU FAILED. THE NUMBER WAS {}'.format(number))
