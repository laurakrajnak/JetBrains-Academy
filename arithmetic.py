# write your code here
# write your code here
from random import randint


def simple_oper():
    a = randint(2, 9)
    b = randint(2, 9)
    oper_list = ['+', '-', '*']
    oper_index = randint(0, 2)
    oper = oper_list[oper_index]
    if oper == '+':
        print(int(a), '+', int(b))
        return int(a) + int(b)
    elif oper == '-':
        print(int(a), '-', int(b))
        return int(a) - int(b)
    elif oper == '*':
        print(int(a), '*', int(b))
        return int(a) * int(b)


def squares_s():
    s = randint(11, 29)
    return s


def first_msg():
    print('''
    Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
    choice = int(input())
    return choice


def score():
    print(f'Your mark is {n}/5. Would you like to save the result? Enter yes or no.')
    save = input()
    save_list = ['yes', 'YES', 'y', 'Yes']
    if save in save_list:
        results = open('results.txt', 'a')
        print('What is your name?')
        name = input()
        results.write(f'{name}: {n}/5 in level {user_choice} ({level_description}).')
        print('The results are saved in "results.txt".')
    else:
        exit()


user_choice = first_msg()
if user_choice == 1:
    level_description = 'simple operations with numbers 2-9'
    n = 0
    num = 5
    for i in range(num):
        calc = simple_oper()
        incorrect = 1
        while incorrect == 1:
            answer = input()
            try:
                if int(answer):
                    if int(answer) == calc:
                        print('Right!')
                        n += 1
                        incorrect = 0
                    else:
                        print('Wrong!')
                        incorrect = 0
            except ValueError:
                print('Wrong format! Try again.')
    score()
elif user_choice == 2:
    level_description = 'integral squares of 11-29'
    n = 0
    num = 5
    for i in range(num):
        sq = squares_s()
        print(sq)
        incorrect = 1
        while incorrect == 1:
            answer = input()
            try:
                if int(answer):
                    if int(answer) == sq*sq:
                        print('Right!')
                        n += 1
                        incorrect = 0
                    else:
                        print('Wrong!')
                        incorrect = 0
            except ValueError:
                print('Wrong format! Try again.')
    score()
else:
    print('Incorrect format.')

