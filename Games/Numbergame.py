import random
import os

# clearing screen command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Guessing game
def numguessing(username, mainmenu, user_money, age_check):
    while True:
        Randonumber = random.randint(1, 100)
        number_of_guesses = 0

        clear_screen()
        print("Welcome", username, "to:")
        print("""
┏┓         ┓            ┓     
┃┓┓┏┏┓┏┏  ╋┣┓┏┓  ┏┓┓┏┏┳┓┣┓┏┓┏┓
┗┛┗┻┗ ┛┛  ┗┛┗┗   ┛┗┗┻┛┗┗┗┛┗ ┛ 
                              
""")
        print("I'm thinking of a number between 1-100, you have 10 guesses")

        for _ in range(10):
            try:
                user_input = int(input("Guess the number: "))

                if user_input == Randonumber:
                    number_of_guesses += 1
                    clear_screen()
                    print("Nice one", username)
                    print("The number was", Randonumber)
                    print("It took you", number_of_guesses, "tries")
                    restart = input("Do you want to play this game again? Say 'y' or 'n': ")

                    if restart.lower() == 'y':
                        numguessing(username, mainmenu, user_money, age_check)
                    elif restart.lower() == 'n':
                        backtomenu = input("Wanna go back to the menu or end the game? Say 'menu' or 'end': ")

                        if backtomenu.lower() == 'menu':
                            clear_screen()
                            mainmenu(username, user_money, age_check)
                        elif backtomenu.lower() == 'end':
                            exit()

                elif user_input < Randonumber:
                    number_of_guesses += 1
                    clear_screen()
                    print("Wrong, the number is higher")
                    print("Try again: ")
                elif user_input > Randonumber:
                    number_of_guesses += 1
                    clear_screen()
                    print("Wrong, the number is lower")
                    print("Try again: ")
            except ValueError:
                number_of_guesses -= 1
                print("Give me a valid number")

        else:
            clear_screen()
            print("You made 10 guesses. The number was", Randonumber)

        replay = input(f"{username}, you were close, wanna try again? Say 'y' or 'n': ")

        if replay.lower() == 'y':
            numguessing(username, mainmenu, user_money, age_check)
        else:
            backtomenu = input("Wanna go back to the menu or end the game? Say 'menu' or 'end': ")
            if backtomenu.lower() == 'menu':
                clear_screen()
                mainmenu(username, user_money, age_check)                
            elif backtomenu.lower() == 'end':
                exit()
