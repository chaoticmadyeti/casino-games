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

os.system('cls' if os.name == 'nt' else 'clear')

# Reels

reel_1 = ["🍒", "--", "🍋", "--", "🍒", "--", "🍋", "--", "🍫", "--", "🍀", "--", "🍊", "--", "🍇", "--", "🍒", "--", "🍊", "--"]
reel_2 = ["🍇", "--", "🍒", "--", "🍋", "--", "🍀", "--", "🍋", "--", "🍒", "--", "🍊", "--", "🍊", "--", "🍫", "--", "🍋", "--"]
reel_3 = ["🍊", "--", "🍫", "--", "🍇", "--", "🍋", "--", "🍊", "--", "🍋", "--", "🍀", "--", "🍒", "--", "🍒", "--", "🍊", "--"]

# Reel 1: 3 Cherry, 2 Lemon, 2 Orange, 1 Grape, 1 Bar, 1 Clover
# Reel 2: 2 Cherry, 3 Lemon, 2 Orange, 1 Grape, 1 Bar, 1 Clover
# Reel 3: 2 Cherry, 2 Lemon, 3 Orange, 1 Grape, 1 Bar, 1 Clover

# Payouts (for future reference):
# 1 Cherry - money back
# 2 Cherry - 2x
# 3 Cherry - 5x
# 3 Lemon - 10x
# 3 Orange - 15x
# 3 Grape - 20x
# 3 Bar - 50x
# 3 Clover - 100x
# 🍒 🍋 🍊 🍇 🍫 🍀

# Calculate how much you win

def winnings(final_middle):
    cnt = 0
    for i in final_middle:
        if i == "🍒":
            cnt += 1
    if cnt == 1:
        return 1
    elif cnt == 2:
        return 2
    elif cnt == 3:
        return 5
    elif final_middle == ["🍋", "🍋", "🍋"]:
        return 10
    elif final_middle == ["🍊", "🍊", "🍊"]:
        return 15
    elif final_middle == ["🍇", "🍇", "🍇"]:
        return 20
    elif final_middle == ["🍫", "🍫", "🍫"]:
        return 50
    elif final_middle == ["🍀", "🍀", "🍀"]:
        return 100
    else:
        return -1

# Scrolling machine

def machine_spin():

    reel_1_idx = random.randint(0, 19)
    reel_2_idx = random.randint(0, 19)
    reel_3_idx = random.randint(0, 19)

    if reel_1[reel_1_idx] == "--":
        reel_1_idx -= 1
    
    if reel_2[reel_2_idx] == "--":
        reel_2_idx -= 1
    
    if reel_3[reel_3_idx] == "--":
        reel_3_idx -= 1

    reel_1_amount = random.randint(50, 70)
    reel_2_amount = reel_1_amount + random.randint(4, 5)
    reel_3_amount = reel_2_amount + random.randint(4, 5)

    cnt = 0

    while cnt < reel_3_amount:

        sys.stdout.write('\x1b[5A\x1b[J')
        sys.stdout.flush()
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
        
        print("")

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
        
        print("")

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
        
        print("")

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
        
        print("")

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
        
        print("")

        time.sleep(0.07)
    
    return winnings([reel_1[(reel_1_idx + reel_1_amount) % 20], reel_2[(reel_2_idx + reel_2_amount - 1) % 20], reel_3[(reel_3_idx + reel_3_amount) % 20]])

# Interface for the machine

def interface(money, bet):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"SLOTS | BALANCE: {money} | BET: {bet}")
    print(f"----------------------------------------------------------------------")
    # Betting, as well as the machine spin

# Main slots logic

def slots():
    print(f"How much do you want to bet? (Type 'exit' to quit)")
    bet = input("$")
    
    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if bet.lower() == "exit":
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        if not bet.isdigit():
            interface("??", [], [], money, "bet")
            print(f"Please input a positive integer. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
        elif int(bet) <= money:
            interface("??", [], [], money, "bet")
            print(f"Please input a positive integer. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
        else:
            interface("??", [], [], money, "bet")
            print(f"You do not have enough money. How much do you want to bet? (Type 'exit' to quit)")
            bet = input("$")
    bet = int(bet)

    print(f"------------------------------SPINNING------------------------------")

    multi = machine_spin()
    money += bet * multi

    if multi == -1:
        print("You lost!")
        print(f"You lost {bet}.")
    elif multi == 1:
        print("Money back!")
    elif multi <= 5:
        print("Nice win!")
        print(f"You won {bet * multi}.")
    elif multi <= 50:
        print("Big win!")
        print(f"You won {bet * multi}.")
    elif multi == 100:
        print("JACKPOT!!!!")
        print(f"You won {bet * multi}.")
    
    

# print("Hello! Welcome to Python Slots!")
# print("If you don't know how to play, please learn beforehand. This game uses custom made reels.")
# input("Press Enter to play...")

# while money > 0:
    # slots()

# with open("money.txt", "w") as f:
    # f.write(str(money))

# print("You ran out of money. Please go to 'money.txt' to reset.")

machine_spin()