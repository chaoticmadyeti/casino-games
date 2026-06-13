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

# Reels

reel_1 = ["🍒", "--", "🍒", "--", "🍒", "--", "🍋", "--", "🍋", "--", "🍊", "--", "🍊", "--", "🍇", "--", "🍫", "--", "🍀", "--"]
reel_2 = ["🍒", "--", "🍒", "--", "🍋", "--", "🍋", "--", "🍋", "--", "🍊", "--", "🍊", "--", "🍇", "--", "🍫", "--", "🍀", "--"]
reel_3 = ["🍒", "--", "🍒", "--", "🍋", "--", "🍋", "--", "🍊", "--", "🍊", "--", "🍊", "--", "🍇", "--", "🍫", "--", "🍀", "--"]

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
    reel_1_idx = random.randint(0, 19)
    reel_2_idx = random.randint(0, 19)
    reel_3_idx = random.randint(0, 19)

    reel_1_amount = random.randint(50, 70)
    reel_2_amount = reel_1_amount + 5
    reel_3_amount = reel_2_amount + 5

    cnt = 0

    while cnt < reel_3_amount:

        os.system('cls' if os.name == 'nt' else 'clear')
        cnt += 1

        if cnt < reel_1_amount:
            print(f"{reel_1[(reel_1_idx + cnt - 2) % 20]}", end="", flush=True)
        else:
            print(f"{reel_1[(reel_1_idx + reel_1_amount - 2) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_2_amount:
            print(f"{reel_2[(reel_2_idx + cnt - 2) % 20]}", end="", flush=True)
        else:
            print(f"{reel_2[(reel_2_idx + reel_2_amount - 2) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_3_amount:
            print(f"{reel_3[(reel_3_idx + cnt - 2) % 20]}", end="", flush=True)
        else:
            print(f"{reel_3[(reel_3_idx + reel_3_amount - 2) % 20]}", end="", flush=True)
        
        print("\n")

        if cnt < reel_1_amount:
            print(f"{reel_1[(reel_1_idx + cnt - 1) % 20]}", end="", flush=True)
        else:
            print(f"{reel_1[(reel_1_idx + reel_1_amount - 1) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_2_amount:
            print(f"{reel_2[(reel_2_idx + cnt - 1) % 20]}", end="", flush=True)
        else:
            print(f"{reel_2[(reel_2_idx + reel_2_amount - 1) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_3_amount:
            print(f"{reel_3[(reel_3_idx + cnt - 1) % 20]}", end="", flush=True)
        else:
            print(f"{reel_3[(reel_3_idx + reel_3_amount - 1) % 20]}", end="", flush=True)
        
        print("\n")

        if cnt < reel_1_amount:
            print(f"{reel_1[(reel_1_idx + cnt) % 20]}", end="", flush=True)
        else:
            print(f"{reel_1[(reel_1_idx + reel_1_amount) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_2_amount:
            print(f"{reel_2[(reel_2_idx + cnt) % 20]}", end="", flush=True)
        else:
            print(f"{reel_2[(reel_2_idx + reel_2_amount) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_3_amount:
            print(f"{reel_3[(reel_3_idx + cnt) % 20]}", end="", flush=True)
        else:
            print(f"{reel_3[(reel_3_idx + reel_3_amount) % 20]}", end="", flush=True)
        
        print("\n")

        if cnt < reel_1_amount:
            print(f"{reel_1[(reel_1_idx + cnt + 1) % 20]}", end="", flush=True)
        else:
            print(f"{reel_1[(reel_1_idx + reel_1_amount + 1) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_2_amount:
            print(f"{reel_2[(reel_2_idx + cnt + 1) % 20]}", end="", flush=True)
        else:
            print(f"{reel_2[(reel_2_idx + reel_2_amount + 1) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_3_amount:
            print(f"{reel_3[(reel_3_idx + cnt + 1) % 20]}", end="", flush=True)
        else:
            print(f"{reel_3[(reel_3_idx + reel_3_amount + 1) % 20]}", end="", flush=True)
        
        print("\n")

        if cnt < reel_1_amount:
            print(f"{reel_1[(reel_1_idx + cnt + 2) % 20]}", end="", flush=True)
        else:
            print(f"{reel_1[(reel_1_idx + reel_1_amount + 2) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_2_amount:
            print(f"{reel_2[(reel_2_idx + cnt + 2) % 20]}", end="", flush=True)
        else:
            print(f"{reel_2[(reel_2_idx + reel_2_amount + 2) % 20]}", end="", flush=True)
        print(" | ", end="", flush=True)
        if cnt < reel_3_amount:
            print(f"{reel_3[(reel_3_idx + cnt + 2) % 20]}", end="", flush=True)
        else:
            print(f"{reel_3[(reel_3_idx + reel_3_amount + 2) % 20]}", end="", flush=True)
        
        print("\n")

        time.sleep(0.07)
        # sys.stdout.write('\x1b[5A\x1b[J')
        # sys.stdout.flush()

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

# print("Hello! Welcome to Python Slots!")
# print("If you don't know how to play, please learn beforehand. This game uses custom made reels.")
# input("Press Enter to play...")

# while money > 0:
    # slots()

# with open("money.txt", "w") as f:
    # f.write(str(money))

# print("You ran out of money. Please go to 'money.txt' to reset.")

machine_spin()