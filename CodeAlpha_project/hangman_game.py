import random

# 1. Predefined list of words
words = ["python", "jupiter", "galaxy", "starlight", "nebula"]
target_word = random.choice(words)

# 2. Game setup
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a display version of the word (e.g., "_ _ _ _ _")
display_word = ["_"] * len(target_word)

print("--- Welcome to Hangman! ---")

# 3. Game Loop
while incorrect_guesses < max_attempts and "_" in display_word:
    print(f"\nWord: {' '.join(display_word)}")
    print(f"Mistakes: {incorrect_guesses}/{max_attempts}")
    print(f"Guessed so far: {', '.join(guessed_letters)}")
    
    guess = input("Guess a letter: ").lower()

    # Basic validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'!")
        continue

    guessed_letters.append(guess)

    # 4. Check the guess
    if guess in target_word:
        print(f"Good job! '{guess}' is in the word.")
        # Update the underscores with the actual letter
        for index, letter in enumerate(target_word):
            if letter == guess:
                display_word[index] = guess
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not there.")

# 5. Ending the game
if "_" not in display_word:
    print(f"\nCongratulations! You found the word: {target_word}")
else:
    print(f"\nGame Over! You've run out of attempts.")
    print(f"The word was: {target_word}")