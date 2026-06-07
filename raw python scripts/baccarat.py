import random
import os
import sys

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(exe_dir)

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']
deck = [f"{rank}{suit}" for suit in suits for rank in ranks]

# Array of choices for bank's third card (d is draw, h is no draw)

bank_third_card_choice = [
    ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'] ,
    ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'] ,
    ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'] ,
    ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'h', 'd'] ,
    ['h', 'h', 'd', 'd', 'd', 'd', 'd', 'd', 'h', 'h'] ,
    ['h', 'h', 'h', 'h', 'd', 'd', 'd', 'd', 'h', 'h'] ,
    ['h', 'h', 'h', 'h', 'h', 'h', 'd', 'd', 'h', 'h'] ,
    ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'] ,
]

content = ''
money = 0

with open("money.txt", "r") as f:
    content = f.read()

if content.isdigit():
    money = int(content)
else:
    print("Please put a positive integer in 'money.txt'")
    sys.exit()

# Interface for the table

def interface(player_hand, bank_hand, money, bet, bet_type):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"BACCARACT - PUNTO BANCO | YOUR BALANCE: ${money}")
    print(f"----------------------------------------------------------------------")
    print(f"YOUR BET: {bet_type.upper()} | BET: ${bet}")
    print(f"----------------------------------------------------------------------")
    print(f"PLAYER CARDS: ", end="", flush=True)
    if player_hand == []:
        print("??, ?? (VALUE: ?)")
    else:
        for i in range(len(player_hand) - 1):
            print(f"{player_hand[i]}, ", end="", flush=True)
        print(f"{player_hand[-1]} (VALUE: {hand_calc(player_hand)})") # forgot array[-1] existed too accustomed to c++ (reminder to use -1 index from now on)
    print(f"BANKER CARDS: ", end="", flush=True)
    if bank_hand == []:
        print("??, ?? (VALUE: ?)")
    else:
        for i in range(len(bank_hand) - 1):
            print(f"{bank_hand[i]}, ", end="", flush=True)
        print(f"{bank_hand[-1]} (VALUE: {hand_calc(bank_hand)})")
    print(f"----------------------------------------------------------------------")

# Determine value of a card

def val_calc(card):
    if card[0] == 'A':
        return 1
    elif card[0] == '2':
        return 2
    elif card[0] == '3':
        return 3
    elif card[0] == '4':
        return 4
    elif card[0] == '5':
        return 5
    elif card[0] == '6':
        return 6
    elif card[0] == '7':
        return 7
    elif card[0] == '8':
        return 8
    elif card[0] == '9':
        return 9
    else:
        return 0

# Determine value of hand

def hand_calc(hand):
    value = 0
    for card in hand:
        value += val_calc(card)
    value = value % 10
    return value

# Main logic

def baccarat():
    global money

    current_deck = deck.copy()

    player_hand = []
    bank_hand = []

    card = random.randint(0, len(current_deck) - 1)
    player_hand.append(current_deck[card])
    current_deck.pop(card)
    card = random.randint(0, len(current_deck) - 1)
    player_hand.append(current_deck[card])
    current_deck.pop(card)

    card = random.randint(0, len(current_deck) - 1)
    bank_hand.append(current_deck[card])
    current_deck.pop(card)
    card = random.randint(0, len(current_deck) - 1)
    bank_hand.append(current_deck[card])
    current_deck.pop(card)

    player_value = hand_calc(player_hand)
    bank_value = hand_calc(bank_hand)

    bet = 0
    bet_type = ""

    interface([], [], money, "??", "??")
    print("What do you want to bet on? (Type 'exit' to quit)")
    bet_type = input("Choice: ")
    while bet_type.lower() not in ["player", "banker", "tie"]:
        if bet_type.lower() == 'exit':
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        interface([], [], money, "??", "??")
        print("Please choose either 'player', 'banker', or 'tie'. What do you want to bet on? (Type 'exit' to quit)")
        bet_type = input("Choice: ")
    
    interface([], [], money, "??", bet_type)
    print("How much do you want to bet on that?")
    bet = input("$")
    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if not bet.isdigit():
            interface([], [], money, "??", bet_type)
            print(f"Please input a positive integer. How much do you want to bet on that?")
            bet = input("$")
        elif int(bet) <= money:
            interface([], [], money, "??", bet_type)
            print(f"Please input a positive integer. How much do you want to bet on that?")
            bet = input("$")
        else:
            interface([], [], money, "??", bet_type)
            print(f"You do not have enough money. How much do you want to bet on that?")
            bet = input("$")
    bet = int(bet)

    # Checking who will draw another card

    interface(player_hand, bank_hand, money, bet, bet_type)
    if player_value >= 8 or bank_value >= 8:
        print("Cards have been dealt. No one will draw cards.")
        input("Press Enter to continue...")
    elif player_value <= 5:
        print("Cards have been dealt. The player will draw a card.")
        input("Press Enter to continue...")
        card = random.randint(0, len(current_deck) - 1)
        third_card = current_deck[card]
        player_hand.append(current_deck[card])
        current_deck.pop(card)
        player_value = hand_calc(player_hand)
        if bank_third_card_choice[bank_value][val_calc(third_card)] == 'd':
            interface(player_hand, bank_hand, money, bet, bet_type)
            print("The player has drawn their card. The banker will draw a card.")
            input("Press enter to continue...")
            card = random.randint(0, len(current_deck) - 1)
            bank_hand.append(current_deck[card])
            current_deck.pop(card)
            bank_value = hand_calc(bank_hand)
            interface(player_hand, bank_hand, money, bet, bet_type)
            print("The banker has drawn their card.")
            input("Press enter to continue...")
        else:
            print("The player has drawn their card. The banker will not draw a card")
            input("Press enter to continue...")
    elif bank_value <= 5:
        print("Cards have been dealt. The banker will draw a card. ")
        input("Press Enter to continue...")
        card = random.randint(0, len(current_deck) - 1)
        bank_hand.append(current_deck[card])
        current_deck.pop(card)
        bank_value = hand_calc(bank_hand)
        interface(player_hand, bank_hand, money, bet, bet_type)
        print("The banker has drawn their card.")
        input("Press Enter to continue...")
    else:
        print("Cards have been dealt. No one will draw cards.")
        input("Press Enter to continue...")
    
    winner = ''
    if player_value > bank_value:
        winner = "player"
    elif player_value < bank_value:
        winner = "banker"
    else:
        winner = "tie"
    
    interface(player_hand, bank_hand, money, bet, bet_type)
    if winner.lower() == bet_type.lower():
        if bet_type.lower() == "banker":
            print("You win! A commision (5%) will be taken from your banker bet.")
            money += (bet // 20) * 19
            input("Press Enter to continue...")
        elif bet_type.lower() == "player":
            print("You win!")
            money += bet
            input("Press Enter to continue...")
        else:
            print("You win!")
            money += bet * 7
            input("Press Enter to continue...")
    elif winner.lower() != "tie":
        print("It's a tie! Nothing happens.")
        input("Press Enter to continue...")
    else:
        print("You lose!")
        money -= bet
        input("Press Enter to continue...")


print("Hello! Welcome to Python Baccarat!")
print("If you don't know how to play, please learn beforehand. This game uses 'punto banco' rules.")
input("Press Enter to play...")

while money > 0:
    baccarat()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")