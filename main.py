import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
limit = 3

while user_wins != limit and computer_wins != 3 :                               # "or" = "and", "and" = "or"
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print ("you won CHAMP")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won CHAMP")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won CHAMP")
        user_wins += 1
    elif user_input == computer_pick:
        print("draw")

    else:
        print("you lost LOSER")
        computer_wins += 1

print(f"You won {user_wins} and the computer won {computer_wins}")
print("Goodbye")
