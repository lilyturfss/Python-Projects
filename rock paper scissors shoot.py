#rock paper scissors shoot

import random
import time
score_comp = 0
score_hooman = 0
exit = ""

while exit.lower() != "no":
    print("")
    print("")
    print("**Rock, Paper, Scissors, Shoot!**")
    time.sleep(1)
    print("")

    print("Your score: ", score_hooman)
    print("Computer's score: ", score_comp)

    print("")
    x = "no"
    while x == "no":
        print("*Pick your choice*")
        choice = input("Rock/Paper/Scissors: ")
        print("")
        time.sleep(1)

        if choice.lower() == "rock":
            print("You choose Rock.")
            x = ""
        elif choice.lower() == "paper":
            print("You choose Paper.")
            x = ""
        elif choice.lower() == "scissors":
            print("You choose Scissors.")
            x = ""
        else:
            print("That is not a choice, try again.")
    time.sleep(1)
    # Computer Plays
    cc = random.randint(0,2)
    match cc:
        case 0:
            print("Computer chose scissors.")
            choicecomp = "scissors"
        case 1:
            print("Computer chose rock.")
            choicecomp = "rock"
        case 2:
            print("Computer chose paper.")
            choicecomp = "paper"
        case _:
            print("Something went wrong.")
            exit()
    
    # The actual game
    print("")
    print("")
    time.sleep(2)

        #Tie
    if choicecomp.lower() == choice.lower():
        print("It's a tie.")
        # Computer chooses scissors
    elif choicecomp.lower() == "scissors" and choice.lower() == "rock":
        print("You win this round!")
        score_hooman += 1
    elif choicecomp.lower() == "scissors" and choice.lower() == "paper":
        print("You lost this round :(")
        score_comp += 1       

        # Computer chooses paper
    elif choicecomp.lower() == "paper" and choice.lower() == "rock":
        print("You lost this round :(")
        score_comp += 1
    elif choicecomp.lower() == "paper" and choice.lower() == "scissors":
        print("You win this round!")
        score_hooman += 1
    
        # Computer chooses rock
    elif choicecomp.lower() == "rock" and choice.lower() == "paper":
        print("You win this round!")
        score_hooman += 1
    elif choicecomp.lower() == "rock" and choice.lower() == "scissors":
        print("You lost this round :(")
        score_comp += 1
    
    print("")
    time.sleep(2)
    print("Your score: ", score_hooman)
    print("Computer's score: ", score_comp)
    print("")
    time.sleep(2)
    exit = input("Still wanna play? (Yes/No)")

if score_hooman > score_comp:
    print("Overall, you won!")
elif score_hooman < score_comp:
    print("Overall, you lost :(")
else:
    print("TIE.")
