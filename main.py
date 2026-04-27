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
    
# Function to create guess limit
def limit(diff: int) -> int:
    if diff == 1:
        return 5
    elif diff == 2:
        return 10
    elif diff == 3:
        return 15
    else:
        return 5

# Function to create and play the game
def play():
    attempts = 0
    n = difficulty()
    max_attempts = limit(n)
    while True and attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        print(feedback(guess, n))
        if guess == n:
            break
        else:
            print(f"Try again! You have {max_attempts - attempts} attempts left.")

    if attempts == max_attempts and guess != n:
        return f"You lose! The correct number was {n}."
    else:
        return f"Congratulations! It took you {attempts} guess(es) to guess the number."

if __name__ == "__main__":
    print(play())