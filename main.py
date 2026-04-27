import random

# Function for getting a random number
def get_random(low: int = 1, high: int = 100) -> int:
    num = random.randint(low, high)
    return num

# Function for getting the users input (guess)
def get_guess() -> int:
    is_int = False
    while is_int == False:
        guess = input("Enter a guess (integer) 1-100")
        if type(guess) not int:
            print("Please enter an integer")

# Function for feedback
def feedback(guess: int, target: int) -> str:
    if guess < target:
        print("You're lower")
    elif guess > target:
        print("You're higher")
    elif guess == target:
        print("Correct!")

# Function to create and play the game
def play():
    n = get_random()
    attempts = 0
    correct = False
    while correct == False:
        attempts += 1
        guess = get_guess()
        print(feedback(guess, n))
        if feedback(guess, n) == "Correct!":
            correct = True

    return f"Congratulations! It took you {attempts} tries to guess the number."

if __name__ == "__main__":
    play()