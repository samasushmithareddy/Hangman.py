import random

def play_hangman():
    # 1. Predefined list of 5 words as per task requirements
    words = ["python", "software", "logic", "algorithm", "script"]
    secret_word = random.choice(words)
    
    # 2. Initialize game state
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6 # Limit incorrect guesses to 6
    
    print("--- Welcome to CodeAlpha Hangman! ---")
    
    # 3. Main Game Loop
    while incorrect_guesses < max_attempts:
        # Display the current progress (e.g., p _ t h _ n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {max_attempts - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Check if the player has won
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            break
            
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            
    # 4. Handle game over (Loss)
    if incorrect_guesses == max_attempts:
        print("\nGame Over!")
        print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()

