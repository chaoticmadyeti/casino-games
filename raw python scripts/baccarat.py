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

def interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"BACCARACT - PUNTO BANCO | YOUR BALANCE: $500")
    print(f"----------------------------------------------------------------------")
    print(f"YOUR BET: PLAYER | BET: $200")
    print(f"----------------------------------------------------------------------")
    print(f"PLAYER CARDS: ??, ?? (VALUE: ?)")
    print(f"BANK CARDS: ??, ?? (VALUE: ?)")
    print(f"----------------------------------------------------------------------")

# Determine value of a card

def val_calc(card):
    pass

# Determine value of hand

def hand_calc(hand):
    pass

# Main logic

def baccarat():
    pass