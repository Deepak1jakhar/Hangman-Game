import random
from replit import clear
from hangman_arts import stages, logo, win, lose
print(logo)
words_list = ["apple", "orange", "banana", "strawberry", "mango", "pomegranate", "kiwi", "papaya", "litchi"]
display = []
chosen_word = random.choice(words_list)
lives = len(stages)-1
for i in chosen_word:
    display.append("_")
end = False
while not end:
    guess = input("Guess a Letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end = True
            print(lose)

    print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        end = True
        print(win)

