import random
import time
import sys
import itertools

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

# Card class

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

deck = [card(suit=s, rank=r) for s in suits for r in ranks]

money = 0

content = ''

with open("money.txt", "r") as f:
    content = f.read()

if content.isdigit():
    money = int(content)
else:
    print("Please put a positive integer in 'money.txt'")
    sys.exit()

# Check hand and community cards combination

def royal_flush(cards):
    pass

def straight_flush(cards):
    pass

def four_of_a_kind(cards):
    pass

def full_house(cards):
    pass

def flush(cards):
    pass

def straight(cards):
    pass

def three_of_a_kind(cards):
    pass

def two_pair(cards):
    pass

def pair(cards):
    pass

# Find hand value

def check_value(cards):
    pass

# Check who wins

def showdown(all_player_hands): 
    # all_player_hands is an array of all players at the end

    # Call check_value() on every hand and determine who wins
    pass

# Handle money

def bet_handling(pots): 
    # Array of all pots, includes side pots
    # Determine who gets how much money
    pass

# Core loop

def texas_hold_em():
    # Handles the dealing of cards, betting in each round etc. (aka all of the text stuff that actually shows up on screen)
    # All above functions are no-text (no print() functions)
    pass

texas_hold_em()