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
    print(f"YOUR BET: {bet_type} | BET: ${bet}")
    print(f"----------------------------------------------------------------------")
    print(f"PLAYER CARDS: ", end="", flush=True)
    if player_hand == []:
        print("??, ?? (VALUE: ?)")
    else:
        for i in range(len(player_hand) - 1):
            print(f"{player_hand[i]}, ", end="", flush=True)
        print(f"{player_hand[-1]} (VALUE: {hand_calc(player_hand)})") # forgot array[-1] existed too accustomed to c++ (reminder to use -1 index from now on)
    print(f"BANK CARDS: ", end="", flush=True)
    if bank_hand == []:
        print("??, ?? (VALUE: ?)")
    else:
        for i in range(len(bank_hand) - 1):
            print(f"{bank_hand[i]}, ", end="", flush=True)
        print(f"{bank_hand[-1]} (VALUE: {hand_calc(bank_hand)})")
    print(f"----------------------------------------------------------------------")

# Determine value of a card

def val_calc(card):
    pass

# Determine value of hand

def hand_calc(hand):
    pass

# Main logic

def baccarat():
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

    bet = 0
    bet_type = ""

    print("What do you want to bet on? (Type 'exit' to quit)")
    bet_type = input("Choice: ")
    while bet_type.lower() not in ["player", "banker", "tie"]:
        if bet_type.lower() == 'exit':
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        print("Please choose either 'player', 'banker', or 'tie'. What do you want to bet on? (Type 'exit' to quit)")
        bet_type = input("Choice: ")
    
    print("How much do you want to bet on that?")
    bet = input("$")
    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if not bet.isdigit():
            print(f"Please input a positive integer. How much do you want to bet on that?")
            bet = input("$")
        elif int(bet) <= money:
            print(f"Please input a positive integer. How much do you want to bet on that?")
            bet = input("$")
        else:
            print(f"You do not have enough money. How much do you want to bet on that?")
            bet = input("$")
    bet = int(bet)