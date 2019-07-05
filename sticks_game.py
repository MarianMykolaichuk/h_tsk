import random

while True:
    player_or_computer = input("Would you like to play the computer (cpu) or player2 (p2)")
    if player_or_computer == "cpu" or player_or_computer=="p2":
        break
    print("Your choice was invalid!")
    
##picking the number of sticks to start with

while True:
    number_of_sticks = int(input("How many sticks would you like to start with? (10-50)"))
    if number_of_sticks>=10 and number_of_sticks<=50:
        print("G

##starting the game
while number_of_sticks>0:
    #turns            
    for whose_turn in range(1,3):
        if whose_turn ==1:
            print("It's Player 1 turn")
        elif whose_turn ==2:
            print("It's Player 2 turn")
        if number_of_sticks==2:
            max_sticks=2
        if number_of_sticks==1:
            max_sticks=1
        if number_of_sticks>2:
            max_sticks=3

       
        while True:         
            print("How many sticks are you taking off? (1-{max_sticks})".format(max_sticks=min(3,max_sticks)))
            sticks