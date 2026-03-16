# UC9 – Display Final Gambling Statistics

import random

stake = 100
goal = 200
bet_amount = 1

total_bets = 0
wins = 0
losses = 0

while stake > 0 and stake < goal:

    bet_result = random.randint(0, 1)
    total_bets += 1

    if bet_result == 1:
        stake += bet_amount
        wins += 1
    else:
        stake -= bet_amount
        losses += 1

win_percentage = (wins / total_bets) * 100
loss_percentage = (losses / total_bets) * 100

print("----- Gambling Statistics -----")
print("Final Stake:", stake)
print("Total Bets:", total_bets)
print("Total Wins:", wins)
print("Total Losses:", losses)
print("Win Percentage:", win_percentage, "%")
print("Loss Percentage:", loss_percentage, "%")