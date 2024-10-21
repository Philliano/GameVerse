#imports
import random
import os

#clearing screen command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#difficulty choice
def hangman_choice(username, user_money, mainmenu, age_check):
    print(f"welcome {username} to")
    print("""\u001b[32m
 

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

          \n\u001b[0m""""")
    print("""On what difficulty do you want to play Hangman?
          Easy[1]
          Medium[2]
          Hard[3]
          \033[2m\u001b[31mImpossible!![4]\u001b\033[0m""")
    difficulty = int(input("choose with 1, 2, 3, or 4: "))
    
    if difficulty in [1, 2, 3]:
        play_hangman_by_difficulty(difficulty, username, user_money, mainmenu, age_check)
    elif difficulty == 4:
        if input("On this difficulty your system will shutdown if you can't guess the word in 10 tries. Are you sure? [y]/[n]") == 'y':
            play_hangman(random.choice(impossible_words), username, user_money, mainmenu, age_check, Shutdown=True)
        else:
            clear_screen()
            hangman_choice(username, user_money, mainmenu, age_check)
    else:
        clear_screen()
        print("\u001b[41m Invalid selection, please try again.\u001b[0m \n ")
        hangman_choice(username, user_money, mainmenu, age_check)

def load_words(file_name):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'Wordlists_Hangman', file_name)
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Load word lists
easy_words = load_words('easy.txt')
medium_words = load_words('medium.txt')
hard_words = load_words('hard.txt')
impossible_words = load_words('impossible.txt')

def replay_text(username, user_money, mainmenu, age_check):
    replay_hangman = input(f"{username}, you tryna play again? [y] or [n]: ")
    if replay_hangman == 'y':
        clear_screen()
        hangman_choice(username, user_money, mainmenu, age_check)
    elif input("Wanna go back to the menu or end the game? Say 'menu' or 'end': ").lower() == 'menu':
        clear_screen()
        mainmenu(username, user_money, age_check)
    else:
        exit()

def play_hangman(word, username, user_money, mainmenu, age_check, Shutdown=False):
    guessed_word = ['_'] * len(word)
    attempts = 10
    guessed_letters = set()

    while attempts > 0 and ''.join(guessed_word) != word:
        clear_screen()
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = letter
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Incorrect guess! {guess} is not in the word.")
        
        input("Press Enter to continue...")

    clear_screen()
    if ''.join(guessed_word) == word:
        print(f"Congrats! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")
        if Shutdown:
            print("Now your system will \u001b[41m shut down...\u001b[0m")
            print("""\u001b[41m
▀█████████▄  ▄██   ▄      ▄████████      ▀█████████▄  ▄██   ▄      ▄████████ 
  ███    ███ ███   ██▄   ███    ███        ███    ███ ███   ██▄   ███    ███ 
  ███    ███ ███▄▄▄███   ███    █▀         ███    ███ ███▄▄▄███   ███    █▀  
 ▄███▄▄▄██▀  ▀▀▀▀▀▀███  ▄███▄▄▄           ▄███▄▄▄██▀  ▀▀▀▀▀▀███  ▄███▄▄▄     
▀▀███▀▀▀██▄  ▄██   ███ ▀▀███▀▀▀          ▀▀███▀▀▀██▄  ▄██   ███ ▀▀███▀▀▀     
  ███    ██▄ ███   ███   ███    █▄         ███    ██▄ ███   ███   ███    █▄  
  ███    ███ ███   ███   ███    ███        ███    ███ ███   ███   ███    ███ 
▄█████████▀   ▀█████▀    ██████████      ▄█████████▀   ▀█████▀    ██████████ 
                                                                             

\u001b[0m""")
            os.system('shutdown -s')
    replay_text(username, user_money, mainmenu, age_check)

def play_hangman_by_difficulty(difficulty, username, user_money, mainmenu, age_check):
    word_list = {1: easy_words, 2: medium_words, 3: hard_words}[difficulty]
    play_hangman(random.choice(word_list), username, user_money, mainmenu, age_check)  # Pass the age_check parameter
