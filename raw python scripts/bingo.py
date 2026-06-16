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

numbers_b = range(1, 16)
numbers_i = range(16, 31)
numbers_n = range(31, 46)
numbers_g = range(46, 61)
numbers_o = range(61, 76)

def create_cards():
    card = [[], [], [], [], []]

    curr_numbers_b = numbers_b.copy()
    for _ in range(5):
        number = random.randint(0, 14)
        card[0].append(curr_numbers_b[number])
        curr_numbers_b.pop(card)
    
    curr_numbers_i = numbers_i.copy()
    for _ in range(5):
        number = random.randint(0, 14)
        card[1].append(curr_numbers_i[number])
        curr_numbers_i.pop(card)
    
    curr_numbers_n = numbers_n.copy()
    for _ in range(5):
        number = random.randint(0, 14)
        card[2].append(curr_numbers_n[number])
        curr_numbers_n.pop(card)
    
    curr_numbers_g = numbers_g.copy()
    for _ in range(5):
        number = random.randint(0, 14)
        card[3].append(curr_numbers_g[number])
        curr_numbers_g.pop(card)
    
    curr_numbers_o = numbers_o.copy()
    for _ in range(5):
        number = random.randint(0, 14)
        card[4].append(curr_numbers_o[number])
        curr_numbers_o.pop(card)
    
    card[2][2] = "FREE"

    return card
    
def bingo():
    pass