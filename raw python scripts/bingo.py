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

def mark_token(card_tokens, number_called, card):
    if number_called in card:
        grid_index = card.index(number_called)
        card_tokens.append(grid_index)
    return card_tokens

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

def bingo():
    player_card = create_cards()
    card_tokens = [12]

    current_numbers = all_numbers.copy()

    print(f"{player_card[0]} {player_card[1]} {player_card[2]} {player_card[3]} {player_card[4]}")
    print(f"{player_card[5]} {player_card[6]} {player_card[7]} {player_card[8]} {player_card[9]}")
    print(f"{player_card[10]} {player_card[11]} {player_card[12]} {player_card[13]} {player_card[14]}")
    print(f"{player_card[15]} {player_card[16]} {player_card[17]} {player_card[18]} {player_card[19]}")
    print(f"{player_card[20]} {player_card[21]} {player_card[22]} {player_card[23]} {player_card[24]}")

    while not check_bingo(card_tokens):
        current_number = random.randint(0, len(current_numbers) - 1)
        mark_token(card_tokens, current_numbers[current_number], player_card)
        print(current_numbers[current_number])
        current_numbers.pop(current_number)


bingo()