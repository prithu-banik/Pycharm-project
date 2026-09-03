import random

lst = ['s', 'w', 'g']

print('      \twelcome to the Snake Game     ')
print('          \tYou have 9 chances             ')


chance = 10
no_chance = 0
human_points = 0
computer_points = 0

while no_chance < chance:
    human_choice = input('  \tchoose s for Snake, w for Water, g for Gun\n\n')
    computer_choice = random.choice(lst)
    if human_choice == computer_choice:
        print('Tie, both choices are the same\n')
    elif human_choice == 'w' and computer_choice == 's':
        computer_points = computer_points + 1
        print('Snake has drunk the water')
        print(f'Your choice is {human_choice} and computer choice is {computer_choice}')
        print(f'your point is {human_points} and computer point is {computer_points}')
        print('Computer wins 1 point\n')
    elif human_choice == 'g' and computer_choice == 'w':
        computer_points = computer_points + 1
        print('Gun has been washed away by water')
        print(f'Your choice is {human_choice} and computer choice is {computer_choice}')
        print(f'your point is {human_points} and computer point is {computer_points}')
        print('Computer wins 1 point\n')
    elif human_choice == 's' and computer_choice == 'g':
        print("Gun has killed the snake")
        computer_points = computer_points + 1
        print(f'Your choice is {human_choice} and computer choice is {computer_choice}')
        print(f'your point is {human_points} and computer point is {computer_points}')
        print('Computer wins 1 point\n')
    elif human_choice == 'g' and computer_choice == 's':
        print("Gun has killed the snake")
        human_points = human_points + 1
        print(f'Your choice is {human_choice} and computer choice is {computer_choice}')
        print(f'your point is {human_points} and computer point is {computer_points}')
        print('Computer wins 1 point\n')
    elif human_choice == 'w' and computer_choice == 'g':
        print("'Gun has been washed away by water")
        human_points = human_points + 1
        print(f'Your choice is {human_choice} and computer choice is {computer_choice}')
        print(f'your point is {human_points} and computer point is {computer_points}')
        print('Computer wins 1 point\n')
    elif human_choice == 's' and computer_choice == 'w':
        print("Snake has drunk the water")
        human_points = human_points + 1
        print(f'Your choice is {human_choice} and computer choice is {computer_choice}')
        print(f'your point is {human_points} and computer point is {computer_points}')
        print('Computer wins 1 point\n')
    else:
        print('Input a valid value (s, w, g)')

    no_chance = no_chance + 1
    print(f'{chance - no_chance} is left out of {chance}')

print("Game over")

if human_points > computer_points:
    print(f'You have got {human_points} points and the computer have got {computer_points} point')
    print('The user has won!!')
elif human_points < computer_points:
    print(f'You have got {human_points} points and the computer have got {computer_points} point')
    print('The computer has won')
elif human_points == computer_points:
    print(f'You have got {human_points} points and the computer have got {computer_points} point')
    print('It is a tie, no one has one')
else:
    print('Nothing has happened maybe there is an unusual problem')
