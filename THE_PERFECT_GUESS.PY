import random
 
n =  random.randint(1,100)

a = -1
guessses = 0

while(a != n):
  guessses += 1
  a = int(input("Guess a number: "))
  if(a > n ):
    print("Lower number please : ")
  else:
    print("Higher number please : ")


print(f"You have guessed the number{n} correctly in {guessses} attempt ")