# Rock Paper Scissors game

import random 

options = ("rock", "paper", "scissors")   # a tuple with the possible options 
running = True



while running :                               # this while loop is for the option to the player to play again 
    
    player = None                             # in player varaible stored the player 's choice
    computer = random.choice(options)         # the computer choice is one random choice from the options tuple


    while player not in options:                                       # while the player is not entering one of the three choises the program is asking again until the player gives a value from the options tuple
        player = input("Enter a choice (rock, paper, scissors ) : ")   # the program  askes from the player to enter a value 



    # and then we print the player 's choice and the computer 's choice 

    print(f"Player:{player}")
    print(f"Computer:{computer}")


    # we define all the winning conditions, if there is not one of them then the player lose

    if player == computer :
        print("It is a tie !")

    elif player == "rock" and computer == "scissors":
        print("You win !")

    elif player == "paper" and computer == "rock":
        print("You win !")

    elif player == "scissors" and computer == "paper":
        print("You win !")

    else:
        print("You lose :') ")

    play_again = input("Play again ? (yes/no): ").lower()
    
    if not play_again == "yes":
        running = False

    