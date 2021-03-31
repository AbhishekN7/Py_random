import random
player_score=0
computer_score=0
choice=["Rock","Paper","Scissor"]

for i in range(11): 
    Player=int(input("Enter Your Choice:\nPress 1 for Rock\n2 for Paper\n3 for Scissor \n"))
    computer=random.choice(choice)
    
    if Player==1:
        if computer=="Paper":
            print("Computer chose Paper")
            print("**Computer Wins**")
            computer_score+=1
        elif computer=="Rock":
            print("Computer chose Rock too..")
            print("**It's a Tie**")
        else:
            computer=="Scissor"
            print("Computer chose Scissor")
            print("**You Win**")
            player_score+=1
    
    elif Player==2:
        if computer=="Rock":
            print("Computer Chose Rock")
            print("**You Win**")
            player_score+=2
        elif computer=="Paper":
            print("Computer Chose Paper too..")
            print("**It's a Tie**")
        else:
            computer=="Scissor"
            print("Computer Chose Scissor")
            print("**Computer Wins**")
            computer_score+=2
    
    elif Player==3:
        if computer=="Rock":
            print("Computer Chose Rock")
            print("**Computer Wins**")
            computer_score+=3
        elif computer=="Paper":
            print("Computer Chose paper")
            print("**You Win**")
            player_score+=3
        else:
            computer=="Scissor"
            print("Computer Chose Scissor too..")
            print("**It's a Tie**")
            
    else:
        print("Wrong Input")
        print("**Enter Valid Input**")
            
print("*"*60)
            
print(" Computer score:" +str(computer_score))
print(" Your Score:" +str(player_score))


if player_score > computer_score:
    print(" You Won The Game.\n Well Played")

elif computer_score > player_score:
    print(" Computer Won the Game.\n Better Luck Next Time.")
 
else:
    print(" Game Tied")
    
    
            
            
            
        
            
            
            
            
  
    