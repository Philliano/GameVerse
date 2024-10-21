#imports
import random
import os

user_wins = 0
bot_wins = 0

#clearing screen command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#black jack
def calculate_value(hand):
    value, aces = 0, 0
    for card in hand:
        if card[:-1] in ['J', 'Q', 'K']:
            value += 10
        elif card[:-1] == 'A':
            value += 11
            aces += 1
        else:
            value += int(card[:-1])
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def deal_card(cards, suits):
    return f"{random.choice(cards)}{random.choice(suits)}"

def Blacky(username, user_money, mainmenu):
    print(f"Welcome {username} to:")
    print("""
\u001b[32m_________________________________________________________________
\u001b[31m    ____                                                       
    /   )    /               /              /                /   
   /__ /    /    __    __   /-__-          /     __    __   /-__-
  /    )   /   /   ) /   ' /(    ===      /    /   ) /   ' /(    
_/____/   /___(___(_(___ _/___\      (___/    (___(_(___ _/  \_
\u001b[32m_________________________________________________________________\u001b[0m                                                                                                                                
""")
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    suits = ['♠', '♡', '♢', '♣']
    
    # plyer and bot hand
    player_hand = [deal_card(cards, suits), deal_card(cards, suits)]
    dealer_hand = [deal_card(cards, suits), deal_card(cards, suits)]
    player_value, dealer_value = calculate_value(player_hand), calculate_value(dealer_hand)
    
    #bet
    while True:
        try:
            bet = int(input('How much do you want to bet? '))
            if bet > user_money:
                print("\u001b[33mYou don't have enough money! Please place a valid bet.\u001b[0m")
            else:
                user_money -= bet
                break
        except ValueError:
            print("\u001b[33mPlease enter a valid number!\u001b[0m")
    
    input("Press Enter to start")
    clear_screen()

    #show hand
    print(f"Your cards: {player_hand} (value: {player_value})")
    print(f"Dealer's face-up card: {dealer_hand[0]}")

    #player pick
    while player_value < 21:
        action = input("[Hit] or [Stand]? ").lower()
        clear_screen()
        
        if action == "hit":
            new_card = deal_card(cards, suits)
            player_hand.append(new_card)
            player_value = calculate_value(player_hand)

            print(f"Your new card: {new_card}")
            print(f"Your total hand: {player_hand} (value: {player_value})")
            print(f"Dealer's face-up card: {dealer_hand[0]}")

            if player_value > 21:
                print("Bust! You lose.")
                return user_money  #Return updated user_money after a loss
        elif action == "stand":
            break
        else:
            print("\u001b[33mInvalid choice, please type 'Hit' or 'Stand'.\u001b[0m")

    #dealer
    clear_screen()
    print(f"Dealer's cards: {dealer_hand} (value: {dealer_value})")
    while dealer_value < 17:
        new_card = deal_card(cards, suits)
        dealer_hand.append(new_card)
        dealer_value = calculate_value(dealer_hand)
        print(f"Dealer draws: {new_card} (value: {dealer_value})")

    #who win
    if dealer_value > 21:
        print("Dealer busts! You win.")
        user_money += bet * 2  # Winning the bet
    elif player_value > dealer_value:
        print(f"You win! Your {player_value} beats the dealer's {dealer_value}.")
        user_money += bet * 2
    elif player_value < dealer_value:
        print(f"Dealer wins with {dealer_value} against your {player_value}.")
    else:
        print(f"It's a tie! Both you and the dealer have {player_value}.")
        user_money += bet  # Tie returns the bet
    return replay_blackjack(username, user_money, mainmenu)

def replay_blackjack(username, user_money, mainmenu):
    if user_money == 0:
        print('\u001b[33mYou can’t play blackjack because you’re BROKE.\u001b[0m')
        input('Press enter to continue')
        clear_screen()
        return user_money  #Return to main menu with updated money
    else:
        replay_blacky = input(f"{username}, would you like to play again? [y] or [n]: ").lower()
        if replay_blacky == 'y':
            clear_screen()
            return Blacky(username, user_money, mainmenu)
        elif replay_blacky == 'n':
            backtomenu = input("Return to the menu or end the game? Type 'menu' or 'end': ").lower()
            if backtomenu == 'menu':
                clear_screen()
                return user_money  #Return to the main menu with updated money
            elif backtomenu == 'end':
                exit()