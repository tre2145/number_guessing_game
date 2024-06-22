import random

def number_guessing_game():
    #Define the range of numbers
    lower_bound = 1
    upper_bound = 100

    #Generate a random number within the range
    target_number = random.randint(lower_bound, upper_bound)

    #Define the number of attempts
    attempts = 10

    print("Welcome to Number Guessing Game!")
    print(f"I'm computing a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess the correct number.")

    #Start guessing loop
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attemp {attempt}: Enter your guess: "))

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempt} attempts.")
            break
    else:
        print("Your guesses: {attempts}. The number was... {target_number}.")

if __name__ == "__main__":
        number_guessing_game()