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

# Check four of a kind

def four_of_a_kind(frequency):
    for i in frequency:
        if i == 4:
            return True
    return False

# Check three of a kind

def three_of_a_kind(frequency):
    for i in frequency:
        if i == 3:
            return True
    return False

# Check two pair

def two_pair(frequency):
    cnt = 0
    for i in frequency:
        if i == 2:
            cnt += 1
    return cnt >= 2

# Check pair

def pair(frequency):
    for i in frequency:
        if i == 2:
            return True
    return False

def get_rank_of_size(frequency, target_num):
    for i in range(len(frequency)):
        if frequency[i] == target_num:
            return i

# Find value of the cards

def eval_hand(cards):
    rank_frequency = card_frequency(cards)
    if flush(cards) and straight(cards):
        # Straight Flush (includes Royal Flush)
        return [9, cards[0]]
    elif four_of_a_kind(rank_frequency):
        # Four of a kind
        four_of_a_kind_card = get_rank_of_size(rank_frequency, 4)
        kicker = get_rank_of_size(rank_frequency, 1)
        return [8, four_of_a_kind_card, kicker]
    elif three_of_a_kind(rank_frequency) and pair(rank_frequency):
        # Full House
        three_of_a_kind_card = get_rank_of_size(rank_frequency, 3)
        pair_card = get_rank_of_size(rank_frequency, 2)
        return [7, three_of_a_kind_card, pair_card]
    elif flush(cards):
        # Flush
        return [6, cards[0].rank, cards[1].rank, cards[2].rank, cards[3].rank, cards[4].rank]
    elif straight(cards):
        # Straight
        return [5, cards[0].rank]
    elif three_of_a_kind(rank_frequency):
        # Three of a kind
        three_of_a_kind_card = get_rank_of_size(rank_frequency, 3)
        hand_value = [4, three_of_a_kind_card]
        for card in cards:
            if card.rank != three_of_a_kind_card:
                hand_value.append(card.rank)
        return hand_value
    elif two_pair(rank_frequency):
        # Two pair
        lower_pair_card = get_rank_of_size(rank_frequency, 2)
        rank_frequency.reverse()
        higher_pair_card = get_rank_of_size(rank_frequency, 2)
        rank_frequency.reverse()
        kicker = get_rank_of_size(rank_frequency, 1)
        return [3, higher_pair_card, lower_pair_card, kicker]
    elif pair(rank_frequency):
        # Pair
        pair_card = get_rank_of_size(rank_frequency, 2)
        hand_value = [2, pair_card]
        for card in cards:
            if card.rank != pair_card:
                hand_value.append(card.rank)
        return hand_value
    else:
        # High Card
        return [1, cards[0].rank, cards[1].rank, cards[2].rank, cards[3].rank, cards[4].rank]


# Rank all players from best to worst (we need to rank all players to deal with side pots down the line)

def find_winner(community_cards, players):
    for player in players:
        all_cards = community_cards + player.hole_cards
        all_cards.sort(key = lambda card: card.rank, reverse=True)

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