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

reel_1 = ["🍒", "🍒", "🍒", "🍋", "🍋", "🍊", "🍊", "🍇", "🍫", "7️⃣"]
reel_2 = ["🍒", "🍒", "🍋", "🍋", "🍋", "🍊", "🍊", "🍇", "🍫", "7️⃣"]
reel_3 = ["🍒", "🍒", "🍋", "🍋", "🍊", "🍊", "🍊", "🍇", "🍫", "7️⃣"]

# Payouts (for future reference):
# 1 Cherry - money back
# 2 Cherry - 2x
# 3 Cherry - 5x
# 3 Lemon - 10x
# 3 Orange - 15x
# 3 Grape - 20x
# 3 Bar - 50x
# 3 7 - 100x

# Scrolling machine

def machine_spin():
    pass

# Interface for the machine

def interface(money, bet):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"SLOTS | BALANCE: {money} | BET: {bet}")
    print(f"----------------------------------------------------------------------")
    # Betting, as well as the machine spin

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