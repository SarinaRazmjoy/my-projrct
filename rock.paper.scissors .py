import random
print ("rock")
print ("paper")
print ("scissors")
print("_________________")



Player1Wins=0
Player2Wins=0
EndOfGame=5

while Player1Wins < EndOfGame and Player2Wins < EndOfGame :
    print(f"your score = { Player1Wins } and my score = { Player2Wins }") 
    Player_1 = input ( "Make your move:").lower()
    Random = (random.randint(0 , 2))
    Player_2= random

    if Player_1 == "quit" :
        break 

    
    if Random ==  0 :
        Player_2 = ("roke")
    elif Random == 1:
        Player_2 =("paper")
    elif Random == 2 :
        Player_2 =("scissors")


    print(                        )
    print(f"you use : {Player_1} ")
    print ( f"I use : {Player_2} ")
    
    if Player_1 == Player_2:
        print(" thats a tie ...")
    elif Player_1 == "rock":
        if Player_2 == "paper":
            print(" you lose...")
            Player2Wins += 1
        elif Player_2 == "scissors":
            print("you win... ") 
            Player1Wins += 1 
    elif Player_1 == "paper":
        if Player_2 == ("rock"):
            print("you win... ")  
            Player1Wins += 1  
        elif Player_2 == "scissors":
            print(" you lose...")
            Player2Wins += 1
    elif Player_1 == "scissors":
        if Player_2 == "rock":
            print("you lose...")
            Player2Wins += 1
        elif Player_2 == "paper":
            print("you win...")
            Player1Wins += 1  
    else: 
        print("something went wrong ....")

    if Player1Wins >= 5 :
        print(" The game is over and You have won.")
    elif Player2Wins >= 5:
        print("The game is over and I won .")


