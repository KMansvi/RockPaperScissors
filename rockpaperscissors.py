import random

# winning possibilities
win = [("rock","scissors"),("scissors","paper"),("paper","rock")]

# choices for the computer to choose
choices = ["rock","paper","scissors"]

#to count player's points
playerpoints=0

#to count computer's points
computerpoints=0

#to decide the winner
def inputs():
    print("Get ready to play the game ROCK-PAPER-SCISSORS with the computer!!")
    #input for the player's choice
    player=input("What's your move?? ")
    #printing player's move
    print("\nYour move is ",player)
    #computer selects randomly from choices list
    computer=random.choice(choices)
    #printing computer's move
    print("Computer's move is ",computer)
    moves(player,computer)

#when choices are different
def moves(player,computer):
    global playerpoints,computerpoints
    if player != computer:
        #check patterns
        playerwin=(player,computer)
        computerwin=(computer,player)
        if playerwin in win:
            if playerwin == win[0]:
                print("Rock damages Scissors \n\n\tPLAYER WON")
            elif playerwin == win[1]:
                print("scissors cuts paper \n\n\tPLAYER WON")
            elif playerwin == win[2]:
                print("paper covers rock \n\n\tPLAYER WON")
            playerpoints+=1
        elif computerwin in win:
            if computerwin == win[0]:
                print("Rock damages Scissors \n\n\tCOMPUTER WON")
            elif computerwin == win[1]:
                print("scissors cuts paper \n\n\tCOMPUTER WON")
            elif computerwin == win[2]:
                print("paper covers rock \n\n\tCOMPUTER WON")
            computerpoints+=1
        #if player did not input rock/paper/scissors
        else:
            print("INVALID RESPONSE from player \n\n\tCOMPUTER WINS")
            computerpoints+=1
    
    #when choices are same
    elif player==computer:
        print("\nDRAW, both player and computer gets 1 point each")
        playerpoints+=1
        computerpoints+=1

    return 0

def main():
    while True:

        #calling the function to execute the game
        inputs()

        #printing the points of player and computer
        print("\nPlayer points:",playerpoints)
        print("Computer points:",computerpoints)
        
        #if the user wants to play another round
        again=input("\nDoes the player want to go for another round(yes/no):")
        if again!="yes":
            break

if __name__=="__main__":
    main()