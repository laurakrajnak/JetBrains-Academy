def machine_has(w, m, b, c, money):
    print(f'''The coffee machine has:
{w} of water
{m} of milk
{b} of coffee beans
{c} of disposable cups
${money} of money''')


def action_func():
    print()
    print('Write action (buy, fill, take, remaining, exit):')
    user = input()
    print()
    return user


w = 400
m = 540
b = 120
c = 9
money = 550

while True:
    action = action_func()
    if action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        buy_user = input()
        if buy_user != 'back':
            buy_user = int(buy_user)
            if buy_user == 1:
                w -= 250
                b -= 16
                c -= 1
                money += 4
            elif buy_user == 2:
                w -= 350
                m -= 75
                b -= 20
                c -= 1
                money += 7
            elif buy_user == 3:
                w -= 200
                m -= 100
                b -= 12
                c -= 1
                money += 6

            if w > 0 and m > 0 and b > 0 and c > 0:
                print('I have enough resources, making you a coffee!')
            else:
                if w < 0:
                    print('Sorry, not enough water!')
                    if buy_user == 1:
                        w += 250
                        b += 16
                        c += 1
                        money -= 4
                    elif buy_user == 2:
                        w += 350
                        m += 75
                        b += 20
                        c += 1
                        money -= 7
                    elif buy_user == 3:
                        w += 200
                        m += 100
                        b += 12
                        c += 1
                        money -= 6

    elif action == 'fill':
        print('Write how many ml of water you want to add:')
        w += int(input())
        print('Write how many ml of milk you want to add:')
        m += int(input())
        print('Write how many grams of coffee beans you want to add:')
        b += int(input())
        print('Write how many disposable coffee cups you want to add:')
        c += int(input())
    elif action == 'take':
        print(f'I gave you ${money}')
        money = 0
    elif action == 'remaining':
        machine_has(w, m, b, c, money)
    elif action == 'exit':
        exit()
