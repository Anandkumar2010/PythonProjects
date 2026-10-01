import time
from random import randint


# Define the main function to encapsulate the game logic
def play_game():
    print("--- Welcome to the Dice Simulator ---")

    # Use an infinite loop to allow the user to roll multiple times
    while True:
        # Get input, remove accidental whitespace, and convert to lowercase for consistent checking
        choice = input("Do you want to roll dice?(y/n)").strip().lower()

        # Check if the user wants to play
        if choice in {"y", "yes"}:
            print("Rolling", end="")

            # Animation: print three dots with a delay to build suspense
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print()  # Move to a new line after the dots

            # Generate and display random dice values
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)
            print(f"You rolled {dice1} and {dice2}")

        # Check if the user wants to quit
        elif choice in {"n", "no"}:
            print("Exiting...")
            break  # Exit the while loop to end the program

        # Handle invalid inputs
        else:
            print("Please enter a valid input")
            print("Thank you for playing")


# Call the function to actually start the game
play_game()



