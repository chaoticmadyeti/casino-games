import random
import time
import sys

# Wheel and colours (European)

wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] # Black numbers are the numbers that aren't 0 or in the red_numbers list

# Colourise numbers

def colour(number):
    global red_numbers

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

wheel_spin()