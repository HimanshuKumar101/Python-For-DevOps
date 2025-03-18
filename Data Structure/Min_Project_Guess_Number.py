import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the target or Quit(Q): "))
    if(userChoice == "Q"):
        break
    
    userChoice = int(userChoice) #this is done because the input is taken as stringQ
    if( userChoice == target):
        print("You guessed the right number")
        break
    elif(userChoice > target):
        print("You guessed a greater number")
    else:
        print("You guessed a smaller number")

print("The target was: ", target)
print("Successfully guessed the number")
