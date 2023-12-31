from colorama import Fore, Back, Style, init
from pyfiglet import figlet_format
import random

init()

Forecolors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.BLACK, Fore.MAGENTA, Fore.WHITE,
                  Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLACK_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX]

text = figlet_format("auto fast qc", "isometric1")
print(list(text))
quit()

def confetti(text):
    text = figlet_format(text, "isometric4")
    list_string = list(text)

    for i in list_string:
        print(random.choice(Forecolors), i, end="", sep="")

def multicolor(text):
    item = figlet_format(text, 'isometric1').split("\n")
    # print(list(item))
    for line in item:
        print(random.choice(Forecolors), line)


confetti("AUTO FAST QC")

# auto = figlet_format("Auto", 'isometric1')
# fast = figlet_format("Fast", 'isometric1')
# QC = figlet_format("QC", 'isometric1')
# print(Fore.RED, auto, Fore.YELLOW, fast, Fore.CYAN, QC, Fore.RESET)