# Exercise 3

print('                         ...Welcome to the guessing game...        ')

secret_number = 25
number_of_guesses = 1


while number_of_guesses <= 9:
    guess_number = int(input('Enter your number: '))
    if guess_number < 25:
        print('You have entered a smaller number\nplease enter a larger number')
    elif guess_number > 25:
        print('You have entered a larger number\nplease enter a smaller number\n')
    else:
        print('Yay!! You have won\n')
        print(f'You took {number_of_guesses} guesses to win')
        break
    print(9 - number_of_guesses, "left\n")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses > 9:
    print('Game over!')
print('Please run the program again')

