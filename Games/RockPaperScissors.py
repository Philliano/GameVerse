#imports
import random
import os

user_wins = 0
bot_wins = 0

#clearing screen command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#Rock Paper Scissors code
def Rock_Paper_scissors(username, user_money, mainmenu, age_check):
    print(f"Welcome {username} to")
    print("""\u001b[34m
______           _     ______                       _____      _                        
| ___ \         | |    | ___ \                     /  ___|    (_)                       
| |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ ___ 
|    // _ \ / __| |/ / |  __/ _` | '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__/ __|
| |\ \ (_) | (__|   <  | | | (_| | |_) |  __/ |    /\__/ / (__| \__ \__ \ (_) | |  \__ |
\_| \_\___/ \___|_|\_\ \_|  \__,_| .__/ \___|_|    \____/ \___|_|___/___/\___/|_|  |___/
                                 | |                                                    
                                 |_|                                                    

          \u001b[0m""")
    
    rock = ("""    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")
    paper = (""" 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
    scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
                """)

    input("Press Enter to start")
    print("best of 3")
    for games_rps in range(3):
        clear_screen()
        Bot_RPS = random.choice(['rock', 'paper', 'scissors'])
        Bot_sign = eval(Bot_RPS)
        User_RPS = input("What are you choosing? rock, paper, or scissors? ")
        if User_RPS in ['rock', 'paper', 'scissors']:
            if User_RPS == Bot_RPS:
                print("\u001b[33m Tie \u001b[0m")
                games_rps + 1
            elif User_RPS == 'rock' and Bot_RPS == 'paper' or User_RPS == 'paper' and Bot_RPS == 'scissors' or User_RPS == 'scissors' and Bot_RPS == 'rock':
                global bot_wins
                bot_wins += 1
                print("\u001b[31m You lost \u001b[0m")
                games_rps + 1
            else:
                global user_wins
                user_wins += 1
                print("\u001b[32m You win \u001b[0m")
                games_rps + 1
                
            user_sign = eval(User_RPS)

            user_lines = user_sign.splitlines()
            bot_lines = Bot_sign.splitlines()
            max_lines = max(len(user_lines), len(bot_lines))

            user_lines += [''] * (max_lines - len(user_lines))
            bot_lines += [''] * (max_lines - len(bot_lines))

            print(f"\nYou chose: {User_RPS}\t\t\tBot chose: {Bot_RPS}")
            for i in range(max_lines):
                print(f"{user_lines[i]:<30} {bot_lines[i]}")
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")

        input("Press Enter to continue...")

    else:
        clear_screen()
        print(f"Nice game: final standings are Bot:{bot_wins} {username}: {user_wins}")

    Replay_RPS = input("do you want to try again? [y]/[n]")

    if Replay_RPS == 'y':
        clear_screen()
        bot_wins = 0
        user_wins = 0
        Rock_Paper_scissors(username, user_money, mainmenu, age_check)
    else:
        bot_wins = 0
        user_wins = 0
        backtomenu = input("Wanna go back to the menu or end the game? Say 'menu' or 'end' to answer: ")
        if backtomenu.lower() == 'menu':
            clear_screen()
            mainmenu(username, user_money, age_check)
        elif backtomenu.lower() == 'end':
            exit()
