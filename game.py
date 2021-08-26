import random

user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Type rock/paper/scissors or Q/q to quit:")
    if user_input=='q' or user_input=='Q':
        break
    if user_input not in options:
        continue
    random_num=random.randint(0,2)
    computer_guess=options[random_num]
    print("Computer picked",computer_guess)

    if user_input=="rock" and computer_guess=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_guess=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input=="scissors" and computer_guess=="paper":
        print("You won!")
        user_wins+=1
    elif user_input==computer_guess:
        print("Draw")
    else:
        print("Computer won!")
        computer_wins+=1

if user_wins>computer_wins:
    print("WINNER --> YOU !!")
    print("Scoreboard")
    print("YOU      COMPUTER")
    print(user_wins,"       ",computer_wins)
else:
    print("WINNER --> COMPUTER !!")
    print("Scoreboard")
    print("YOU      COMPUTER")
    print(user_wins,"       ",computer_wins)
print("Goodbye!")