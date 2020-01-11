# Imports
import os, sys, tty, termios
import time
import subprocess

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

#Key capturer, for the credits, look at main python file. This is a modified version to match the browser's needs.
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
            returnValueTemp = "up"
        elif k=='\x1b[B':
            returnValueTemp = "down"
        elif k=='\x1b[C':
            returnValueTemp = "right"
        elif k=='\x1b[D':
            returnValueTemp = "left"   
    
        else:
            returnValueTemp =  "nonArrrow"
        return returnValueTemp

# Some default values for the stuff.



# Main browser
def browser(DebugMode, CanSeeHidden):
    

    # Preset Values for stuff
    subMenu = False
    isFirstTime = True 
    Browsercursor = 1
    cursor = 1    
    move = "non"
    moveb = "non"
    currentLocation = sys.path[0]
    dirList = os.listdir(currentLocation)
    cursorDisplay = []
    for i in dirList:
        cursorDisplay.append(" ")
    
    # Debug Points for Debug mode (enabled in settings)
    debugp1 = False
    debugp2 = False
    debugp3 = False
    debugp4 = False
    debugVal1 = False
    debugVal2 = False
    
    
    
    
    
    # Main print
    while True:
        
        if isFirstTime: # To make it print for once at start 
            isFirstTime = False
            selectedFile = "non"
            
        elif not isFirstTime: # The Calculations for stuff
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
                if cursor < len(cursorDisplay) or cursor > len(cursorDisplay):
                    cursorDisplay[cursor] = ">"
                
            
            
            # SUBMENU STUFF
            if subMenu:
                debugp1 = True
                temp = 0
                while temp < len(cursorDisplay):
                    cursorDisplay[temp] = " "
                    temp += 1
                time.sleep(0.02)
                moveb = get() # WHY ISNT THIS WORKING FOR FUCKS SAKE
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

        print(bcolors.HEADER + "********************************************" + bcolors.ENDC)
        print(bcolors.OKGREEN + "Current Location: " +  currentLocation + bcolors.ENDC)
        print(bcolors.HEADER + "********************************************" + bcolors.ENDC)
        cursorIndex = 0
        for i in dirList:

            print(bcolors.OKGREEN + cursorDisplay[cursorIndex] + " - " +  i + bcolors.ENDC)
            cursorIndex += 1            
        print(bcolors.HEADER + "********************************************" + bcolors.ENDC)
        if DebugMode:        
            print(bcolors.WARNING + "Debug mode enabled" + bcolors.ENDC)
            print(bcolors.OKGREEN + "Selected File: " +  selectedFile + bcolors.ENDC)
            print(bcolors.OKGREEN + "SubMenu enabled?: " +  str(subMenu) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Cursor: " + str(cursor) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Cursor Display List: " + str(cursorDisplay) + bcolors.ENDC)   
            print(bcolors.OKGREEN + "MOVE: " + str(move) + bcolors.ENDC)
            print(bcolors.OKGREEN + "MOVE SubMenu: " + str(moveb) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Debug Point 1: " + str(debugp1) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Debug Point 2: " + str(debugp2) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Debug Point 3: " + str(debugp3) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Debug Point 4: " + str(debugp4) + bcolors.ENDC)
        if subMenu:
            print("")
            print(bcolors.HEADER + "********************************************" + bcolors.ENDC)
            print(bcolors.OKGREEN + "Test" + bcolors.ENDC)
            
        
        
