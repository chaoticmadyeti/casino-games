import random
import time
import sys

# Wheel and colours (European)

wheel = ['0', '32', '15', '19', '4', '21', '2', '25', '17', '34', '6', '27', '13', '36', '11', '30', '8', '23', '10', '5', '24', '16', '33', '1', '20', '14', '31', '9', '22', '18', '29', '7', '28', '12', '35', '3', '26']
red_numbers = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36'] 
black_numbers = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']
half_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'] 
half_2 = ['19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
odd = ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33', '35'] 
even = ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36']
col_1 = ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28', '31', '34']
col_2 = ['2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35'] 
col_3 = ['3', '6', '9', '12', '15', '18', '21', '24', '27', '30', '33', '36']
dozen_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
dozen_2 = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'] 
dozen_3 = ['25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
streets = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12'], ['13', '14', '15'], ['16', '17', '18'], ['19', '20', '21'], ['22', '23', '24'], ['25', '26', '27'], ['28', '29', '30'], ['31', '32', '33'], ['34', '35', '36']]
splits_vertical = [['1', '4'], ['4', '7'], ['7', '10'], ['10', '13'], ['13', '16'], ['16', '19'], ['19', '22'], ['22', '25'], ['25', '28'], ['28', '31'], ['31', '34'], ['2', '5'], ['5', '8'], ['8', '11'], ['11', '14'], ['14', '17'], ['17', '20'], ['20', '23'], ['23', '26'], ['26', '29'], ['29', '32'], ['32', '35'], ['3', '6'], ['6', '9'], ['9', '12'], ['12', '15'], ['15', '18'], ['18', '21'], ['21', '24'], ['24', '27'], ['27', '30'], ['30', '33'], ['33', '36']]
splits_horizontal = [['1', '2'], ['2', '3'], ['4', '5'], ['5', '6'], ['7', '8'], ['8', '9'], ['10', '11'], ['11', '12'], ['13', '14'], ['14', '15'], ['16', '17'], ['17', '18'], ['19', '20'], ['20', '21'], ['22', '23'], ['23', '24'], ['25', '26'], ['26', '27'], ['28', '29'], ['29', '30'], ['31', '32'], ['32', '33'], ['34', '35'], ['35', '36']]
top_line = ['0', '1', '2', '3']

bets = ["colour", "parity", "half", "column", "dozen", "double street", "top line", "corner"]

content = ''

with open("money.txt", "r") as f:
    content = f.read()

money = int(content)
multi = 1

# Colourise numbers

def colour(number):

    # Background colours (ANSI)

    RED = "\033[1;37;41m"
    BLACK = "\033[1;37;40m"
    GREEN = "\033[1;37;42m"
    RESET = "\033[0m"

    new_num = number.replace(' ', '')

    if new_num == '0':
        return f"{GREEN}{number}{RESET}"
    elif new_num in red_numbers:
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
    global money
    global multi

    print("What do you want to bet on? (Type 'exit' to quit)")
    print("Currently, this code has: Colour, Parity, Half, Column, Dozen, Double Street, Top Line, Corner.")
    specific_bet = input("Choice: ")

    while specific_bet.lower() not in bets:
        if specific_bet.lower() == "exit":
            print("Exiting...")
            with open("money.txt", "w") as f:
                f.write(str(money))
            sys.exit()
        print("Please choose a valid choice. What do you want to bet on? (Type 'exit' to quit)")
        print("Currently, this code has: Colour, Parity, Half, Column, Dozen, Double Street, Top Line, Corner.")
        specific_bet = input("Choice: ")

    # Colour bets
    
    if specific_bet.lower() == "colour":
        multi = 1
        print("Which colour do you want to bet on?")
        specific_bet = input("Choice: ")
        while specific_bet.lower() != "red" and specific_bet.lower() != "black":
            print("Please pick a valid colour. Which colour do you want to bet on?")
            specific_bet = input("Choice: ")
        if specific_bet.lower() == "red":
            return red_numbers
        elif specific_bet.lower() == "black":
            return black_numbers
        
    # Parity bets
    
    elif specific_bet.lower() == "parity":
        multi = 1
        print("Which parity do you want to bet on?")
        specific_bet = input("Choice: ")
        while specific_bet.lower() != "odd" and specific_bet.lower() != "even":
            print("Please pick a valid parity. Which parity do you want to bet on?")
            specific_bet = input("Choice: ")
        if specific_bet.lower() == "odd":
            return odd
        elif specific_bet.lower() == "even":
            return even
    
    # Half bets

    elif specific_bet.lower() == "half":
        multi = 1
        print("Which half do you want to bet on?")
        print("1. 1-18")
        print("2. 19-36")
        print("(Type an option from 1 - 2)")
        specific_bet = input("Choice: ")
        while specific_bet.lower() != "1" and specific_bet.lower() != "2":
            print("Please pick an option from 1 - 2. Which half do you want to bet on?")
            print("1. 1-18")
            print("2. 19-36")
            print("(Type an option from 1 - 2)")
            specific_bet = input("Choice: ")
        if specific_bet.lower() == "1":
            return half_1
        elif specific_bet.lower() == "2":
            return half_2
    
    # Column Bets

    elif specific_bet.lower() == "column":
        multi = 2
        print("Which column do you want to bet on?")
        print("1. 1, 4, 7...")
        print("2. 2, 5, 8...")
        print("3. 3, 6, 9...")
        print("(Type an option from 1 - 3)")
        specific_bet = input("Choice: ")
        while specific_bet.lower() not in ['1', '2', '3']:
            print("Please pick an option from 1 - 3. Which column do you want to bet on?")
            print("1. 1, 4, 7...")
            print("2. 2, 5, 8...")
            print("3. 3, 6, 9...")
            print("(Type and option from 1 - 3)")
            specific_bet = input("Choice: ")
        if specific_bet.lower() == '1':
            return col_1
        elif specific_bet == '2':
            return col_2
        elif specific_bet == '3':
            return col_3
    
    # Dozen Bets

    elif specific_bet.lower() == "dozen":
        multi = 2
        print("Which dozen do you want to bet on?")
        print("1. 1 - 12")
        print("2. 13 - 24")
        print("3. 25 - 36")
        print("(Type an option from 1 - 3)")
        specific_bet = input("Choice: ")
        while specific_bet.lower() not in ['1', '2', '3']:
            print("Please pick an option from 1 - 3. Which dozen do you want to bet on?")
            print("1. 1 - 12")
            print("2. 13 - 24")
            print("3. 25 - 36")
            print("(Type an option from 1 - 3)")
            specific_bet = input("Choice")
        if specific_bet.lower() == '1':
            return dozen_1
        elif specific_bet == '2':
            return dozen_2
        elif specific_bet == '3':
            return dozen_3
        
    # Double Street Bets

    elif specific_bet.lower() == "double street":
        multi = 5
        print("Please type the lowest number in the double street you would like to bet on.")
        specific_bet = input("Choice: ")
        while specific_bet.lower() not in col_1:
            print("That is not a valid number. Please type the lowest number in the double street you would like to bet on.")
            specific_bet = input("Choice: ")
        for i in range(len(streets) - 1):
            if streets[i][0] == specific_bet.lower():
                return streets[i] + streets[i + 1]
    
    # Top Line Bets

    elif specific_bet.lower() == "top line":
        multi = 8
        return top_line
    
    # Corner Bets

    elif specific_bet.lower() == "corner":
        multi = 8
        print("Please type the lowest number in the corner you would like the bet on.")
        specific_bet = input("Choice: ")
        while specific_bet.lower() not in ['1', '2', '4', '5', '7', '8', '10', '11', '13', '14', '16', '17', '19', '20', '22', '23', '25', '26', '28', '29', '31', '32']:
            print("That is not a valid number. Please type the lowest number in the corner you would like to bet on.")
            specific_bet = input("Choice: ")
        for i in range(len(splits_horizontal) - 2):
            if splits_horizontal[i][0] == specific_bet.lower():
                return splits_horizontal[i] + splits_horizontal[i + 2]

# Main Logic

def roulette():
    global money
    global multi
    
    while money > 0:

        print(f"You have ${money}.")
        winning_numbers = bet_type()

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

        if wheel_spin() in winning_numbers:
            print(f"You win! You win ${bet}")
            money = money + (bet * multi)
        else:
            print(f"You lost! You lost ${bet}")
            money = money - bet


print("Hello! Welcome to Python Roulette.")
print("If you don't know how to play roulette, I highly suggest you learn how to play beforehand. This game uses the European wheel.")

roulette()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")

# To Do: add other types of bets, add multi betting (bet on multiple types)