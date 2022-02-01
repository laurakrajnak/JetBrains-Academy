# write your code here
print('Enter the number of friends joining (including you):')
number = int(input())

names = {}
if number < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line: ')
    for i in range(number):
        name = input()
        names[name] = 0

    print(names)
