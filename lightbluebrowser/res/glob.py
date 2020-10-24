import termios
import tty
import sys
import os

DEBUG_ = False


# Color codes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUEBG = '\u001b[44m'
    REDBG = '\u001b[41m'


# arrow key dedector, for here, i modified a existing code. See: https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples
def __getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get():

    k = ""
    while k == "":
        k = __getch()

    if k == '\x1b[A':
        return "up"
    elif k == '\x1b[B':
        return "down"
    elif k == '\x1b[C':
        return "right"
    elif k == '\x1b[D':
        return "left"
    else:
        return None


def printWrapper(color, *msg):
    # print(color, *msg, bcolors.ENDC)
    printMsg = color + "".join(*msg) + bcolors.ENDC
    print(printMsg)


def clearScreen():
    command = "cls" if sys.platform.startswith("win") else "clear"
    os.system(command)
