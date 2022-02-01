# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

index_list = [msg_10, msg_11, msg_12]

count = 0
memory = 0
result = 0


def is_one_digit(v):
    if -10 < int(v) < 10 and v == int(v):
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ''
    digit1 = is_one_digit(v1)
    digit2 = is_one_digit(v2)
    if digit1 is True and digit2 is True:
        msg = msg + msg_6  # lazy
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7  # very lazy
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8  # very vey lazy
    if msg != '':
        msg = msg_9 + msg  # you are
    print(msg)


while count != 1:
    x, o, y = input(msg_0 + ' ').split(' ')
    try:
        if x == 'M':  # memory cast
            x = float(memory)
        if y == 'M':
            y = float(memory)

        x = float(x)
        y = float(y)

        if o == '+' or o == '-' or o == '*' or o == '/':
            check(x, y, o)
            count = count + 1  # count = 1
            if o == '+':
                result = x + y
                print(result)
            elif o == '-':
                result = float(x) - float(y)
                print(result)
            elif o == '*':
                result = x * y
                print(result)
            elif o == '/':
                if y != 0:
                    result = x / y
                    print(result)
                else:
                    print(msg_3)  # nedeli sa nulou
                    count = count - 1
            else:
                print(msg_2)
                count = count - 1

        if count == 1:
            count2 = 0
            while count2 < 1:  # 4 a 5 msg
                count2 = count2 + 1
                answer4 = input(msg_4 + ' ')  # memory y/n

                if answer4 == 'y':
                    count4 = 0
                    count10 = 0

                    if is_one_digit(result) is True:
                        msg_index = 10

                        list_count = 0
                        while count10 != 1:
                            count10 = count10 + 1

                            if msg_index == 10:
                                list_count = 0
                            elif msg_index == 11:
                                list_count = 1
                            elif msg_index == 12:
                                list_count = 2

                            answer10 = input(index_list[list_count])
                            if answer10 == 'y':
                                if msg_index < 12:
                                    msg_index = msg_index + 1
                                    count10 = count10 - 1
                                else:
                                    memory = result
                            elif answer10 == 'n':
                                pass
                            elif answer10 != 'n':
                                count10 = count10 - 1
                    else:
                        memory = result

                    while count4 != 1:
                        answer5 = input(msg_5 + ' ')
                        count4 = count4 + 1
                        if answer5 == 'y':  # count again y/n
                            count = count - 1
                        elif answer5 == 'n':
                            exit()
                        else:  # je potrebne sa vratit na msg_5
                            count4 = count4 - 1
                elif answer4 == 'n':
                    count3 = 0
                    while count3 != 1:
                        answer5 = input(msg_5 + ' ')
                        count3 = count3 + 1
                        if answer5 == 'y':
                            count = count - 1
                        elif answer5 == 'n':
                            exit()
                        else:
                            count3 = count3 - 1
                else:
                    count2 = count2 - 1

    except ValueError:
        print(msg_1)
        count = count - 1
