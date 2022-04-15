# Exercise 4

print('                   Star Pattern Printing         ')

row = int(input('How many rows do you want'))
bool_val = input('Type 1 for True or for False')

if bool_val == '1':
    for i in range(0, row+1):
        print('*' * i)
elif bool_val == '0':
    for p in range(row, 0, -1):
        print('*' * p)







