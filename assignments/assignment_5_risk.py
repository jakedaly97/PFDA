# Assignment 5
# Author: Jake Daly
# program simulates 

import random
import numpy as py

# variables keep track of the total number of wins for attacker and defender across 1000 simulations
total_attacker_wins = 0
total_defender_wins = 0

for _ in range(1000): # loops the below code 1000 times 

    attacker_rolls = [random.randint(1, 6) for _ in range(3)] # random.randin() function used to simulate dice roll (values from 1-6) range is set to 3 because there are 3 attackers (3 dice rolls)

    defender_rolls = [random.randint(1, 6) for _ in range(2)] # range is set to 2 because there are 2 defenders (2 dice rolls)


    attacker_rolls = sorted(attacker_rolls, reverse=True) # sorted() and reverse=True organise the list in descending order (highest value to lowest)

    defender_rolls = sorted(defender_rolls, reverse=True)

    # set score to zero 
    attacker_wins = 0
    defender_wins = 0

    
    for i in range(len(defender_rolls)): # loops over the defender rolls which is 2
        if attacker_rolls[i] > defender_rolls[i]: # highest roll of the attacker is compared to the highest roll of the defender, if attacker dice roll is higher than defender, attacker wins. If the roll is equal to or less, defender wins
            attacker_wins += 1  # variable increases by 1
        else:
            defender_wins += 1  

   
    total_attacker_wins += attacker_wins # updates win for each loop
    total_defender_wins += defender_wins

# Print the total results after 1000 simulations
print("Total attacker wins:", total_attacker_wins)
print("Total defender wins:", total_defender_wins)

# Resources
# https://www.w3schools.com/python/ref_func_range.asp
# https://docs.python.org/3/library/random.html