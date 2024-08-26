#Type in your code here
import random                        
options = ["Rock", "Paper", "Scissors"]  
rounds = 0                             
score = 0                             
computerscore =0
user_wins = 0
comp_wins = 0

print ("ROCK,PAPER,SCISSORS")
while rounds == 0:                    
  for i in range (5):                  
    answer = input ("Pick Rock, Paper or Scissors.")     

    print (answer)                               
    computer= random.choice(options)                        

    print ("Computer picks",computer)                   

    if answer == "Rock" and computer == "Rock":          
      print ("Its a tie!")                                       
      rounds +=1                                                  

    elif answer == "Paper" and computer == "Paper":
      print ("Its a tie!")
      rounds +=1

    elif answer == "Scissors" and computer == "Scissors":
      print ("Its a tie!")
      rounds +=1

    elif answer == "Paper" and computer == "Rock":
      print ("You win!")
      rounds +=1
      score +=1
      user_wins +=1

    elif answer == "Paper" and computer == "Scissors":
      print ("Computer won!")
      rounds +=1
      computerscore +=1
      comp_wins +=1

    elif answer  == "Rock" and computer == "Paper":
      print ("Computer won!")
      rounds +=1
      computerscore +=1
      comp_wins +=1

    elif answer == "Rock" and computer == "Scissors":
      print ("Computer won!")
      rounds +=1
      score +=1
      user_wins +=1

    elif answer == "Scissors" and computer == "Rock":
      print ("Computer won!")
      rounds +=1
      computerscore +=1
      comp_wins +=1

    elif answer == "Scissors" and computer == "Paper":
      print ("You win!")
      rounds +=1
      score +=1
      user_wins +=1
    if user_wins==3:
        break
    if comp_wins==3:
        break



if score < computerscore:                      
  print ("Your score is", score)
  print ("Computers score is",computerscore)
  print ("Computer wins!.")

if score > computerscore:
  print ("Your score is", score)
  print ("Computers score is",computerscore)
  print ("You win!.")

if score == computerscore:
  print ("Your score is", score)
  print ("Computers score is",computerscore)
  print ("Its a tie!!.")




