import random
import time

def main():
    # Welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Initialize high scores list
    high_scores = []

    # Main game loop
    while True:
        # Generate random number to guess
        number_to_guess = random.randint(1, 100)
        number_of_guesses = 0
        user_guess = None

        # Start timer
        start_time = time.time()

        # User input loop
        while user_guess != number_to_guess:
            user_input = input("Enter your guess: ")

            # Check if user input is a valid integer between 1 and 100
            if user_input.isdigit() and 1 <= int(user_input) <= 100:
                user_guess = int(user_input)
                number_of_guesses += 1

                # Provide feedback based on user's guess
                if user_guess < number_to_guess:
                    print("Too low! Try again.")
                elif user_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    # End timer and calculate time taken
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 2)

                    # Display results and update high scores
                    print(f"Congratulations! You guessed the number in {number_of_guesses} attempts.")
                    print(f"Time taken: {time_taken} seconds")
                    high_scores.append((number_of_guesses, time_taken))
                    high_scores.sort()

                    # Display top 5 high scores
                    print("\nTop 5 High Scores:")
                    for index, score in enumerate(high_scores[:5], start=1):
                        print(f"{index}. {score[0]} attempts, {score[1]} seconds")
            else:
                print("Please enter a valid integer between 1 and 100.")

        # Ask user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
