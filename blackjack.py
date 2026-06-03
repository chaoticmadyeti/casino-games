import random
import time
import sys
import os

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']
deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
num_of_ace_player = 0
num_of_ace_dealer = 0

content = ''

with open("money.txt", "r") as f:
    content = f.read()

if content.isdigit():
    money = int(content)
else:
    print("Please put a positive integer in 'money.txt'")
    sys.exit()

def value_calc(i, person):
    global num_of_ace_player
    global num_of_ace_dealer
    val = 0
    if i == '2':
        val += 2
    elif i == '3':
        val += 3
    elif i == '4':
        val += 4
    elif i == '5':
        val += 5
    elif i == '6':
        val += 6
    elif i == '7':
        val += 7
    elif i == '8':
        val += 8
    elif i == '9':
        val += 9
    elif i == 'A':
        val += 11
        if person == "player":
            num_of_ace_player += 1
        else:
            num_of_ace_dealer += 1
    else:
        val += 10
    return val

# Interface for the table (placeholder information for now)

def interface(bet, player_hand, dealer_hand, money, situation):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"BlACKJACK | BET: ${bet} | YOUR BALANCE: ${money}")
    print(f"----------------------------------------------------------------------")
    if situation == "bet":
        print(f"DEALER CARDS: ??, ??")
        print(f"YOUR CARDS: ??, ??")
    else:
        if situation != "end":
            print(f"DEALER CARDS: {dealer_hand[0]}, ??")
        else:
            print(f"DEALER CARDS: ", end="", flush=True)
            for card in range(len(dealer_hand) - 1):
                print(f"{dealer_hand[card]}, ", end="", flush=True)
            print(f"{dealer_hand[len(dealer_hand) - 1]}")
        print(f"YOUR CARDS: ", end="", flush=True)
        for card in range(len(player_hand) - 1):
            print(f"{player_hand[card]}, ", end="", flush=True)
        print(f"{player_hand[len(player_hand) - 1]}")
    print(f"----------------------------------------------------------------------")

