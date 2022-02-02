# Rock Paper Scissors - by Shubham Singh | github: LiQuiD-404
# No prerequisites required for running this program

import time  # to add a little bit of suspense
import random  # for the computer to play along

options = []


def rand_move():
    ai = ""
    z = random.randint(0, len(options) - 1)
    ai = options[z]
    return ai


print("----------Welcome to Rock Paper Scissors----------")
print("Please enter your name to get started : ")
p1 = input()
f = open("names.txt", 'r')
lines = f.read().split()
p2 = random.choice(lines)
print(f'Welcome {p1} to Rock Paper Scissors')
time.sleep(1)
print("You will be playing against: ")
time.sleep(2)
print(p2)
while True:
    print("Select your preferred difficulty! Please choose carefully as the difficulty cannot be changed during rounds")
    print("1. Newbie Rock Paper Scissors - probability of opponent playing either rock, paper or scissors is "
          "increased to 50%")
    print("2. Standard Rock Paper Scissors - equal probability of rock, paper and scissors")
    print("3. Hard Rock Paper Scissors - probability that the opponent defeats you is 40% ")
    print("4. Extreme Rock Paper Scissors (not recommended) - Either you defeat your opponent or he defeats you ")
    difficulty = int(input())
    if difficulty == 2:
        options = ["ROCK", "PAPER", "SCISSORS"]
    if difficulty == 1:
        options = ["ROCK", "PAPER", "SCISSORS"]
        p = random.randint(0, 2)
        increased = options[p]
        print(f'Probability of the opponent playing {increased} is increased by 50% ')
        options = ["ROCK", increased, increased, "ROCK", increased, "SCISSORS", increased, "PAPER", "SCISSORS",
                   increased]

    win_p1 = 0
    win_p2 = 0
    print("How many rounds do you want to play for? ")
    rounds = int(input())
    print("Dusting up the tables... ")
    time.sleep(2)
    print("-" * 30)
    print(p1 + " V/S " + p2)
    print("-" * 30)
    for i in range(1, rounds + 1):
        print("-" * 50)
        print("ROUND " + str(i) + " Coming up...")
        time.sleep(1)
        p1_move = input(f'Enter your move {p1}: ')
        p1_move = p1_move.upper()
        if difficulty == 4:
            if p1_move == "ROCK":
                p2_move = random.choice(["PAPER", "SCISSORS"])
            if p1_move == "PAPER":
                p2_move = random.choice(["SCISSORS", "ROCK"])
            if p1_move == "SCISSORS":
                p2_move = random.choice(["ROCK", "PAPER"])
        elif difficulty == 3:
            if p1_move == "ROCK":
                increased = "PAPER"
                options = ["ROCK", increased, increased, "ROCK", increased, "SCISSORS", increased, "SCISSORS",
                           "SCISSORS", "ROCK"]
            if p1_move == "PAPER":
                increased = "SCISSORS"
                options = ["PAPER", increased, increased, "ROCK", increased, "ROCK", increased, "PAPER", "ROCK",
                           "PAPER"]
            if p1_move == "SCISSORS":
                increased = "ROCK"
                options = ["SCISSORS", increased, increased, "PAPER", increased, "SCISSORS", increased, "PAPER",
                           "PAPER", "SCISSORS"]
            p2_move = rand_move()

        else:
            p2_move = rand_move()
        print("ROCK ", end="")
        time.sleep(0.5)
        print("PAPER ", end="")
        time.sleep(0.5)
        print("SCISSORS ", end="")
        time.sleep(0.5)
        print("SHOOT...", end="")
        time.sleep(0.3)
        print("")
        print(p1_move + " V/S " + p2_move)
        time.sleep(0.5)
        if p1_move == "ROCK" and p2_move == "SCISSORS":
            print(p1 + " Wins this round!")
            win_p1 = win_p1 + 1
        elif p1_move == "PAPER" and p2_move == "ROCK":
            print(p1 + " Wins this round!")
            win_p1 = win_p1 + 1
        elif p1_move == "SCISSORS" and p2_move == "PAPER":
            print(p1 + " Wins this round!")
            win_p1 = win_p1 + 1
        elif p1_move == p2_move:
            print("Draw...")
        else:
            print(p2 + " Wins this round")
            win_p2 = win_p2 + 1
        time.sleep(1)
        print(f'Current Standing : {p1}: {win_p1} and {p2}: {win_p2}')
        print("-" * 50)
        time.sleep(1)

    time.sleep(1)
    print("-" * 30)
    if win_p1 > win_p2:
        print(p1 + " Wins the match!")
    elif win_p2 > win_p1:
        print(p2 + " Wins the match!")
    else:
        print("Match concluded in a Draw!")
    print("-" * 30)
    time.sleep(1)
    print(f'Do you want to challenge {p2} for a rematch?')
    print("Enter 1 for yes and 0 for no :")
    rematch = int(input())
    if rematch == 0:
        print("Do you want to play with a new opponent? Enter 1 for yes and 0 for no: ")
        new_match = int(input())
        if new_match == 1:
            p2 = random.choice(lines)
            print("You will be playing against: ")
            time.sleep(2)
            print(p2)
            continue
        else:
            break
    else:
        print(f'{p2} accepted your rematch request! ')
