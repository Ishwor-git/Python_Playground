from string import printable as characters
from time import sleep
import os


def clear_screen():
    if os.name == "posix":  # Unix/Linux/MacOS
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")


message = "Hello World"
current_string = ""

print("Processing....")
sleep(1)
print("Processing....")
sleep(1)
for i in message:
    for j in characters:
        clear_screen()
        print("Requested Message : " + current_string + j)
        sleep(0.05)
        if i == j:
            current_string += j
            break
sleep(1)
print("Mission Accomplished!")
