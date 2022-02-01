# write your code here
s = '         '
count = 0
winner = 0
o_win = 0
x_win = 0
impossible = 1
print('---------')
print('| ' + '     ' + ' |')
print('| ' + '     ' + ' |')
print('| ' + '     ' + ' |')
print('---------')

grid = [[s[0], s[1], s[2]],
        [s[3], s[4], s[5]],
        [s[6], s[7], s[8]]]


def user():
    row, col = input('Enter the coordinates: ').split()  # user's input
    if not row.isdigit() and col.isdigit():
        print('You should enter numbers!')
    else:
        row = int(row) - 1
        col = int(col) - 1
        if not 0 <= row <= 2 or not 0 <= col <= 2:
            print('Coordinates should be from 1 to 3!')
            user()
        elif grid[row][col] != ' ':
            print('This cell is occupied! Choose another one!')
            user()
        else:
            if count % 2 == 1:
                grid[row][col] = 'X'
            elif count % 2 == 0:
                grid[row][col] = 'O'
            print('---------')
            print('| ' + grid[0][0], grid[0][1], grid[0][2] + ' |')
            print('| ' + grid[1][0], grid[1][1], grid[1][2] + ' |')
            print('| ' + grid[2][0], grid[2][1], grid[2][2] + ' |')
            print('---------')


while winner == 0:
    big_grid = grid[0] + grid[1] + grid[2]
    if ' ' in big_grid:
        user()
        big_grid = grid[0] + grid[1] + grid[2]
        count += 1

        x_num = [x for x in s if x == 'X']
        o_num = [o for o in s if o == 'O']

        if (len(x_num) + len(o_num)) == (2 * len(x_num)):
            impossible = 0
        # if len(x_num) > len(o_num) + 1 or len(x_num) < len(o_num) + 1:
        elif len(x_num) + len(o_num) == 2 * len(x_num) + 1:
            impossible = 0
        elif len(x_num) + len(o_num) == (2 * len(x_num)) - 1:
            impossible = 0

        if impossible == 1:
            print('Impossible')

        for i in range(3):
            if big_grid[0 + 3*i] == big_grid[1 + 3*i] == big_grid[2 + 3*i]:  # rows
                if big_grid[0 + 3*i] == 'O':
                    o_win = 1
                    if x_win == 1 and o_win == 1:
                        print('Impossible')
                elif big_grid[0 + 3*i] == 'X':
                    x_win = 1
                    if x_win == 1 and o_win == 1:
                        print('Impossible')
                if not x_win == o_win == 1 and big_grid[0 + 3*i] != ' ':
                    print(big_grid[0 + 3*i], 'wins')
                    winner = 1
            elif big_grid[0 + i] == big_grid[3 + i] == big_grid[6 + i]:  # columns
                if big_grid[0 + i] == 'O':
                    o_win = 1
                    if x_win == 1 and o_win == 1:
                        print('Impossible')
                elif big_grid[0 + i] == 'X':
                    x_win = 1
                    if x_win == 1 and o_win == 1:
                        print('Impossible')
                if not x_win == o_win == 1 and big_grid[0 + i] != ' ':
                    print(big_grid[0 + i], 'wins')
                    winner = 1

        print(big_grid, 'check')
        if big_grid[0] == big_grid[4] == big_grid[8] or big_grid[4] == big_grid[6] == big_grid[2]:  # diagonally
            print('first works')
            if big_grid[4] != ' ':
                print('second works')
                print(big_grid[4], 'wins')
                winner = 1
    else:
        if winner == 0:
            print('Draw')
            winner = 1
