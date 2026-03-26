# import random library
import random

# ─────────────────────────────────────────────────────────────
# Function 1: Generate the secret number
# ─────────────────────────────────────────────────────────────
def get_secret_number():
    # Computer chooses a secret number between 1 and 10
    return random.randint(1, 10)


# ─────────────────────────────────────────────────────────────
# Function 2: Get and validate user input
# ─────────────────────────────────────────────────────────────
def get_guess(attempt, max_attempts):
    # Ask the user to enter a guess
    guess_str = input(
        f"Attempt {attempt}/{max_attempts} - Guess a number: "
    )  # Return string not int

    # Validate inputs
    if guess_str:
        # Error handling
        try:
            # Convert guess from string to int
            return int(guess_str)
        except ValueError:
            print("Error: Please enter a valid number only")
            return None

    else:
        print("You haven't entered anything. Please enter a number.")
        return None


# ─────────────────────────────────────────────────────────────
# Function 3: Check the guess
# ─────────────────────────────────────────────────────────────
def check_guess(guess_num, secret_number):
    # Comparison and return the result
    if guess_num == secret_number:
        return "win"
    elif guess_num > secret_number:
        return "high"
    else:
        return "low"


# ─────────────────────────────────────────────────────────────
# Function 4: Play one full round
# ─────────────────────────────────────────────────────────────
def play_round():
    # Computer chooses a secret number
    secret_number = get_secret_number()

    # Set max number of attempts
    max_attempts = 5

    print(
        f"You have {max_attempts} Attempts to guess the secret number between 1 and 10."
    )

    # Loop through attempts using for loop
    for attempt in range(1, max_attempts + 1):
        # Get and validate user guess
        guess_num = get_guess(attempt, max_attempts)

        if guess_num == None:
            continue

        # Check the guess and print the result
        result = check_guess(guess_num, secret_number)

        if result == "win":
            print(f"Genius! The secret number was {secret_number}. You won!")
            break
        elif result == "high":
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")

    # for-else: runs only if the loop finished without a break (player lost)
    else:
        print(
            f"Game Over! You used all {max_attempts} attempts. The secret number was {secret_number}."
        )


# ─────────────────────────────────────────────────────────────
# Function 5: Main game loop
# ─────────────────────────────────────────────────────────────
def main():
    # While True: keeps the game running until the player chooses to stop
    while True:
        play_round()

        # Ask the player if he wants to play again
        play_again = input("Would you like to play again? (y/n): ").strip().lower()

        # If the player doesn't want to play again, exit the while loop
        if play_again != "y":
            print("Thanks for playing! See you in the next episode. 👋")
            break


# ─────────────────────────────────────────────────────────────
# Start the game
# ─────────────────────────────────────────────────────────────
main()


