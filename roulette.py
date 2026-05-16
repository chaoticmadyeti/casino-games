import random
import time
import sys

# Wheel and colours (European)

wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] 
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
half_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] # Second half are the numbers that aren't 0 or in the half_1 list
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35] # Even numbers are the numbers that aren't 0 or in the odd list
col_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
col_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35] # Column three are the numbers that aren't 0, in col_1, or in col_2
dozen_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dozen_2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] # Dozen 3 are the numbers that aren't 0, in dozen_1 or in dozen_1
top_line = [0, 1, 2, 3]

bets = ["colour"]

# Colourise numbers

def colour(number):

    # Background colours (ANSI)

    RED = "\033[1;37;41m"
    BLACK = "\033[1;37;40m"
    GREEN = "\033[1;37;42m"
    RESET = "\033[0m"

    if int(number) == 0:
        return f"{GREEN}{number}{RESET}"
    elif int(number) in red_numbers:
        return f"{RED}{number}{RESET}"
    else:
        return f"{BLACK}{number}{RESET}"

# Wheel spin

def wheel_spin():
    curr = random.randint(0, len(wheel) - 1)
    spins = random.randint(60, 80)
    speed = 0.05
    print("---------Wheel Spinning---------")
    for i in range(spins):
        curr = (curr + 1) % len(wheel)

        prev2 = wheel[(curr - 2) % len(wheel)]
        prev1 = wheel[(curr - 1) % len(wheel)]
        centre = wheel[curr]
        next1 = wheel[(curr + 1) % len(wheel)]
        next2 = wheel[(curr + 2) % len(wheel)]

        prev2_display = colour(f"{prev2:>2}")
        prev1_display = colour(f"{prev1:>2}")
        centre_display = colour(f"{centre:>2}")
        next1_display = colour(f"{next1:>2}")
        next2_display = colour(f"{next2:>2}")

        sys.stdout.write(f"\r{prev2_display} | {prev1_display} | ---> {centre_display} <--- | {next1_display} | {next2_display}")
        sys.stdout.flush()

        if i > spins * 0.65:
            speed *= 1.1

        time.sleep(speed)
    
    print(f"\nResult: {wheel[curr]}")
    return wheel[curr]

# Betting

def bet_type():
    print("What do you want to bet on? Currently, this code has: Colour.")
    specific_bet = input("Choice: ")
    while specific_bet not in bets:
        print("Please choose a valid choice. What do you want to bet on? Currently, this code has: Colour.")
        specific_bet = input("Choice: ")
    if specific_bet.lower() == "colour":
        print("Which colour do you want to bet on?")
        specific_bet = input("Choice: ")
        while specific_bet != "red" and specific_bet != "black":
            print("Please pick a valid colour. Which colour do you want to bet on?")
            specific_bet = input("Choice: ")
        if specific_bet.lower() == "red":
            return red_numbers
        elif specific_bet.lower() == "black":
            return black_numbers

# Main Logic

def roulette():
    money = 1000

    print(f"You have ${money}.")
    winning_numbers = bet_type()

    if wheel_spin() in winning_numbers:
        print("You win!")
    else:
        print("You loose!")


print("Hello! Welcome to Python Roulette.")
print("If you don't know how to play roulette, I highly suggest you do. This game uses the European wheel.")

roulette()