import random

# generate a random number between 1 and 100
secret_number = random.randint(1,100)

print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

attemps = 0
while True:
    guess = int(input("enter your guess:"))
    attemps +=1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"congratulation! you guessed the number in {attemps} attempts.")
        break        
       
