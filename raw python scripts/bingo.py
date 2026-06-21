import random
import os
import sys
import time

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(exe_dir)

content = ''
money = 0

with open("money.txt", "r") as f:
    content = f.read()

if content.isdigit():
    money = int(content)
else:
    print("Please put a positive integer in 'money.txt'")
    sys.exit()

all_numbers = list(range(1, 76))
numbers_b = list(range(1, 16))
numbers_i = list(range(16, 31))
numbers_n = list(range(31, 46))
numbers_g = list(range(46, 61))
numbers_o = list(range(61, 76))

# Interface

def interface(bet, jackpot):
    global money

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"BINGO | BET: ${bet} | JACKPOT: ${jackpot} | BALANCE: ${money}")
    print(f"----------------------------------------------------------------------")

# Mark a number if it is called

def mark_token(card_tokens, number_called, card):
    if number_called in card:
        grid_index = card.index(number_called)
        card_tokens.append(grid_index)
    return card_tokens

# Create the cards

def create_cards():
    card = []

    curr_numbers_b = numbers_b.copy()
    for _ in range(5):
        number = random.randint(0, len(curr_numbers_b) - 1)
        card.append(curr_numbers_b[number])
        curr_numbers_b.pop(number)
    
    curr_numbers_i = numbers_i.copy()
    for _ in range(5):
        number = random.randint(0, len(curr_numbers_i) - 1)
        card.append(curr_numbers_i[number])
        curr_numbers_i.pop(number)
    
    curr_numbers_n = numbers_n.copy()
    for _ in range(5):
        number = random.randint(0, len(curr_numbers_n) - 1)
        card.append(curr_numbers_n[number])
        curr_numbers_n.pop(number)
    
    curr_numbers_g = numbers_g.copy()
    for _ in range(5):
        number = random.randint(0, len(curr_numbers_g) - 1)
        card.append(curr_numbers_g[number])
        curr_numbers_g.pop(number)
    
    curr_numbers_o = numbers_o.copy()
    for _ in range(5):
        number = random.randint(0, len(curr_numbers_o) - 1)
        card.append(curr_numbers_o[number])
        curr_numbers_o.pop(number)
    
    card[12] = "FREE"

    return card

# Check for a bingo

winning_lines = [
        {0, 1, 2, 3, 4}, 
        {5, 6, 7, 8, 9},
        {10, 11, 12, 13, 14},
        {15, 16, 17, 18, 19},
        {20, 21, 22, 23, 24},
        {0, 5, 10, 15, 20},
        {1, 6, 11, 16, 21},
        {2, 7, 12, 17, 22},
        {3, 8, 13, 18, 23},
        {4, 9, 14, 19, 24},
        {0, 6, 12, 18, 24},
        {4, 8, 12, 16, 20}
    ]

def check_bingo(card_tokens): # card_tokens is an array of all numbers gotten
    global winning_lines

    for line in winning_lines:
        if line.issubset(card_tokens):
            return True
    
    return False

# Display the card with marked numbers

def display_card(card, card_tokens):
    for i in range(0, 5):
        for j in range(0, 5):
            if i + j * 5 in card_tokens:
                print("\033[32m" + f"{card[i + j * 5]:^4}" + "\033[0m", end="")
            else:
                print(f"{card[i + j * 5]:^4}", end="")
        print("")

# Main bingo logic

def bingo():
    global money

    bet = 0
    jackpot = 0

    interface(bet, jackpot)
    print(f"How much do you want to bet? (Type 'exit' to quit)")
    bet = input("$")
    
    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if bet.lower() == "exit":
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        if not bet.isdigit():
            interface(bet, jackpot)
            print(f"Please input a positive integer. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
        elif int(bet) <= money:
            interface(bet, jackpot)
            print(f"Please input a positive integer. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
        else:
            interface(bet, jackpot)
            print(f"You do not have enough money. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
    bet = int(bet)

    money = money - bet

    interface(bet, jackpot)
    total_bot_num = 0
    print(f"How many bots do you want to play against? (This, and your bet, will determine the jackpot)")
    total_bot_num = input("Number of bots: ")

    while not total_bot_num.isdigit() or int(total_bot_num) <= 0 or int(total_bot_num) > 999:
        if not total_bot_num.isdigit():
            interface(bet, jackpot)
            print(f"Please input a positive integer. How many bots do you want to play against?")
            total_bot_num = input("Number of bots: ")
        elif int(total_bot_num) <= 0:
            interface(bet, jackpot)
            print(f"Please input a positive integer. How many bots do you want to play against?")
            total_bot_num = input("Number of bots: ")
        else:
            interface(bet, jackpot)
            print(f"The maximum amount of bots is 999. How many bots do you want to play against?")
            total_bot_num = input("Number of bots: ")

    total_bot_num = int(total_bot_num)

    jackpot = bet * (total_bot_num + 1)

    bot_id = list(range(0, total_bot_num))
    bot_cards = [None] * total_bot_num
    bot_tokens = [None] * total_bot_num 

    player_card = create_cards()
    card_tokens = [12]

    for i in bot_id:
        bot_cards[i] = create_cards()
        bot_tokens[i] = [12]

    current_numbers = all_numbers.copy()

    bot_winner = False

    # Core number pulling logic

    while not check_bingo(card_tokens):
        interface(bet, jackpot)

        current_number = random.randint(0, len(current_numbers) - 1)
        card_tokens = mark_token(card_tokens, current_numbers[current_number], player_card)
        print(f"The caller calls {current_numbers[current_number]}! Your card now:")
        for i in bot_id:
            bot_tokens[i] = mark_token(bot_tokens[i], current_numbers[current_number], bot_cards[i])
        current_numbers.pop(current_number)

        display_card(player_card, card_tokens)

        input("Press Enter to continue...")

        if check_bingo(card_tokens):
            print("You won!")
            input("Press Enter to continue...")
            break

        for i in bot_id:
            if check_bingo(bot_tokens[i]):
                interface(bet, jackpot)
                print(f"Bot {i + 1} won! Bot {i + 1}'s card:")
                display_card(bot_cards[i], bot_tokens[i])
                input("Press Enter to continue...")
                bot_winner = True
        
        if bot_winner:
            break
    
    interface(bet, jackpot)
    if bot_winner:
        print("You lose!")
    else:
        print(f"You won! You won the jackpot of ${jackpot}!")
        money = money + jackpot
    input("Press Enter to continue...")


print("Hello! Welcome to Python Bingo!")
print("Rules for this game are in README.md. Please learn the rules beforehand.")
input("Press Enter to play...")

while money > 0:
    bingo()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")