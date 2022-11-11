
while True:
    num = list(range(1, 101))
    print(num[-1])
    user_input = int(input('введите число от 1 до 100:'))
    for i in num:
        robot = (num[0]+num[-1])//2
        print(robot)
        user_input1 = input('<>=:')
        if user_input1 == '<':
            num = list(range(robot, 101))
        elif user_input1 == '>':
            num = list(range(0, robot))



