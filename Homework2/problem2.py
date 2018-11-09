import random

num = random.randint(1, 100)
num_of_guesses = 0
guess = 0
 
while int(guess) != num: 
  guess = input("Guess: ") 
  if guess == "exit":
     break
 
  num_of_guesses += 1 

  if int(guess) > num:
    print("It's too high")  
  elif int(guess) < num:
    print("It's too low")
else:
  print("Congrats")
  print("Bravo. You guessed it in {} steps" .format(num_of_guesses))  

