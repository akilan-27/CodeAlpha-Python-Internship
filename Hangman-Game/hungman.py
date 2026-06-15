import random

secret_words = [
    "taco", "waffle", "pizza", "popcorn", "surfing", 
    "gaming", "king", "vibe", "groove", "arcade", 
    "panda", "sloth", "safari", "jungle", "guitar"
]

target_word = random.choice(secret_words)

guessed_letters = []
wrong_guesses = 0
max_lives = 6

print("Welcome to Hangman! Let's see what you got.")

while wrong_guesses < max_lives:
    
    display_word = ""
    for letter in target_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    print(f"\nWord: {display_word}")

    if "_" not in display_word:
        print(f"Awesome job! You got it: '{target_word}'")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Oops! Please enter a single letter from A-Z.")
        continue

    if guess in guessed_letters:
        print(f"You already tried '{guess}'. Pick something else!")
        continue

    guessed_letters.append(guess)

    if guess not in target_word:
        wrong_guesses += 1
        lives_left = max_lives - wrong_guesses
        print(f"Nope! '{guess}' is not in the word. Lives left: {lives_left}")

else:
    print("\n Out of moves! Better luck next time.")
    print(f"The word you were looking for was: '{target_word}'")
