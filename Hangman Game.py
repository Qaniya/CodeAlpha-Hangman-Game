import random

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
    ]
    return stages[attempts]

def hangman():
    categories = {
        "Animals": ["cat", "dog", "lion", "tiger", "zebra"],
        "Fruits": ["apple", "mango", "peach", "grape", "pear"],
        "Countries": ["india", "china", "italy", "egypt", "japan"],
    }

    print("Welcome to Hangman!")
    print("Choose a category:")

    category_names = list(categories.keys())
    for i, category in enumerate(category_names, 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen category: "))
            if 1 <= choice <= len(category_names):
                selected_category = category_names[choice - 1]
                print(f"You selected: {selected_category}")
                break
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    word = random.choice(categories[selected_category])
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("\nGuess the word:", " ".join(guessed_word))
    print(display_hangman(attempts))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts}")

        print("\n" + display_hangman(attempts))
        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
