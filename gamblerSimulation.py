# UC3 – Update Stake Based on Win or Loss

import random

stake = 100
goal = 200
bet_amount = 1

bet_result = random.randint(0, 1)

if bet_result == 1:
    stake += bet_amount
    print("Gambler wins the bet")
else:
    stake -= bet_amount
    print("Gambler loses the bet")

print("Updated Stake:", stake)