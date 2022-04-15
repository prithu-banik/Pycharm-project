# Exercise 2

f1 = int(input('Enter the first number: '))
f2 = int(input('Enter the second number: '))
op = input('?: ')


def f_c():
    while True:
        if f1 == 45 and f2 == 3 and op == 'f':
            return f1 * f2 * 3
        elif f1 == 56 and f2 == 9 and op == 'f':
            return f1 + f2 + 9
        elif f1 == 56 and f2 == 6 and op == 'f':
            return f1 / f2 + 34
        elif op == '+':
            return f1 + f2
        elif op == '-':
            return f1 - f2
        elif op == '*':
            return f1 * f2
        elif op == "/":
            return f1 / f2
        else:
            pass


xm = f_c()
print(xm)

print('please, run the program again')

