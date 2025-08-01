# Random is imported.
import random

# This prints the name of the game.
print("\nNUMBER GUESSING GAME\n")
score = 0
while True:
    # While True user enters a number from 1 to 5 and presses 'q' to quit the game.
    number_guessed = input("Enter to guess a number from 1 to 5 ('q' to quit): \n")
    print()

    # Computer randomly selects number from 1 to 5.
    computer_guessed = random.randint(1,5)
    try:
        # If user guessed is 'q', the game quits and prints 'BYE'.

        if number_guessed == str('q'):
            exit_query = input("Are you sure you want to quit? Enter either 'yes' or 'no': ").lower()
            if exit_query == 'yes':
                print("\nAww BYE! Let's play again later, okay👋.\n")
                break
            else:
                print("\nWow COOL! Let's play then🤗.\n")
                continue

        # If computer guessed number is equal to user guessed number:
        # 'CORRECT' is printed.
        print("-------RESULT-------")
        if computer_guessed == int(number_guessed):
            score += 1
            print("CORRECT |😘|")
            print("-------------------")
            print(f"The computer guessed number is: {computer_guessed}")
            print(f"SCORE: {score}\n")

        # If computer guessed number is not equal to user guessed number:
        # 'WRONG' is printed.
        elif computer_guessed != int(number_guessed):
            score -= 1
            print("WRONG |😒|")
            print("-------------------")
            print(f"The computer guessed number is: {computer_guessed}")
            print(f"SCORE: {score}\n")

    # Except ValueError enter 'Invalid entry. Please enter again.' and continue.
    except ValueError:
        print("Invalid entry. Please enter a number from 1 to 6.😵‍💫")
        continue






