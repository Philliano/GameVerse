#imports
import random
import os
from Games import Black_Jack, Hangman, Numbergame, RockPaperScissors, Roulette

# clearing screen command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu
def mainmenu(username, user_money, age_check):
    print(f"Welcome {username} to")

    print("""\u001b[36m
░░      ░░░░      ░░░  ░░░░  ░░        ░░  ░░░░  ░░        ░░       ░░░░      ░░░        ░
▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒   ▒▒   ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒
▓  ▓▓▓   ▓▓  ▓▓▓▓  ▓▓        ▓▓      ▓▓▓▓▓  ▓▓  ▓▓▓      ▓▓▓▓       ▓▓▓▓      ▓▓▓      ▓▓▓
█  ████  ██        ██  █  █  ██  ██████████    ████  ████████  ███  █████████  ██  ███████
██      ███  ████  ██  ████  ██        █████  █████        ██  ████  ███      ███        █
                                                                                          
\u001b[0m""")
    print("Games: \t\t\t\t Casino:")
    print("[1] Number guesser \t\t [4] Black-Jack")
    print("[2] Hangman \t\t\t [5] Roulette")
    print("[3] Rock Paper Scissors")
    print("Select a game using the number before the game")
    
    if age_check >= 18:
        print(f'You have €{user_money}')
    
    chosengame = input()

    if chosengame == '1':
        clear_screen()
        Numbergame.numguessing(username, mainmenu, user_money, age_check)

    elif chosengame == '2':
        clear_screen()
        Hangman.hangman_choice(username, user_money, mainmenu, age_check)

    elif chosengame == '3':
        clear_screen()
        RockPaperScissors.Rock_Paper_scissors(username, user_money, mainmenu, age_check)

    elif chosengame == '4':
        clear_screen()
        if age_check < 18:
            print("\u001b[33msorry, you are too young to play this game\u001b[0m")
            mainmenu(username, user_money, age_check)
        else:
            if user_money == 0:
                print("\u001b[33myou are broke now, you can't play blackjack\u001b[0m")
                mainmenu(username, user_money, age_check)
            else:
                user_money = Black_Jack.Blacky(username, user_money, mainmenu)
                clear_screen()
                mainmenu(username, user_money, age_check)

    elif chosengame == '5':
        clear_screen()
        if age_check < 18:
            print("\u001b[33msorry, you are too young to play this game\u001b[0m")
            mainmenu(username, user_money, age_check)
        else:
            if user_money == 0:
                print("\u001b[33myou are broke now, you can't play roulette\u001b[0m")
                mainmenu(username, user_money, age_check)
            else:
                clear_screen()
                user_money = Roulette.roulette(username, user_money, mainmenu, age_check)
                mainmenu(username, user_money, age_check)

    else:
        clear_screen()
        print("\u001b[33m Invalid selection, please try again.\u001b[0m")
        mainmenu(username, user_money, age_check)


# Startup
clear_screen()
username = input("Hello user, what's your name? ")
age_check = int(input("How old are you?"))
user_money = 100
clear_screen()
mainmenu(username, user_money, age_check)
