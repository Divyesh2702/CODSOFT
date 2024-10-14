import random

def printoptions():
    print("\nChoices:")
    print("1)Rock")
    print("2)Paper")
    print("3)Scissors\n")

def get_user_choice():
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.\n")
        printoptions()
        choice = input("Enter your choice (1, 2, or 3): ")
    return choice

def getcomputerchoice():
    return str(random.randint(1, 3))

def print_round_result(user_choice, comp_choice, user_score, comp_score):
    choices_mapping = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    user_choice_str = choices_mapping[user_choice]
    comp_choice_str = choices_mapping[comp_choice]

    print(f"You chose {user_choice_str}")
    print(f"Computer chose {comp_choice_str}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "1" and comp_choice == "3") or \
         (user_choice == "2" and comp_choice == "1") or \
         (user_choice == "3" and comp_choice == "2"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        comp_score += 1

    print(f"Score: You {user_score}, Computer {comp_score}\n")

def printfinalresult(x, y):
    if x > y:
        print("Congratulations! You win!")
        return
    elif x < y:
        print("Sorry, computer wins. Better luck next time.")
        return
    else:
        print("It's a tie!")
        return


print("Rock Paper Scissors\n")

rounds = int(input("Best out of how many rounds? "))
printoptions()

userscore = 0
compscore = 0

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    user_choice = get_user_choice()
    comp_choice = getcomputerchoice()
    print_round_result(user_choice, comp_choice, userscore, compscore)