def blackjack():
    global money
    global deck
    global num_of_ace

    current_deck = deck.copy()
    player_hand = []
    dealer_hand = []
    num_of_ace_player = 0
    num_of_ace_dealer = 0
    player_blackjack = False
    dealer_blackjack = False

    # Bet handling

    bet = 0

    interface("??", [], [], money, "bet")

    print(f"How much do you want to bet? (Type 'exit' to quit)")
    bet = input("$")
    
    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if bet.lower() == "exit":
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        if not bet.isdigit():
            interface("??", [], [], money, "bet")
            print(f"Please input a positive integer. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
        elif int(bet) <= money:
            interface("??", [], [], money, "bet")
            print(f"Please input a positive integer. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
        else:
            interface("??", [], [], money, "bet")
            print(f"You do not have enough money. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
    bet = int(bet)

    # Player hand generation

    card = random.randint(0, len(current_deck) - 1)
    player_hand.append(current_deck[card])
    current_deck.pop(card)
    card = random.randint(0, len(current_deck) - 1)
    player_hand.append(current_deck[card])
    current_deck.pop(card)

    player_value = 0
    for i in player_hand:
        player_value += value_calc(i[0], "player")
    
    if player_value == 21:
        player_blackjack = True

    # Dealer hand generation

    card = random.randint(0, len(current_deck) - 1)
    dealer_hand.append(current_deck[card])
    current_deck.pop(card)
    card = random.randint(0, len(current_deck) - 1)
    dealer_hand.append(current_deck[card])
    current_deck.pop(card)

    dealer_value = 0
    for i in dealer_hand:
        dealer_value += value_calc(i[0], "dealer")
    
    if dealer_value == 21:
        dealer_blackjack = True

    # Dealing and revealing to the player

    interface(bet, player_hand, dealer_hand, money, "drawing")

    print("Cards have been drawn (see above).")
    print(f"Your hand is of value {player_value}.")
    input("Press Enter to continue... ")

    if player_blackjack:
        print("Blackjack!")
        bet = bet // 2 * 3
    else:

        # Handling insurance

        if dealer_hand[0][0] == 'A':
            interface(bet, player_hand, dealer_hand, money, "insurance")
            print("Would you like to pay for insurance? (Y/N)")
            insurance_choice = input("Choice: ")
            while insurance_choice.upper() != 'Y' and insurance_choice.upper() != 'N':
                interface(bet, player_hand, dealer_hand, money, "insurance")
                print("Please input either 'Y' or 'N'. Would you like to pay for insurance? (Y/N)")
                insurance_choice = input("Choice: ")
            if insurance_choice.upper() == 'Y':
                if dealer_blackjack:
                    interface(bet, player_hand, dealer_hand, money, "end")
                    print("The dealer had a blackjack! Your insurance paid off.")
                    input("Press Enter to continue... ")
                    return
                else:
                    interface(bet, player_hand, dealer_hand, money, "insurance")
                    print(f"The dealer doesn't have a blackjack. Your insurance (${bet // 2}) is lost.")
                    input("Press Enter to continue... ")
                    money -= bet // 2


        # Handling doubling

        interface(bet, player_hand, dealer_hand, money, "doubling")
        double = False
        if bet <= money // 2:
            print("Do you want to double (Y/N)?")
            double_choice = input("Choice: ")
            while double_choice.upper() != 'Y' and double_choice.upper() != 'N':
                interface(bet, player_hand, dealer_hand, money, "doubling")
                print("Please input either 'Y' or 'N'. Do you want to double (Y/N)?")
                double_choice = input("Choice: ")
            if double_choice.upper() == 'Y':
                bet = bet * 2
                double = True
        else:
            print("You do not have enough money to double.")
            input("Press Enter to continue... ")

        # Hitting and standing 

        if double:
            interface(bet, player_hand, dealer_hand, money, "hit_and_stand")
            card = random.randint(0, len(current_deck) - 1)
            player_hand.append(current_deck[card])
            player_value += value_calc(current_deck[card][0], "player")
            print(f"You drew a {current_deck[card]}.")
            current_deck.pop(card)
            if player_value > 21 and num_of_ace_player > 0:
                player_value -= 10
                num_of_ace_player -= 1
            if num_of_ace_player > 0:
                print(f"Your hand is of value {player_value} / {player_value - 10}.")
            else:
                print(f"Your hand is of value {player_value}.")
        else:
            hit_or_stand = ''
            while player_value <= 21:
                interface(bet, player_hand, dealer_hand, money, "hit_and_stand")
                print("Hit or stand?")
                hit_or_stand = input("Choice: ")
                while hit_or_stand.lower() != 'hit' and hit_or_stand.lower() != 'stand':
                    interface(bet, player_hand, dealer_hand, money, "hit_and_stand")
                    print("Please input either 'hit' or 'stand'. Hit or stand?")
                    hit_or_stand = input("Choice: ")
                if hit_or_stand.lower() == 'hit':
                    card = random.randint(0, len(current_deck) - 1)
                    player_hand.append(current_deck[card])
                    player_value += value_calc(current_deck[card][0], "player")
                    interface(bet, player_hand, dealer_hand, money, "hit_and_stand")
                    print(f"You drew a {current_deck[card]}.")
                    current_deck.pop(card)
                    if player_value > 21 and num_of_ace_player > 0:
                        player_value -= 10
                        num_of_ace_player -= 1
                    if num_of_ace_player > 0:
                        print(f"Your hand is of value {player_value} / {player_value - 10}.")
                    else:
                        print(f"Your hand is of value {player_value}.")
                    input("Press Enter to continue... ")
                else:
                    break

        if player_value > 21:
            money = money - bet
            interface(bet, player_hand, dealer_hand, money, "end")
            print(f"You bust! You lost ${bet}.")
            input("Press Enter to continue... ")
            return

    # Dealer reveal and draw

    interface(bet, player_hand, dealer_hand, money, "end")
    print(f"The dealers other card is {dealer_hand[1]}")
    print(f"The dealer's hand is of value {dealer_value}.")
    input("Press Enter to continue... ")
    while dealer_value <= 17:
        card = random.randint(0, len(current_deck) - 1)
        dealer_hand.append(current_deck[card])
        dealer_value += value_calc(current_deck[card][0], "dealer")
        if dealer_value > 21 and num_of_ace_dealer > 0:
            dealer_value -= 10
            num_of_ace_dealer -= 1
        interface(bet, player_hand, dealer_hand, money, "end")
        print(f"The dealer drew a {current_deck[card]}")
        print(f"The dealer's hand is of value {dealer_value}.")
        input("Press Enter to continue... ")
        current_deck.pop(card)

    if dealer_value > 21:
        print(f"The dealer bust! You won ${bet}.")
        input("Press Enter to continue... ")
        money = money + bet
        return

    # Win check

    interface(bet, player_hand, dealer_hand, money, "end")
    if dealer_blackjack and player_blackjack:
        print("You tied! Nothing happens.")
        input("Press Enter to continue... ")
    elif dealer_blackjack:
        print(f"You lost! You lost ${bet}.")
        input("Press Enter to continue... ")
        money = money - bet
    elif dealer_value > player_value:
        print(f"You lost! You lost ${bet}.")
        input("Press Enter to continue... ")
        money = money - bet
    elif dealer_value < player_value:
        print(f"You won! You won ${bet}.")
        input("Press Enter to continue... ")
        money = money + bet
    else:
        print("You tied! Nothing happens.")
        input("Press Enter to continue... ")

# Main blackjack logic:

print("Hello! Welcome to Python Blackjack.")
print("If you don't know how to play blackjack, I highly suggest you do. This game goes by American rules.")
print("Note: Cents do not exist in this game. All decimals will be rounded down, to favour the house.")

while money > 0:
    blackjack()

with open("money.txt", "w") as f:
    f.write("0")

print("You ran out of money. Please go to 'money.txt' to reset.")

# To do: splitting