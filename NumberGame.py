import random

def guess_game():
    print("------------Number Guessing Game!------------")
    print("The computer has selected a number between 1 and 100. Start guessing!")

    random_number = random.randint(1, 100)
    guess_count = 0

    while True:
        user_guess = int(input("Your guess: "))

        guess_count += 1

        if user_guess < random_number:
            print("Guess higher.")
        elif user_guess > random_number:
            print("Guess lower.")
        else:
            print("Congratulations! You guessed the correct number in",guess_count , "guesses!")
            break

    play_again = input("Do you want to play again? (Enter 'y' for Yes / 'n' for No): ")
    if play_again.lower() == 'y':
        guess_game()
    else:
        print("You have exited the game. Have a great day!")

guess_game()
