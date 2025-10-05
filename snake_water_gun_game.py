import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
print("water:-> w")
print("Snake:-> s")
print("Gun:-> g")
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g":0}
reversedDict = {1: "Snake", -1: "water", 0 : " Gun"}

you = youDict[youstr]

print(f"You chose{reversedDict[you]}\nComputer chose {reversedDict[computer]}")

if(computer == you):
  print("Its a draw: ")
else:
  if(computer == -1 and you == 1):
    print("you win!")

  elif(computer == -1 and you == 0):
    print("you Lose!") 

  elif(computer ==1 and you == -1):
    print("you Lose!")

  elif(computer == 1 and you == 0):
    print("you win!")  

  elif(computer == 0 and you == 1):
    print("You Lose!")

  else:
    print("Something went wrong! ")
     

