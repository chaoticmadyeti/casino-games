import random
import os
import sys

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

# Reels

reel_1 = ["🍒", "🍒", "🍒", "🍒", "🍋", "🍋", "🍋", "🍊", "🍇", "🍫"]
reel_2 = ["🍒", "🍒", "🍒", "🍒", "🍋", "🍋", "🍊", "🍊", "🍇", "🍫"]
reel_3 = ["🍒", "🍒", "🍒", "🍋", "🍋", "🍋", "🍊", "🍊", "🍇", "🍫"]

# Payouts (for future reference):
# 2 Cherry - money back
# 3 Cherry - 2x
# 3 Lemon - 3x
# 3 Orange - 5x
# 3 Plum/Grape - 10x
# 3 Bar - 20x

# Interface for the machine

def interface():
    pass

# Main slots logic

def slots():
    pass

print("Hello! Welcome to Python Slots!")
print("If you don't know how to play, please learn beforehand. This game uses custom made reels.")
input("Press Enter to play...")

while money > 0:
    slots()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")