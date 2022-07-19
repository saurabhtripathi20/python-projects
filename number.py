import random

top_limit = input("number limit? ")

if top_limit.isdigit():
    top_limit = int(top_limit)
    if top_limit <= 0:
        print("enter no. greater then 0")
        quit()
else:
    print("enter a number")
    quit()        


number = random.randrange(top_limit)
# generate_number = print(number)
guesses = 0
while True:
    guesses += 1
    guess_number = input("guess a number: ")
    if (guess_number.isdigit()):
        guess_number = int(guess_number)
    else:
        print("Only integers") 
        continue
          
    if (guess_number == number):
        print("you guessed right")
        break
    else:
        print(f"oops guessed number is{ number}") 
        quit()


print(f"you guessed it n {guesses} gusses")
           

