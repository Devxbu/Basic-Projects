import time, sys


def game():
    i = 0
    while True:
        print(i)
        time.sleep(1)
        x = input("Number: ")
        if (i + 1) % 5 == 0 and x.lower == 'boom':
            time.sleep(1)
            print(x)
        elif (i + 1) % 5 != 0 and x.lower != 'boom':
            time.sleep(1)
            print(x)
        else:
            print('Wrong!')
            sys.exit()

game()