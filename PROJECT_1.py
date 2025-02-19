'''
1 = rock
2 = paper
3 = scissors

'''
import random

a=int(input("Enter how many you want to play: "))
#loop for how many times to play
i=1
while(i<=a):
    # computer choice
    NPC = random.choice([1, 2, 3])

    # input from user
    user = input("Choose any one from Rock, Paper, Scissors: ")
    
    # create dictionary for inputs
    dict = {"r": 1, "rock": 1, "p": 2, "paper": 2, "s": 3, "scissors": 3}
    #create reversedict to print choices choosen by user and computer
    reversedict = {1:"rock", 2:"paper", 3:"scissors"}
    # put dict values into user
    user2 = dict[user.lower()]

    print(f"!!! You choose {reversedict[user2]}\n!!! Computer choose {reversedict[NPC]}")


    # condition for different cases in game
    if (user2==NPC):
        print("MATACH DRAW")
        
    else:
        if(NPC==1 and user2==2):
            print("YOU WIN")
            
        elif(NPC==1 and user2==3):
            print("YOU LOSE")
            
        elif(NPC==2 and user2==1):
            print("YOU LOSE")
            
        elif(NPC==2 and user2==3):
            print("YOU WIN")
            
        elif(NPC==3 and user2==1):
            print("YOU WIN")

        elif(NPC==3 and user2==2):
            print("YOU LOSE")
            
        else:
            ("SOMETHING GONE WRONG!!!")
            
        i+=1