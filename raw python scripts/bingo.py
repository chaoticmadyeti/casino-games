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

# All 99 bots playing

total_bot_num = 9

bot_id = list(range(0, total_bot_num))
bots = [f"Bot {id + 1}" for id in bot_id]
bot_cards = [None] * total_bot_num
bot_tokens = [None] * total_bot_num

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
    player_card = create_cards()
    card_tokens = [12]

    for i in bot_id:
        bot_cards[i] = create_cards()
        bot_tokens[i] = [12]

    current_numbers = all_numbers.copy()

    winner = False

    # Core number pulling logic

    while not check_bingo(card_tokens):
        for i in bot_id:
            if check_bingo(bot_tokens[i]):
                print(f"Bot {i + 1} won!")
                display_card(bot_cards[i], bot_tokens[i])
                winner = True
        
        if winner:
            break

        current_number = random.randint(0, len(current_numbers) - 1)
        card_tokens = mark_token(card_tokens, current_numbers[current_number], player_card)
        print(current_numbers[current_number])
        for i in bot_id:
            bot_tokens[i] = mark_token(bot_tokens[i], current_numbers[current_number], bot_cards[i])
        current_numbers.pop(current_number)

        display_card(player_card, card_tokens)

        input("")

        if check_bingo(card_tokens):
            print("You won!")
            break


bingo()