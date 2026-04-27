import random

def get_random(low: int, high: int) -> int:
    return random.randint(low, high)

def get_guess(low: int, high: int) -> int:
    while True:
        try:
            guess = int(input(f"Enter a guess ({low}-{high}): "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if low <= guess <= high:
            return guess
        print(f"Please enter a number between {low} and {high}.")

def feedback(guess: int, target: int) -> str:
    if guess < target:
        return "Too low"
    elif guess > target:
        return "Too high"
    else:
        return "Correct!"

def difficulty() -> int:
    while True:
        try:
            n = int(input("Choose a difficulty level (1-3): "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if 1 <= n <= 3:
            return n
        print("Invalid difficulty level, please enter 1, 2, or 3.")

def limit(diff: int) -> int:
    return {1: 5, 2: 10, 3: 15}.get(diff, 5)

def play():
    attempts = 0
    diff = difficulty()
    ranges = {1: (1, 10), 2: (1, 50), 3: (1, 100)}
    low, high = ranges[diff]
    n = get_random(low, high)
    max_attempts = limit(diff)
    guess = None

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess(low, high)
        print(feedback(guess, n))
        if guess == n:
            break
        print(f"You have {max_attempts - attempts} attempt(s) left.")

    if guess != n:
        return f"You lose! The correct number was {n}."
    return f"Congratulations! It took you {attempts} guess(es)."

if __name__ == "__main__":
    while True:
        print(play())
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break