#imports
import random
import os

# Color numbers
red_numbers = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
black_numbers = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']

#clearing screen command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bet(user_money):
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))
            if bet_amount > user_money:
                print("You don't have enough money to place that bet.")
            else:
                return bet_amount
        except ValueError:
            print("Please enter a valid number.")

#roulette wheel
def wheel_spin():
    return random.choice([*map(str, range(37)), '00'])

#winnings frm bet and result
def calculate_winnings(result, bet_type, number, numbers, bet_range, bet_dozen, color, odd_even):
    red_numbers = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
    black_numbers = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']

    if bet_type == '1':  #Single number
        if result == number:
            return 35 # x 35 bet
    elif bet_type == '2':  #Multiple numbers
        if result in numbers:
            return 35 / len(numbers) # x 35 bet / amt guesses
    elif bet_type == '3':  #High/Low
        if bet_range == 'high' and result.isdigit() and 19 <= int(result) <= 36:
            return 1 # x 2 money
        elif bet_range == 'low' and result.isdigit() and 1 <= int(result) <= 18:
            return 1 # x 2 money
    elif bet_type == '4':  #Dozen 
        if bet_dozen == '1' and result.isdigit() and 1 <= int(result) <= 12:
            return 2 # x 3 money
        elif bet_dozen == '2' and result.isdigit() and 13 <= int(result) <= 24:
            return 2 # x 3 money
        elif bet_dozen == '3' and result.isdigit() and 25 <= int(result) <= 36:
            return 2 # x 3 money
    elif bet_type == '5':  #Color
        if color == 'red' and result in red_numbers:
            return 1 # x 2 money
        elif color == 'black' and result in black_numbers:
            return 1 # x 2 money
    elif bet_type == '6':  #Odd/Even
        if result.isdigit() and int(result) != 0:  #0 is not in this bet
            if odd_even == 'odd' and int(result) % 2 != 0:
                return 1 # x 2 money
            elif odd_even == 'even' and int(result) % 2 == 0:
                return 1 # x 2 money
    return 0 

