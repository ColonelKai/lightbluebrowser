# Actual Browser (IN THE OTHER FILE)

import lightbluebrowser.lib.browser_module as LB_BrowserModule
from lightbluebrowser.res.glob import *

# import of required libraries
import sys, tty, termios  # for arrow key detection
import getpass  # to get the seemless password input
import base64  # for password encryption to keep noobs away
import time  # to keep a print text on screen
import os  # for clearing the screen

# # option default values or preperations, first 3 can be changed in options tab.
# option_CanSeeHidden = False  # Bu isim ne lan
# option_DebugMode = False

# global option_CanSeeHidden
# global option_DebugMode

# File Manager
# NEEDS TO BE DONE
# Options


def optionsLB(option_CanSeeHidden, option_DebugMode):
    # global option_CanSeeHidden
    # global option_DebugMode

    # Option cursor and arrow key dedection preparetion (horrible spelling)
    optionCursor = 1
    optionCursor1 = ">"
    optionCursor2 = " "
    optionCursor3 = " "
    optionCursor4 = " "
    option_output = ""
    optionMove = "none"

    option_IsFirstTime = True

    while (True):
        # First time checker, prints UI for first joiner.
        if option_IsFirstTime == True:
            option_IsFirstTime = False
        # Non-first time init, does all arrow moves.
        elif option_IsFirstTime == False:
            optionMove = get()

            # Left Move, leaves options
            if optionMove == "left":
                option_output = "Leaving the options...."

            # up move, moves up.
            if optionMove == "up":
                if optionCursor == 1:
                    option_output = ""
                if optionCursor != 1:
                    optionCursor = optionCursor - 1

            # down move, goes down.
            if optionMove == "down":
                if optionCursor == 2:
                    option_output = ""
                if optionCursor != 2:
                    optionCursor = optionCursor + 1

            # right move, changes value.
            if optionMove == "right":
                if optionCursor == 1:
                    option_CanSeeHidden = bool(1 - option_CanSeeHidden)
                    # if option_CanSeeHidden == False:
                    #     option_CanSeeHidden = True
                    # elif option_CanSeeHidden == True:
                    #     option_CanSeeHidden = False

                elif optionCursor == 2:
                    option_DebugMode = bool(1 - option_DebugMode)
                    # if option_DebugMode == False:
                    #     option_DebugMode = True
                    # elif option_DebugMode == True:
                    #     option_DebugMode = False

            # optionCursor1,2,3 configs.
            if optionCursor == 1:
                optionCursor1 = ">"
                optionCursor2 = " "

            if optionCursor == 2:
                optionCursor1 = " "
                optionCursor2 = ">"

        # yapf: disable
        clearScreen()
        printWrapper(bcolors.BLUEBG, "*" * 80)
        printWrapper(bcolors.OKGREEN, "Right arrow key to change, Up and Down to move and Left arrow key to quit.")
        printWrapper(bcolors.BLUEBG, "*" * 80)
        printWrapper(bcolors.OKGREEN, "Options for LightBlue:\n")
        printWrapper(bcolors.OKBLUE, f"{optionCursor1} 1- See hidden files? - {option_CanSeeHidden}")
        printWrapper(bcolors.OKBLUE, f"{optionCursor2} 2- Debug mode? - {option_DebugMode}")
        printWrapper(bcolors.BLUEBG, "\n" + ("*" * 80))
        # yapf: enable

        if optionMove == "left":
            break

        option_output = ""

    return option_CanSeeHidden, option_DebugMode


