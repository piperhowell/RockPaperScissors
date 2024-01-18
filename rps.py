import random as r

###
# Name: Piper Howell
# Class: CISC 105 Intro to Computer Science
# Project: RPS Game

print("Warning, selection must be lowercase")

play = True

while play == True:

    userChoice = ""
    replay = ""

    while (userChoice != "r") and (userChoice != "p") and (userChoice != "s"):   
        userChoice = input("Please select r, p, or s: ")
        print("You chose: " + userChoice)
        if (userChoice != "r") and (userChoice != "p") and (userChoice != "s"):
            print("Warning, selection must be lowercase r, p, or s")

    computerChoice = r.choice(['r','p','s'])   
    print("The computer chose: " + computerChoice)

    if userChoice == "r":
        if computerChoice == "r":
            print("Draw, you both chose rock")
        if computerChoice == "p":
            print("You lost")
        if computerChoice == "s":
            print("You won")
    if userChoice == "p":
        if computerChoice == "p":
            print("Draw, you both chose paper")
        if computerChoice == "s":
            print("You lost")
        if computerChoice == "r":
            print("You won")
    if userChoice == "s":
        if computerChoice == "s":
            print("Draw, you both chose scissors")
        if computerChoice == "r":
            print("You lost")
        if computerChoice == "p":
            print("You won")

    while (replay != "y") and (replay != "n"):
        replay = input("Do you want to play again? y/n: ")
        if replay == "y":
            play = True
        elif replay == "n":
            play = False
        else:
            print("You must choose y or n")

    
# rock > scissors
# scissors > paper 
# paper > rock