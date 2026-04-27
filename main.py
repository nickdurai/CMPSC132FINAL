import random

# Function for getting a random number
def get_random(low: int = 1, high: int = 100) -> int:
    num = random.randint(low, high)
    return num

# Function for getting the users input (guess)
def get_guess() -> int:
    while True:
        try:
            guess = int(input("Enter a guess 1-100: "))
        except ValueError:
            print("Please enter an integer")
            continue
        if 1 <= guess <= 100:
            return guess
        print("Please enter a number between 1 and 100")

# Function for feedback
def feedback(guess: int, target: int) -> str:
    if guess < target:
        return "Too low"
    elif guess > target:
        return "Too high"
    else:
        return "Correct!"

# Function to create and play the game
def play():
    n = get_random()
    attempts = 0
    while True:
        attempts += 1
        guess = get_guess()
        print(feedback(guess, n))
        if guess == n:
            break

    return f"Congratulations! It took you {attempts} tries to guess the number."

if __name__ == "__main__":
    print(play())