# selection function for main menu
def selectionLB(MainMenu_IsFirstTime, option_CanSeeHidden, option_DebugMode):
    MainMenuCursor = 1
    MainMenuCursor1 = ">"
    MainMenuCursor2 = " "
    MainMenuCursor3 = " "
    MainMenu_output = ""
    MainMenuMove = "none"

    returnValueMainMenu = None
    MainMenu_IsFirstTime = True
    while True:
        # First time checker, prints UI for first joiner.
        if MainMenu_IsFirstTime:
            MainMenu_IsFirstTime = False

        # Non-first time init, does all arrow moves.
        elif not MainMenu_IsFirstTime:
            MainMenuMove = get()

            if MainMenuMove == "left":
                MainMenu_output = "Leaving the MainMenu...."

            # up move, moves up.
            if MainMenuMove == "up":
                if MainMenuCursor == 1:
                    MainMenu_output = ""
                if MainMenuCursor != 1:
                    MainMenuCursor = MainMenuCursor - 1

            # down move, goes down.
            if MainMenuMove == "down":
                if MainMenuCursor == 3:
                    MainMenu_output = ""
                if MainMenuCursor != 3:
                    MainMenuCursor = MainMenuCursor + 1

            # right move, changes value.
            if MainMenuMove == "right":

                if MainMenuCursor == 2:
                    option_CanSeeHidden, option_DebugMode = optionsLB(
                        option_CanSeeHidden, option_DebugMode)

                if MainMenuCursor == 1:
                    returnValueMainMenu = "options"
                    LB_BrowserModule.browser(option_DebugMode,
                                             option_CanSeeHidden)
                    break

                if MainMenuCursor == 3:
                    clearScreen()
                    if MainMenuMove == "right":
                        sys.exit()

            # Bunu ne zaman yazdın
            # MainMenuCursor 1,2,3 configs.
            if MainMenuCursor == 1:
                MainMenuCursor1 = ">"
                MainMenuCursor2 = " "
                MainMenuCursor3 = " "

            if MainMenuCursor == 2:
                MainMenuCursor1 = " "
                MainMenuCursor2 = ">"
                MainMenuCursor3 = " "

            if MainMenuCursor == 3:
                MainMenuCursor1 = " "
                MainMenuCursor2 = " "
                MainMenuCursor3 = ">"

        clearScreen()
        printWrapper(bcolors.BLUEBG, ("*" * 44) + "\n")
        printWrapper(bcolors.OKGREEN, "Main Menu of LightBlue")
        printWrapper(bcolors.OKBLUE, f"{MainMenuCursor1} 1- Browser")
        printWrapper(bcolors.OKBLUE, f"{MainMenuCursor2} 2- Options")
        printWrapper(bcolors.OKBLUE, f"{MainMenuCursor3} 3- Quit")
        printWrapper(bcolors.BLUEBG, "\n" + ("*" * 44))

        if option_DebugMode:
            printWrapper(
                bcolors.WARNING,
                "Debug modded version, please close from options to disable this."
            )

            if MainMenu_IsFirstTime:
                print(returnValueMainMenu)

            print(MainMenu_IsFirstTime)
            print(MainMenuCursor)
            print(MainMenuMove)
        MainMenu_output = ""

    rv = {
        "MainMenu_IsFirstTime": MainMenu_IsFirstTime,
        "option_CanSeeHidden": option_CanSeeHidden,
        "option_DebugMode": option_DebugMode
    }
    return rv
    # return MainMenu_IsFirstTime, option_CanSeeHidden, option_DebugMode


# Password Function
def passwordLight():
    # password = base64.b64decode("bGlnaHRibHVlMTIz").decode()
    password = base64.b64decode(b"dHVuYXBybzE=").decode()
    # Şimdiden özür dilerim
    # print(password)

    clearScreen()
    printWrapper(bcolors.BLUEBG, "Welcome to lightblue!")
    printWrapper(bcolors.BLUEBG, "*" * 44)

    # yapf: disable
    inputValue = getpass.getpass(bcolors.WARNING + "Please enter your LB access key:" + bcolors.ENDC)
    # print(inputValue, password, password == inputValue)
    # yapf: enable

    if inputValue == password:
        print("Access Granted")
        time.sleep(2)

        return True

    if inputValue != password:
        print("Access Denied")
        time.sleep(3)
        clearScreen()

        return False

    raise Exception


def main():
    # option default values or preperations, first 3 can be changed in options tab.
    # MainMenu_IsFirstTime = True # Bu isim ne lan
    # option_CanSeeHidden = False
    # option_DebugMode = False

    # Bu daha kullanışlı ama
    # arguments = True, False, False

    # Bunun okunabilirliği daha iyi
    kw_arguments = {
        "MainMenu_IsFirstTime": True,
        "option_CanSeeHidden": False,
        "option_DebugMode": False
    }

    # Main Codeline
    hasLoggedIn = passwordLight()
    clearScreen()

    # main choosing has started
    if hasLoggedIn:
        while True:
            clearScreen()
            kw_arguments = selectionLB(**kw_arguments)  # MainInterface


if __name__ == "__main__":
    main()