# Main roulette
def roulette(username, user_money, mainmenu, age_check):
    print(""" 
\u001b[31m .----------------. \u001b[30m .----------------.  \u001b[31m.----------------. \u001b[30m .----------------. \u001b[31m .----------------. \u001b[30m .----------------. \u001b[31m .----------------. \u001b[30m .----------------. 
\u001b[31m| .--------------. |\u001b[30m| .--------------. |\u001b[31m| .--------------. |\u001b[30m| .--------------. |\u001b[31m| .--------------. |\u001b[30m| .--------------. |\u001b[31m| .--------------. |\u001b[30m| .--------------. |
\u001b[31m| |  _______     | |\u001b[30m| |\u001b[32m     ____     \u001b[30m| |\u001b[31m| | _____  _____ | |\u001b[30m| |   _____      | |\u001b[31m| |  _________   | |\u001b[30m| |  _________   | |\u001b[31m| |  _________   | |\u001b[30m| |  _________   | |
\u001b[31m| | |_   __ \    | |\u001b[30m| |\u001b[32m   .'    `.   \u001b[30m| |\u001b[31m| ||_   _||_   _|| |\u001b[30m| |  |_   _|     | |\u001b[31m| | |_   ___  |  | |\u001b[30m| | |  _   _  |  | |\u001b[31m| | |  _   _  |  | |\u001b[30m| | |_   ___  |  | |
\u001b[31m| |   | |__) |   | |\u001b[30m| |\u001b[32m  /  .--.  \  \u001b[30m| |\u001b[31m| |  | |    | |  | |\u001b[30m| |    | |       | |\u001b[31m| |   | |_  \_|  | |\u001b[30m| | |_/ | | \_|  | |\u001b[31m| | |_/ | | \_|  | |\u001b[30m| |   | |_  \_|  | |
\u001b[31m| |   |  __ /    | |\u001b[30m| |\u001b[32m  | |    | |  \u001b[30m| |\u001b[31m| |  | '    ' |  | |\u001b[30m| |    | |   _   | |\u001b[31m| |   |  _|  _   | |\u001b[30m| |     | |      | |\u001b[31m| |     | |      | |\u001b[30m| |   |  _|  _   | |
\u001b[31m| |  _| |  \ \_  | |\u001b[30m| |\u001b[32m  \  `--'  /  \u001b[30m| |\u001b[31m| |   \ `--' /   | |\u001b[30m| |   _| |__/ |  | |\u001b[31m| |  _| |___/ |  | |\u001b[30m| |    _| |_     | |\u001b[31m| |    _| |_     | |\u001b[30m| |  _| |___/ |  | |
\u001b[31m| | |____| |___| | |\u001b[30m| |\u001b[32m   `.____.'   \u001b[30m| |\u001b[31m| |    `.__.'    | |\u001b[30m| |  |________|  | |\u001b[31m| | |_________|  | |\u001b[30m| |   |_____|    | |\u001b[31m| |   |_____|    | |\u001b[30m| | |_________|  | |
\u001b[31m| |              | |\u001b[30m| |              | |\u001b[31m| |              | |\u001b[30m| |              | |\u001b[31m| |              | |\u001b[30m| |              | |\u001b[31m| |              | |\u001b[30m| |              | |
\u001b[31m| '--------------' |\u001b[30m| '--------------' |\u001b[31m| '--------------' |\u001b[30m| '--------------' |\u001b[31m| '--------------' |\u001b[30m| '--------------' |\u001b[31m| '--------------' |\u001b[30m| '--------------' |
\u001b[31m '----------------' \u001b[30m '----------------' \u001b[31m '----------------' \u001b[30m '----------------' \u001b[31m '----------------' \u001b[30m '----------------' \u001b[31m '----------------' \u001b[30m '----------------' 
\u001b[0m""")
    
    input("press enter to continue")
    clear_screen()
    print(f"You have €{user_money}")
    #Betting options
    print("Choose your bet type:")
    print("[1] Single Number (0-36, 00)")
    print("[2] Multiple Numbers (comma-separated, e.g., 1,2,3)")
    print("[3] High (19-36) / Low (1-18)")
    print("[4] Dozens (1-12, 13-24, 25-36)")
    print("[5] Color (Red/Black)")
    print("[6] Odd/Even")

    bet_type = input("Select a bet type (1-6): ")

    #get error without because "variables not defined"
    number, numbers, bet_range, bet_dozen, color, odd_even = None, None, None, None, None, None

    #bets
    if bet_type == '1':
        number = input("Choose a number (0, 00, 1-36): ")
        if number not in ['0', '00'] + [str(i) for i in range(1, 37)]:
            print("Invalid number.")
            return roulette(username, user_money, mainmenu, age_check)
        bet_amount = get_bet(user_money)

    elif bet_type == '2':
        numbers = input("Choose numbers (comma-separated, example: 1,2,3): ")
        numbers = [n.strip() for n in numbers.split(',')]
        if any(n not in ['0', '00'] + [str(i) for i in range(1, 37)] for n in numbers):
            print("Invalid numbers.")
            return roulette(username, user_money, mainmenu, age_check)
        bet_amount = get_bet(user_money)

    elif bet_type == '3':
        bet_range = input("Choose 'high' (19-36) or 'low' (1-18): ").lower()
        if bet_range not in ['high', 'low']:
            print("Invalid choice.")
            return roulette(username, user_money, mainmenu, age_check)
        bet_amount = get_bet(user_money)

    elif bet_type == '4':
        bet_dozen = input("Choose 1 (1-12), 2 (13-24), or 3 (25-36): ").lower()
        if bet_dozen not in ['1', '2', '3']:
            print("Invalid choice.")
            return roulette(username, user_money, mainmenu, age_check)
        bet_amount = get_bet(user_money)

    elif bet_type == '5':
        color = input("Choose 'red' or 'black': ").lower()
        if color not in ['red', 'black']:
            print("Invalid color.")
            return roulette(username, user_money, mainmenu, age_check)
        bet_amount = get_bet(user_money)

    elif bet_type == '6':
        odd_even = input("Choose 'odd' or 'even': ").lower()
        if odd_even not in ['odd', 'even']:
            print("Invalid choice.")
            return roulette(username, user_money, mainmenu, age_check)
        bet_amount = get_bet(user_money)

    else:
        print("Invalid selection.")
        input("press enter to go again")
        clear_screen()
        return roulette(username, user_money, mainmenu, age_check)

    #Spimming wheel
    result = wheel_spin()
    print(f"The wheel landed on {result}!")

    #payout
    payout = calculate_winnings(result, bet_type, number, numbers, bet_range, bet_dozen, color, odd_even)
    if payout > 0:
        winnings = bet_amount * payout
        user_money += winnings
        print(f"Congratulations! You won €{winnings}!")
        replay_roulette(username, user_money, mainmenu, age_check)
    else:
        user_money -= bet_amount
        print(f"Sorry, you lost €{bet_amount}. You have €{user_money} left.")
        replay_roulette(username, user_money, mainmenu, age_check)

    #replay
def replay_roulette(username, user_money, mainmenu, age_check):
    if user_money == 0:
        print('\u001b[33myou cant play roulette because ur BROKEE\u001b[0m')
        input('press enter to continue')
        clear_screen()
        mainmenu(username, user_money, age_check)
    else:
        replay_blacky = input(f"{username}, you tryna play again? [y] or [n]: ").lower()
        if replay_blacky == 'y':
            clear_screen()
            roulette(username, user_money, mainmenu, age_check)
        elif replay_blacky == 'n':
            backtomenu = input("Wanna go back to the menu or end the game? Say 'menu' or 'end' to answer: ").lower()
            if backtomenu == 'menu':
                clear_screen()
                mainmenu(username, user_money, age_check)
            elif backtomenu == 'end':
                exit()
