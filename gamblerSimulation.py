# UC4 – Repeat Betting Until Stake Reaches Goal or Zero

import random

stake = 100
goal = 200
bet_amount = 1

while stake > 0 and stake < goal:

    bet_result = random.randint(0, 1)

    if bet_result == 1:
        stake += bet_amount
    else:
        stake -= bet_amount

print("Final Stake:", stake)

if stake == goal:
    print("Gambler reached the goal!")
else:
    print("Gambler went broke.")