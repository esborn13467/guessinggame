# this program demonstrates a guessing game 
# get user input
# player=input("what is your name"?)
# print("hello there"+player+"!")
#generate a random number 
 
# get user number
# using a while Loop 
# check if user input is equal to generated number
#from random import randint



# terminal cmds for git hub 
# ls lists thr gates in the current directory
# pwd get current directory(folder)
# cd path 
from random import randint
player = input("what is your name?")
print("hello there " +player +"!")
counter=0

random_number=randint(10,50)
while counter<5:
    user_number=eval(input("enter a number"))

    counter+=1

    if user_number<random_number: 
        print("your guess is too low")
    elif user_number>random_number:
        print("your  guess is too high")
    elif user_number==random_number:
        
        break

    print("game over.")
if user_number==random_number:
    print("you win")
else:
    print("game over the correct number is")
    print(random_number)
#    when a user guesses a lower number than the range 
#    if user_input <number
#    print("your guess is too low")
#    elif user_input>number
#  print("your guess is too high")
# elif user_input==number
#  print("you guessed right")
