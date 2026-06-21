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
    print(f"YOUR BET: {bet.upper()} | BET AMOUNT: ${bet_amount}")
    if rolls == []:
        print(f"ROLLS: ??, ?? (TOTAL: ??)")
    else:
        print(f"ROLLS: {rolls[0]}, {rolls[1]} (TOTAL: {rolls[0] + rolls[1]})")
    print(f"----------------------------------------------------------------------")

# Main logic

def craps():
    global money

    rolls = []

    interface(money, "??", "??", rolls)
    print("What would you like to bet on? (Type 'exit' to quit)")
    print("Currently, this code has: Pass, Don't Pass")
    bet_type = input("Choice: ")
    while bet_type.lower() not in bets:
        if bet_type.lower() == 'exit':
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        interface(money, "??", "??", rolls)
        print("Please choose a valid option. What would you like to bet on? (Type 'exit' to quit)")
        print("Currently, this code has: Pass, Don't Pass")
        bet_type = input("Choice: ")
    
    interface(money, bet_type, "??", rolls)
    print("How much do you want to bet on that?")
    bet = input("$")

    while not bet.isdigit() or int(bet) <= 0 or int(bet) > money:
        if not bet.isdigit():
            interface(money, bet_type, "??", rolls)
            print(f"Please input a positive integer. How much do you want to bet?")
            bet = input("$")
        elif int(bet) <= money:
            interface(money, bet_type, "??", rolls)
            print(f"Please input a positive integer. How much do you want to bet?")
            bet = input("$")
        else:
            interface(money, bet_type, "??", rolls)
            print(f"You do not have enough money. How much do you want to bet?")
            bet = input("$")
    bet = int(bet)

    interface(money, bet_type, bet, rolls)

    num = random.randint(0, len(dice) - 1)
    rolls.append(dice[num])
    num = random.randint(0, len(dice) - 1)
    rolls.append(dice[num])

    sum = rolls[0] + rolls[1]

    print("Rolling...")
    input("Press Enter to continue...")

    if sum == 7 or sum == 11:
        if bet_type.lower() == "pass":
            interface(money, bet_type, bet, rolls)
            print("You win!")
            money += bet
            input("Press Enter to continue...")
        else:
            interface(money, bet_type, bet, rolls)
            print("You lose!")
            money -= bet
            input("Press Enter to continue...")
    elif sum == 2 or sum == 3 or sum == 12:
        if bet_type.lower() == "pass":
            interface(money, bet_type, bet, rolls)
            print("You lose!")
            money -= bet
            input("Press Enter to continue...")
        elif sum == 12:
            interface(money, bet_type, bet, rolls)
            print("It's a tie!")
            input("Press Enter to continue...")
        else:
            interface(money, bet_type, bet, rolls)
            print("You win!")
            money += bet
            input("Press Enter to continue...")
    else:
        interface(money, bet_type, bet, rolls)
        print("The point has been established.")
        input("Press Enter to continue...")
        point = sum
        sum = 0
        while point != sum and sum != 7:
            rolls.clear()

            num = random.randint(0, len(dice) - 1)
            rolls.append(dice[num])
            num = random.randint(0, len(dice) - 1)
            rolls.append(dice[num])

            sum = rolls[0] + rolls[1]

            interface(money, bet_type, bet, rolls)
            print("The dice has been rolled.")
            input("Press Enter to continue...")
        
        if sum == 7:
            if bet_type.lower() == "pass":
                interface(money, bet_type, bet, rolls)
                print("You lose!")
                money -= bet
                input("Press Enter to continue...")
            else:
                interface(money, bet_type, bet, rolls)
                print("You win!")
                money += bet
                input("Press Enter to continue...")
        else:
            if bet_type.lower() == "pass":
                interface(money, bet_type, bet, rolls)
                print("You win!")
                money += bet
                input("Press Enter to continue...")
            else:
                interface(money, bet_type, bet, rolls)
                print("You lose!")
                money -= bet
                input("Press Enter to continue...")


print("Hello! Welcome to Python Craps!")
print("Rules for this game are in README.md. Please learn the rules beforehand.")
input("Press Enter to play...")

while money > 0:
    craps()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")