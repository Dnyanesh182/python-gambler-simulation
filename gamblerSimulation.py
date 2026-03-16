# UC5 – Count Total Number of Bets Made

import random

stake = 100
goal = 200
bet_amount = 1

total_bets = 0

while stake > 0 and stake < goal:

    bet_result = random.randint(0, 1)
    total_bets += 1

    if bet_result == 1:
        stake += bet_amount
    else:
        stake -= bet_amount

print("Final Stake:", stake)
print("Total Bets Made:", total_bets)