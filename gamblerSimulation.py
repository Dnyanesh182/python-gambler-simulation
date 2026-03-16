# UC10 – Allow Multiple Gambling Simulations Using Loop

import random

while True:

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

    print("\n----- Gambling Simulation Result -----")
    print("Final Stake:", stake)
    print("Total Bets:", total_bets)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Win Percentage:", win_percentage, "%")
    print("Loss Percentage:", loss_percentage, "%")

    choice = input("\nRun another simulation? (yes/no): ").lower()

    if choice != "yes":
        print("Simulation ended.")
        break