from lightbluebrowser.res.glob import *
# import subprocess
# import termios
import time
import sys
# import tty
import os


# Main browser
# Some default values for the stuff.
def browser(DebugMode, CanSeeHidden):
    # Preset Values for stuff
    cursor = 1
    move = None
    moveb = None
    subMenu = False
    Browsercursor = 1
    isFirstTime = True

    cursorDisplay = []
    currentLocation = sys.path[0]
    dirList = os.listdir(currentLocation)

    for i in dirList:
        cursorDisplay.append(" ")

    selectedFile = None
    # Debug Points for Debug mode (enabled in settings)
    debugp1, debugp2 = False, False
    debugp3, debugp4 = False, False
    debugVal1, debugVal2 = False, False

    # Main print
    while True:
        if isFirstTime:  # To make it print for once at start
            isFirstTime = False
            selectedFile = None

        elif not isFirstTime:  # The Calculations for stuff
            currentLocation = sys.path[0]

            dirList = os.listdir(currentLocation)

            if not subMenu:
                move = get()

            # File display:
            cursorDisplay = []
            for i in dirList:
                cursorDisplay.append(" ")

            # Calculation of position
            if not subMenu:
                if move == "down":
                    temp = int(len(cursorDisplay)) - 1
                    if cursor != temp:
                        cursor += 1

                if move == "up":
                    if cursor != 0:
                        cursor = cursor - 1

                if move == "left":
                    break

                if move == "right":
                    selectedFile = dirList[cursor]
                    subMenu = True

                # cursorDisplay set
                if cursor != len(cursorDisplay):
                    cursorDisplay[cursor] = ">"

            # SUBMENU STUFF
            if subMenu:
                temp = 0
                debugp1 = True
                while temp < len(cursorDisplay):
                    cursorDisplay[temp] = " "
                    temp += 1

                time.sleep(0.02)
                moveb = get()  # WHY ISNT THIS WORKING FOR FUCKS SAKE
                debugp2 = True

                # SubMenu Controls
                if moveb == "left":
                    subMenu = False
                    debugp3 = True
                    cursorDisplay[0] = ">"
                if moveb == "right":
                    debugp4 = True

            elif not subMenu:
                debugp1 = False
                debugp2 = False

        # UI IS HERE
        if not debugVal1:
            debugVal1 = True
            debugp4 = False
        os.system("clear")

        printWrapper(bcolors.HEADER, "*" * 44)
        printWrapper(bcolors.OKGREEN, f"Current Location: {currentLocation}")
        printWrapper(bcolors.HEADER, "*" * 44)

        cursorIndex = 0
        for i in dirList:
            # yapf: disable
            printWrapper(bcolors.OKGREEN, f"{cursorDisplay[cursorIndex]} - {i}")
            cursorIndex += 1
            # yapf: enable

        printWrapper(bcolors.HEADER, "*" * 44)

        if DebugMode:
            # yapf: disable
            printWrapper(bcolors.WARNING, f"Debug mode enabled")
            printWrapper(bcolors.OKGREEN, f"Selected File: {selectedFile}")
            printWrapper(bcolors.OKGREEN, f"SubMenu enabled?: {subMenu}")
            printWrapper(bcolors.OKGREEN, f"Cursor: {cursor}")
            printWrapper(bcolors.OKGREEN, f"Cursor Display List: {cursorDisplay}")
            printWrapper(bcolors.OKGREEN, f"MOVE: {move}")
            printWrapper(bcolors.OKGREEN, f"MOVE SubMenu: {moveb}")
            printWrapper(bcolors.OKGREEN, f"Debug Point 1: {debugp1}")
            printWrapper(bcolors.OKGREEN, f"Debug Point 2: {debugp2}")
            printWrapper(bcolors.OKGREEN, f"Debug Point 3: {debugp3}")
            printWrapper(bcolors.OKGREEN, f"Debug Point 4: {debugp4}")
            # yapf: enable

        if subMenu:
            printWrapper(bcolors.HEADER, "\n" + ("*" * 44))
            printWrapper(bcolors.OKGREEN, "Test")
