import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target : "))
    if(userChoice == target):
        print("Success : Correct Guess!! ")
        break
    if(userChoice < target):
        print("Your number was to small. Take a bigger guess..")
    else:
        print("Your number was to big. Take a smaller guess..")

print("-----GAME OVER-----")      