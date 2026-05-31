import random
import time
import sys
import itertools

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
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

# Score will be 1 - 9 depending on the value of the hand, and all other elements in the list will be tiebreaker / kicker cards

deck = [card(suit=s, rank=r) for s in suits for r in rank_value]

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

# Check straight

def straight(cards):
    card_ranks = []
    for card in cards:
        card_ranks.append(card.rank)
    if card_ranks == [12, 3, 2, 1, 0]:
        return True
    for i in range(len(card_ranks) - 1):
        if card_ranks[i] != card_ranks[i + 1] + 1:
            return False
    return True

# Check flush

def flush(cards):
    for card in cards:
        if card.suit != cards[0].suit:
            return False
    return True

# Check rank frequences (needed for three of a kind etc.)

def card_frequency(cards):
    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in cards:
        frequency[card.rank] += 1
    return frequency

# Find value of the cards

def eval_hand(cards):
    pass

# Rank all players from best to worst (we need to rank all players to deal with side pots down the line)

def find_winner(community_cards, players):
    for player in players:
        all_cards = community_cards + player.hole_cards
        combinations = itertools.combinations(all_cards, 5)

        best_score = [0]

        for combination in combinations:
            current_score = eval_hand(combination)
            for i in range(len(current_score)):
                if current_score[i] > best_score[i]:
                    best_score = current_score
                    break
        
        player.score = best_score

    sorted_players = sorted(players, reverse=True)

    return sorted_players


# Core betting logic

def texas_hold_em():
    pass

texas_hold_em()