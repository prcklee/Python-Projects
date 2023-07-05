import random
from hangman_art import logo, stages
from hangman_words import word_list

random_word = random.choice(word_list)

print("\n\n\n")
print("👋 Welcome to hangman!! 👋")
# Test Code
# print(f"The random word is '{random_word}'")
print(logo)

game_over = False
lives = 6

# list of unknown letters
random_list = []
for _ in random_word:
    random_list += "_"

while game_over != True:

    user_guess = input("Guess a letter: ")

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == user_guess:
            random_list[position] = user_guess 
    print(f"{' '.join(random_list)}")

    if user_guess not in random_list:
        lives -= 1
        print(f"{user_guess} is not in the word. Guess another letter.")
        # losing condition
        if lives == 0:
            game_over = True
            print("😭 You Lose!!! Game Over!!! 🤬")
            print(f"The secret word is '{random_word}'👈")
            print("\n\n")
    
    # ASCII art
    print(stages[lives])
    
    # winning condition
    if "_" not in random_list:
        print('\n\n')
        game_over = True
        print("🏆 You Win!!! Game Over!!! 🎖️")
        print("\n\n")

    if game_over == False:
        print(f"Lives remain: {lives}")



    