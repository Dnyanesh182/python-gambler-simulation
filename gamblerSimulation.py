# UC2 – Simulate a Single Bet (Win or Loss)

import random

stake = 100
goal = 200
bet_amount = 1

bet_result = random.randint(0, 1)

if bet_result == 1:
    print("Gambler wins the bet")
else:
    print("Gambler loses the bet")