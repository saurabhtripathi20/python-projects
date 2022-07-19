print("Welcome to my Game!")

play = input("Do you want to play game? ")
if play.lower() != "yes":
    quit()    

print("okay lets play :)") 

Score = 0

answer = input("What is my name? ")
if answer.lower() == "saurabh":
    print("Correct answer")
    Score += 1
else:
    print("Incorrect")  

answer = input("What is my age? ")
if answer.lower() == "22":
    print("Correct answer")
    Score += 1
else:
    print("Incorrect")  

answer = input("What is my surname? ")
if answer.lower() == "tripathi":
    print("Correct answer")
    Score += 1
else:
    print("Incorrect")  

answer = input("What is my place? ")
if answer.lower() == "vapi":
    print("Correct answer")
    Score += 1
else:
    print("Incorrect")  

print(f"my score is {(Score/4) * 100} ")