#import of required libraries
import os #for clearing the screen
import sys,tty,termios #for arrow key dedection
import base64 #for password encryption to keep noobs away
import time #to keep a print text on screen 
import getpass #to get the seemless password input

# Actual Browser (IN THE OTHER FILE)
import LB_BrowserModule

debug123 = False
#For the Coloring of The Console output.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUEBG = '\033[44m'
    REDBG = '\033[41m'



#option default values or preperations, first 3 can be changed in options tab.
option_CanSeeHidden = False
option_DebugMode = False
global option_CanSeeHidden
global option_DebugMode
#File Manager
#NEEDS TO BE DONE
#Options

def optionsLB():
    #Option cursor and arrow key dedection preparetion (horrible spelling)
    optionCursor = 1
    optionCursor1 = ">"
    optionCursor2 = " "
    optionCursor3 = " "
    optionCursor4 = " "
    option_output = ""
    optionMove = "none"

    global option_DebugMode
    global option_CanSeeHidden


    global option_IsFirstTime
    option_IsFirstTime = True
    
    
    while(True):
        #First time checker, prints UI for first joiner.
        if option_IsFirstTime == True:
            option_IsFirstTime = False
        #Non-first time init, does all arrow moves.
        elif option_IsFirstTime == False:
            optionMove = get()
            
            #Left Move, leaves options
            if optionMove == "left":
                option_output = "Leaving the options...."

            #up move, moves up.
            if optionMove == "up":
                if optionCursor == 1:
                    option_output = ""
                if optionCursor != 1:
                    optionCursor = optionCursor - 1
                
            
            #down move, goes down.
            if optionMove == "down":
                if optionCursor == 2:
                    option_output = ""
                if optionCursor != 2:
                    optionCursor = optionCursor + 1

            #right move, changes value.
            if optionMove == "right":

                if optionCursor == 1:
                    if option_CanSeeHidden == False:
                        option_CanSeeHidden = True
                    elif option_CanSeeHidden == True:
                        option_CanSeeHidden = False

                elif optionCursor == 2:
                    if option_DebugMode == False:
                        option_DebugMode = True
                    elif option_DebugMode == True:
                        option_DebugMode = False
                

            #optionCursor1,2,3 configs.
            if optionCursor == 1:
    	        optionCursor1 = ">"
    	        optionCursor2 = " "

            if optionCursor == 2:
    	        optionCursor1 = " "
    	        optionCursor2 = ">"




        os.system("clear")
        print(bcolors.BLUEBG + "********************************************************************************" + bcolors.ENDC)
        print(bcolors.OKGREEN + "Right arrow key to change, Up and Down to move and Left arrow key to quit." + bcolors.ENDC)
        print(bcolors.BLUEBG + "********************************************************************************" + bcolors.ENDC)
        print(bcolors.OKGREEN + "Options for LightBlue:" + bcolors.ENDC)
        print("")
        print(bcolors.OKBLUE + optionCursor1 + "1- See hidden files? - " + str(option_CanSeeHidden) + bcolors.ENDC) 
        print(bcolors.OKBLUE + optionCursor2 + "2- Debug mode? - " + str(option_DebugMode) + bcolors.ENDC)
        print("")
        print(bcolors.BLUEBG + "********************************************************************************" + bcolors.ENDC)
        if optionMove == "left":
            break
        option_output = ""


#arrow key dedector, for here, i modified a existing code. See: https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples

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
            returnValueTemp =  "nonArrow"
        return returnValueTemp
        
#selection function for main menu
def selectionLB():
    MainMenuCursor = 1
    MainMenuCursor1 = ">"
    MainMenuCursor2 = " "
    MainMenuCursor3 = " "
    MainMenu_output = ""
    MainMenuMove = "none"

    global MainMenu_IsFirstTime
    
    global option_DebugMode
    global option_CanSeeHidden
    MainMenu_IsFirstTime = True
    
    
    while True:
        #First time checker, prints UI for first joiner.
        if MainMenu_IsFirstTime == True:
            MainMenu_IsFirstTime = False
        #Non-first time init, does all arrow moves.
        elif MainMenu_IsFirstTime == False:
            MainMenuMove = get()
            
            #
            if MainMenuMove == "left":
                MainMenu_output = "Leaving the MainMenu...."

            #up move, moves up.
            if MainMenuMove == "up":
                if MainMenuCursor == 1:
                    MainMenu_output = ""
                if MainMenuCursor != 1:
                    MainMenuCursor = MainMenuCursor - 1
                
            
            #down move, goes down.
            if MainMenuMove == "down":
                if MainMenuCursor == 3:
                    MainMenu_output = ""
                if MainMenuCursor != 3:
                    MainMenuCursor = MainMenuCursor + 1

            #right move, changes value.
            if MainMenuMove == "right":

                if MainMenuCursor == 2:
                   optionsLB()


                if MainMenuCursor == 1:
                    returnValueMainMenu = "options"
                    LB_BrowserModule.browser(option_DebugMode, option_CanSeeHidden)
                    break


                if MainMenuCursor == 3:
                    os.system("clear")
                    if MainMenuMove == "right":
                        sys.exit()
            #MainMenuCursor1,2,3 configs.
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
        os.system("clear")
        print(bcolors.BLUEBG + "********************************************************************************" + bcolors.ENDC)
        print("")
        print(bcolors.OKGREEN + "Main Menu of LightBlue" + bcolors.ENDC)
        print(bcolors.OKBLUE + MainMenuCursor1 + " 1- Browser" + bcolors.ENDC)
        print(bcolors.OKBLUE + MainMenuCursor2 + " 2- Options" + bcolors.ENDC)
        print(bcolors.OKBLUE + MainMenuCursor3 + " 3- Quit" + bcolors.ENDC)
        print("")
        print(bcolors.BLUEBG + "********************************************************************************" + bcolors.ENDC)
        global option_DebugMode
        if option_DebugMode:
            print(bcolors.WARNING + "Debug modded version, please close from options to disable this." + bcolors.ENDC)
            if MainMenu_IsFirstTime is set:
                print(returnValueMainMenu)
            print(MainMenuCursor is set)
            print(MainMenu_IsFirstTime is set)
            print(MainMenuMove)
        MainMenu_output = ""    



#Password Function
def passwordLight():
    password = base64.b64decode("bGlnaHRibHVlMTIz")
    print(password)
    password = str(password)
    os.system("clear")
    print(bcolors.BLUEBG + "Welcome to lightblue!" + bcolors.ENDC)
    print(bcolors.BLUEBG + "********************************************" + bcolors.ENDC)
    inputValue = getpass.getpass(bcolors.WARNING + "Please enter your LB access key:" + bcolors.ENDC)	
    if inputValue == password:
        hasLoggedIn = True
        print("Access Granted")
        time.sleep(2)
    if inputValue != password:
        hasLoggedIn = False
        print("Access Denied")
        time.sleep(3)
        os.system("clear")
    return hasLoggedIn	


#Main Codeline
hasLoggedIn = passwordLight()
os.system("clear")

if hasLoggedIn == True:
    while(True):   #main choosing has started

        os.system("clear")
        #MainInterface
        selectionLB()
        
