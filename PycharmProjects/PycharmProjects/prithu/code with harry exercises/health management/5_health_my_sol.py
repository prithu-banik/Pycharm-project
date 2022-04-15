import datetime


def get_date():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        p = int(input('1 for exe and 2 for food'))
        if p == 1:
            val = input('Type what You did today.. ')
            with open('prithu_exercise.txt', 'a') as pr:
                pr.write(str([str(get_date())]) + ': ' + val + '\n')
        if p == 2:
            val = input('Type what You ate today.. ')
            with open('prithu_diet.txt', 'a') as pr:
                pr.write(str([str(get_date())]) + ': ' + val + '\n')
    if k == 2:
        p = int(input('1 for exe and 2 for food'))
        if p == 1:
            val = input('Type what You did today.. ')
            with open('rubayet_exercise.txt', 'a') as pr:
                pr.write(str([str(get_date())]) + ': ' + val + '\n')
        if p == 2:
            val = input('Type what You ate today.. ')
            with open('rubayet_diet.txt', 'a') as pr:
                pr.write(str([str(get_date())]) + ': ' + val + '\n')
    if k == 3:
        p = int(input('1 for exe and 2 for food'))
        if p == 1:
            val = input('Type what You did today.. ')
            with open('raihan_exercise.txt', 'a') as pr:
                pr.write(str([str(get_date())]) + ': ' + val + '\n')
        if p == 2:
            val = input('Type what You ate today.. ')
            with open('raihan_diet.txt', 'a') as pr:
                pr.write(str([str(get_date())]) + ': ' + val + '\n')
    else:
        print('Please enter a valid value (1(harry),2(rohan),3(hammad)')


def retrieve(k):
    if k == 1:
        p = int(input('1 for food and 2 for exe'))
        if p == 1:
            with open('prithu_diet.txt', 'r') as pr:
                for i in pr:
                    print(i, end=' ')
        elif p == 2:
            with open('prithu_exercise.txt', 'r') as pr:
                for i in pr:
                    print(i, end=' ')
    if k == 2:
        p = int(input('1 for food and 2 for exe'))
        if p == 1:
            with open('rubayet_diet.txt', 'r') as pr:
                for i in pr:
                    print(i, end=' ')
        elif p == 2:
            with open('rubayet_exercise.txt', 'r') as pr:
                for i in pr:
                    print(i, end=' ')
    if k == 3:
        p = int(input('1 for food and 2 for exe'))
        if p == 1:
            with open('raihan_diet.txt', 'r') as pr:
                for i in pr:
                    print(i, end=' ')
        elif p == 2:
            with open('raihan_exercise.txt', 'r') as pr:
                for i in pr:
                    print(i, end=' ')
    else:
        print('Please enter a valid value ((harry),(rohan),(hammad)')


print('         Health Management    ')

a = int(input('Type 1 for take and 2 for retrieve'))

if a == 1:
    b = int(input('Press 1 for Prithu, 2 for Rubayet, 3 for Raihan'))
    take(b)
else:
    b = int(input('Press 1 for Prithu, 2 for Rubayet, 3 for Raihan'))
    retrieve(b)
