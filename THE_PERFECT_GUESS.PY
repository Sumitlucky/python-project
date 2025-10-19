import random
 
n =  random.randint(1,100)

a = -1
guessses = 1

while(a != n):
  a = int(input("Guess a number: "))
  if(a > n ):
    print("Lower number please : ")
    guessses += 1  

  elif(a<n):
    print("Higher number please : ")
    guessses += 1  


print(f"You have guessed the number{n} correctly in {guessses} attempt ")
