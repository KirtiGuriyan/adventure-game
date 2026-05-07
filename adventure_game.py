"""
Adventure Game
Author: [Kirti Guriyan]
License: MIT
Description: A text-based choice-driven RPG where players explore a forest or a cave.
"""


# Handles the initial setup and the first major choice.
def start_game():
    print("Welcome to the Adventure Game!")

    player_name = input("What is your name? ")
    print(f"Hello, {player_name}! Let's begin your adventure.")
    
    print("You find yourself at a crossroads. You can:")
    print("1. Explore the forest")
    print("2. Enter the cave")
    choice = input("What do you want to do? (1 or 2): ")
    if choice == "1": 
        print("You venture into the forest, surrounded by tall trees and mysterious sounds.")
    elif choice == "2":
        print("You step into the dark cave, feeling the cool air and hearing echoes inside.")
    else:
        print("Invalid choice. Your adventure ends before it begins.")
    return choice


# Logic for continuing the adventure after the initial choice.
def continue_adventure():
    print("The adventure continues...")
    next_step = input("Do you want to go deeper (yes/no)? ")
    if next_step.lower() == "yes":
        print("You bravely move forward into the unknown!")
    else:  
        print("You decide to turn back and head home. Adventure ends.")


# Logic for when the player chooses the forest route.
def forest_path():
    print("You walk deeper into the forest and discover a fork in your path.")
    print("You can:")
    print("1. Follow the river")
    print("2. Climb a tall tree to get a better view")
    choice = input("What do you want to do? (1 or 2): ")
    if choice == "1":
        print("You follow the river and find fresh water and beautiful scenery.")
    elif choice == "2":
        print("You climb the tree and spot a distant village beyond the forest.")
    else:
        print("You hesitate and lose your way among the trees.")


# Logic for when the player chooses the cave route.
def cave_path():
    print("You venture deeper into the cave and find there was darkness all around.")
    print("You can:")
    print("1. Light a torch") 
    print("2. Proceed in the dark")
    choice = input("what do you want to do? (1 or 2): ")
    if choice == "1":
        print("You light a torch and see sparkling gems embedded in the cave walls.")
    elif choice == "2":
        print("You stumble in the dark and fall into a hidden pit.")
    else:
        print("You freeze in place, unsure of what to do next.")   
   

# Main game loop to allow for replayability.
while True:
    choice = start_game()
    # The adventure continues functions are called in sequence for now.
    continue_adventure()
    if choice == "1":
        forest_path()
    elif choice == "2":
        cave_path()
    else:
        print("You did not choose a valid path, so the story ends here.")
    restart = input("Do you want to restart the adventure? (yes/no): ")
    if restart != "yes":
        print("Thank you for playing the Adventure Game!")
        break
