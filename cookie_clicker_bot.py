#! python3
"""Cookie Clicker Bot

A bot program to automatically play the game Cookie Clicker (Orteil) at https://orteil.dashnet.org/cookieclicker/
""" 

import pyautogui, time, os, logging, functools, sys
if 'darwin' in sys.platform:
    from utils.mac_PyAutoGui_compat import macLocateOnScreen, macLocateCenterOnScreen, macLocateAllOnScreen
    locateOnScreen, locateCenterOnScreen, locateAllOnScreen = macLocateOnScreen, macLocateCenterOnScreen, macLocateAllOnScreen
else:
    locateOnScreen, locateCenterOnScreen, locateAllOnScreen = pyautogui.locateOnScreen, pyautogui.locateCenterOnScreen, pyautogui.locateAllOnScreen


logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.info) #uncomment to block debug log messages

# Building Constants
CURSOR = 'cursor'
GRANDMA = 'grandma'
FARM = 'farm'
MINE = 'mine'
FACTORY = 'factory'
ALL_BUILDING_TYPES = (CURSOR, GRANDMA, FARM, MINE, FACTORY)

# Global Variables
INVENTORY = {CURSOR: 0, GRANDMA: 0, FARM: 0, MINE: 0, FACTORY: 0}
COOKIE_COUNT = 0

# Various coordinates of objects in the game
GAME_REGION = ()
UPGRADES_REGION = ()
COOKIE_COORDS = None
CURSOR_COORDS = None
GRANDMA_COORDS = None
FARM_COORDS = None
MINE_COORDS = None
FACTORY_COORDS = None
BUY_COORDS = None
SELL_COORDS = None
MULTIPLIER_1X_COORDS = None
MULTIPLIER_10X_COORDS = None
MULTIPLIER_100X_COORDS = None

def main():
    """Runs the entire program. The Cookie Clicker game must be visible on the screen."""
    logging.info('Program Started. Press Ctrl-C to abort at any time.')
    getGameRegion()
    resetGame()
    setupCoordinates()
    

def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filenames with 'images/' prepended."""
    return os.path.join('images', filename)

def getGameRegion():
    global GAME_REGION

    #identify the top-left corner
    logging.info('Finding the game region...')
    try:
        topLeftRegion = locateOnScreen(imPath('top_left_corner.png'), confidence=0.7)
        bottomRightRegion = list(locateAllOnScreen(imPath('bottom_right_corner.png'), confidence=0.7))[-1]

        
        GAME_REGION = (int(topLeftRegion[0]), 
                       int(topLeftRegion[1]),
                       int((bottomRightRegion[0]+bottomRightRegion[2])-topLeftRegion[0]),
                       int((bottomRightRegion[1]+bottomRightRegion[3])-topLeftRegion[1]))
        

        logging.info('Game region found: %s' % (GAME_REGION,))
    except pyautogui.ImageNotFoundException:
        raise Exception("Could not find game on screen. Is the game visible?")
    
def resetGame():
    """Resets cookie clicker game to default starting state."""   
    try:
        locateOnScreen(imPath('zero_cookies.png'), confidence = 0.9)
        logging.info('Game currently in default starting state.')
        return
    except pyautogui.ImageNotFoundException:
        logging.info('Game not at default starting state. Resetting game...')

        # open options menu
        options_button = locateCenterOnScreen(imPath('options_button.png'), confidence = 0.5)
        pyautogui.click(options_button, duration=0.5, clicks=2)

        # save game data to text file
        game_saved = False
        if userWantsToSave():
            save_button = locateCenterOnScreen(imPath('save_button.png'), confidence = 0.9)
            pyautogui.click(save_button, duration=0.5, clicks=2)
            game_saved = True      
        
        # reset game 
        wipe_save_button = locateCenterOnScreen(imPath('wipe_save_button.png'), confidence = 0.8)
        
        if game_saved:
            pyautogui.click(wipe_save_button, duration=0.5)
            wipe_save_confirmation_button = locateCenterOnScreen(imPath('wipe_save_confirmation_button.png'), confidence = 0.8)
        else:
            pyautogui.click(wipe_save_button, clicks=2, duration=0.5)
            wipe_save_confirmation_button = locateCenterOnScreen(imPath('wipe_save_confirmation_button.png'), confidence = 0.8)
        pyautogui.click(wipe_save_confirmation_button, clicks=2,interval=0.1, duration=0.5)
        pyautogui.click(options_button, duration=0.5)
        
def userWantsToSave():
    '''Prompts user to save game. Returns True if user inputs "yes", false if "no".'''
    valid = {'yes': True, 'y': True, 'ye': True, 'no': False, 'n': False}
    logging.info('Would you like to save your previous game? Type "yes" or "no".')

    while True:
        choice = input().lower()
        if choice not in valid:
            logging.info('Please respond with "yes" or "no".')
            continue
        
        if not valid[choice]:
            logging.info('Game will not be saved.')   
            return False

        logging.info('Game will be saved to file')
        return True

def setupCoordinates():
    """Sets several of the coordinate-related global variables, after aquiring the value for GAME_REGION"""

    logging.info('Setting up coordinates...')
    global COOKIE_COORDS, CURSOR_COORDS, GRANDMA_COORDS, FARM_COORDS, MINE_COORDS, FACTORY_COORDS, BUY_COORDS, SELL_COORDS, MULTIPLIER_1X_COORDS, MULTIPLIER_10X_COORDS, MULTIPLIER_100X_COORDS

    COOKIE_COORDS = locateCenterOnScreen(imPath('cookie.png'), confidence = 0.5)

    BUY_COORDS = locateCenterOnScreen(imPath('buy_button.png'), confidence = 0.7)

    SELL_COORDS = locateCenterOnScreen(imPath('sell_button.png'), confidence = 0.7)

    MULTIPLIER_1X_COORDS = locateCenterOnScreen(imPath('multiplier_1X.png'), confidence = 0.8)
    MULTIPLIER_10X_COORDS = ((MULTIPLIER_1X_COORDS[0] + (MULTIPLIER_1X_COORDS[0]-BUY_COORDS[0])),(BUY_COORDS[1]+SELL_COORDS[1])/2)
    MULTIPLIER_100X_COORDS = ((MULTIPLIER_1X_COORDS[0] + 2*(MULTIPLIER_1X_COORDS[0]-BUY_COORDS[0])),(BUY_COORDS[1]+SELL_COORDS[1])/2)

    region = locateOnScreen(imPath('cursor.png'), confidence = 0.7)
    CURSOR_COORDS = (region[0] + region[2]/2, region[1] + region[3]/2)
    GRANDMA_COORDS = (region[0] + region[2]/2, region[1] + 3*(region[3]/2))
    FARM_COORDS = (region[0] + region[2]/2, region[1] + 5*(region[3]/2))
    MINE_COORDS = (region[0] + region[2]/2, region[1] + 7*(region[3]/2))
    FACTORY_COORDS = (region[0] + region[2]/2, region[1] + 9*(region[3]/2))

    UPGRADES_REGION = (region[0], region[1], region[2], region[3])    
    logging.info('Finished setting up coordinates...')    
    
if __name__ == '__main__':
    main()