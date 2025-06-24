import random

# List of predefined words
word_list = ['apple', 'house', 'plane', 'river', 'zebra']

# Randomly choose a word
secret_word = random.choice(word_list)
guessed_word = ['_'] * len(secret_word)
attempts_left = 6
guessed_letters = []

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while attempts_left > 0 and '_' in guessed_word:
    print("Word:", ' '.join(guessed_word))
    print("Guessed letters:", ', '.join(guessed_letters))
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for idx, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[idx] = guess
    else:
        print("❌ Wrong guess.\n")
        attempts_left -= 1

# Result
if '_' not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)