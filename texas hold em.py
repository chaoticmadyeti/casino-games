import random
import time
import sys

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]