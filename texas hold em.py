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

# Player class

class player:
    def __init__(self, id, hole_cards, score):
        self.id = id # ID number 1 will be the human player.
        self.hole_cards = hole_cards
        self.score = score

deck = [card(suit=s, rank=r) for s in suits for r in ranks]

bot_list = ["Robert", "Patrick", "John", "Harry"]
bot_money = [1000, 1000, 1000, 1000] # Will randomise both names and money amounts at start of game, these are just placeholder

money = 0

content = ''

with open("money.txt", "r") as f:
    content = f.read()

if content.isdigit():
    money = int(content)
else:
    print("Please put a positive integer in 'money.txt'")
    sys.exit()

# Find value of the cards

def eval_hand(cards):
    pass

# Rank all players from best to worst (we need to rank all players to deal with side pots down the line)

def find_winner(community_cards, players):
    pass

# Core betting logic

def texas_hold_em():
    pass

texas_hold_em()