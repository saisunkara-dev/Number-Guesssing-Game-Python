import random

best_score = None

while True:
    print("\n🎯 Welcome to Number Guessing Game!")
    print("Choose Difficulty Level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        max_num = 50
    elif choice == "2":
        max_num = 100
    elif choice == "3":
        max_num = 200
    else:
        print("Invalid choice. Try again.")
        continue

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\nGuess a number between 1 and {max_num}")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts.")
            if best_score is None or attempts < best_score:
                best_score = attempts
                print("🏆 New Best Score!")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break