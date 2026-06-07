import random
import os
import sys

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(exe_dir)

dice = [1, 2, 3, 4, 5, 6]
bets = ["pass", "don't pass", "dont pass"]

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

def interface(money, bet, bet_amount, rolls):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======================================================================")
    print(f"CRAPS | YOUR BALANCE: ${money}")
    print(f"----------------------------------------------------------------------")
    print(f"YOUR BET: {bet} | BET AMOUNT: ${bet_amount}")
    if rolls == []:
        print(f"ROLLS: ??, ?? (TOTAL: ??)")
    else:
        print(f"ROLLS: {rolls[0]}, {rolls[1]} (TOTAL: {rolls[0] + rolls[1]})")
    print(f"----------------------------------------------------------------------")

# Main logic

def craps():
    rolls = []

    print("What would you like to bet on? (Type 'exit' to quit)")
    print("Currently, this code has: Pass, Don't Pass")
    bet_type = input("Choice: ")
    while bet_type.lower() not in bets:
        if bet_type.lower() == 'exit':
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        print("Please choose a valid option. What would you like to bet on? (Type 'exit' to quit)")
        print("Currently, this code has: Pass, Don't Pass")
        bet_type = input("Choice: ")
    
    print("How much do you want to bet on that?")
    bet = input("$")

    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if not bet.isdigit():
            print(f"Please input a positive integer. How much do you want to bet?")
            bet = input("$")
        elif int(bet) <= money:
            print(f"Please input a positive integer. How much do you want to bet?")
            bet = input("$")
        else:
            print(f"You do not have enough money. How much do you want to bet?")
            bet = input("$")
    bet = int(bet)

print("Hello! Welcome to Python Craps!")
print("If you don't know how to play, please learn beforehand. This game uses casino craps rules.")
input("Press Enter to play...")

while money > 0:
    craps()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")