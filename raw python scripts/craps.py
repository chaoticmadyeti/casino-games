import random
import os
import sys

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(exe_dir)

dice = [1, 2, 3, 4, 5, 6]

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

def interface():
    pass

# Main logic

def craps():
    pass

print("Hello! Welcome to Python Craps!")
print("If you don't know how to play, please learn beforehand. This game uses casino craps rules.")
input("Press Enter to play...")

while money > 0:
    craps()

with open("money.txt", "w") as f:
    f.write(str(money))

print("You ran out of money. Please go to 'money.txt' to reset.")