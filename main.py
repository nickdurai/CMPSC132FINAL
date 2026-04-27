import random

# Function for getting a random number
def get_random(low, high) -> int:
    num = random.randint(low, high)
    return num

# Function for getting the users input (guess)
def get_guess() -> int:
    while True:
        try:
            guess = int(input("Enter a guess: "))
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
    
# Function to create different game difficulties
def difficulty():
    n = int(input("Choose a difficulty level (1-3): "))
    if n == 1:
        return get_random(1, 10)
    elif n == 2:
        return get_random(1, 50)
    elif n == 3:
        return get_random(1, 100)
    else:
        print("Invalid difficulty level. Defaulting to level 1.")
        return get_random(1, 10)

# Function to create and play the game
def play():
    n = difficulty()
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