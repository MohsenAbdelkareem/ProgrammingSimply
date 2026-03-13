# 1- import random library
import random

# 2- While True: keeps the game running until the player chooses to stop
while True:

    # 3- Computer chooses a secret number between 1, 10
    secret_number = random.randint(1, 10)

    # 4- Set max number of attempts
    max_attempts = 5

    print(
        f"You have {max_attempts} Attempts to guess the secret number between 1 and 10."
    )

    # 5- Loop through attempts using for loop
    for attempt in range(1, max_attempts + 1):
        # 6- we ask the user to enter a guess
        guess_str = input(
            f"Attempt {attempt}/{max_attempts} - Guess a number: "
        )  # Return string not int

        # 7- validate inputs
        if guess_str:
            # logic
            # 8- Error hanlding
            try:
                # 9- Convert guess from string to int
                guess_num = int(guess_str)
                # 10- comparison and printing the result
                if guess_num == secret_number:
                    print(f"Genius! The secret number was {secret_number}. You won!")
                    break
                elif guess_num > secret_number:
                    print("Your guess is too high. Try again.")
                else:
                    print("Your guess is too low. Try again.")
            except ValueError:
                print("Error: Please enter a valid number only")
        else:
            print("You haven't entered anything. Please enter a number.")
    # 11- for-else: runs only if the loop finished without a break (player lost)
    else:
        print(
            f"Game Over! You used all {max_attempts} attempts. The secret number was {secret_number}."
        )

    # 12- Ask the player if he wants to play again
    play_again = input("Would you like to play again? (y/n): ").strip().lower()

    # 13- If the player doesn't want to play again, exit the while loop
    if play_again != "y":
        print("thanks for playing! See you in the next episode.  👋")
        break
