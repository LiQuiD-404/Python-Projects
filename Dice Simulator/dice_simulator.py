# Dice Simulator - by Shubham Singh | github: LiQuiD-404
# no pre-requisites required for running this program

import random  # this module will generate a random number between the given limits
import time


def number_generator(x):
    global rand
    if x == 1:
        rand = random.randint(1, 6)
    if x == 2:
        rand = 3
        while rand % 2 != 0:
            rand = random.randint(1, 6)
    if x == 3:
        rand = 2
        while rand % 2 == 0:
            rand = random.randint(1, 6)
    if x == 4:
        rand = random.randint(1, 2)
        if rand == 1:
            rand = 1
        if rand == 2:
            rand = 6
    return rand


print("-----------Welcome to Dice Simulator----------")
print("Select a dice based on your preference")
print("1. Standard Die - With equal probability of each number ")
print("2. Even biased Die - Will guarantee an even throw ")
print("3. Odd biased Die - Will guarantee an odd throw ")
print("4. 1 and 6 biased Die - Will only result in a number between 1 or 6 ")

while True:     # check for valid user input
    choice = int(input("Enter your choice: "))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        break
    else:
        print("Wrong Input.. Please try again!!")

n = 1  # loop control variable
while n != 0:
    lst = []  # to store the output of the random function for multiple dice
    print("Enter the number of dice you want to roll: ")
    no_dice = int(input())
    for i in range(no_dice):
        output = number_generator(choice)
        lst.append(output)
    print("Rolling dice------->")
    time.sleep(2)
    print("-" * 30)
    print("Result: ", lst)
    print("-" * 30)
    time.sleep(0.8)
    print("Do you want to roll again? ")
    print("Enter 1 to reroll ")
    print("Enter 0 to exit ")
    n = int(input())
    if n == 1:
        print("Do you want to change your die? Enter 1 to change and 0 to continue with the same dice")
        new_choice = int(input("Enter choice: "))
        if new_choice == 1:
            print("Select a dice based on your preference")
            print("1. Standard Die - With equal probability of each number ")
            print("2. Even biased Die - Will guarantee an even throw ")
            print("3. Odd biased Die - Will guarantee an odd throw ")
            print("4. 1 and 6 biased Die - Will only result in a number between 1 or 6 ")
            while True:  # check for valid user input
                choice = int(input("Enter your choice: "))
                if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                    break
                else:
                    print("Wrong Input.. Please try again!!")
