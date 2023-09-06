import random, time

def game(round = 1):
    while round > 0:
        user = input('Heads or Tails (Heads: 1 Tails: 0) ')
        if user not in ["0","1"]:
            raise ValueError("Please try again")
        coin = random.choice('0 1')
        points = 0
        if user == coin:
            points += 1
            print('Correct!')
            round -= 1
            time.sleep(1)
        else:
            print('Incorrect!')
            round -= 1
            time.sleep(1)
    print(f'Game is over here is your points: {points}')

try:
    game(2)
except Exception as ex:
    print(ex)