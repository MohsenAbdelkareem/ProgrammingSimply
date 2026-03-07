# 1- import random library
import random

# 2- Computer chooses a secret number between 1, 10
secret_number = random.randint(1, 10)

# 3- we ask the user to enter a guess
guess_str = input("Guess a number between 1 and 10 : ") # Return string not int

# 4- validate inputs
if guess_str:
    # logic
    # 5- Error hanlding
    try:
        # 6- Convert guess from string to int
        guess_num = int(guess_str)
        # 7- comparison and printing the result
        if guess_num == secret_number:
            print(f"Genius! The secret number was {secret_number}. You won!")
        elif guess_num > secret_number:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")
    except ValueError:
        print("Error: Please enter a valid number only")
else:
    print("You haven't entered anything. Please enter a number.")
