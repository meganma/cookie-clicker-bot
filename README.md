# Overview 🤖
This project is an Autoclicker bot for [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/), a popular browser based idle game. This bot uses the [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/index.html#) python library, which lets Python scripts control the mouse and keyboard to automate interactions with other applications.  

Currently, all Cookie Clicker game elements for unlocking the first five in game game buildings, as well as the buy/sell feature, have been implemented. The code for this bot has been configured to facilitate future extensions for additional game elements, should I (or the community!) ever decide to upgrade the bot.


# Setup 🛠️
## Prerequisites
Please make sure you have PyAutoGUI installed. Additionally, PyAutoGUI relies on OpenCV to locate images on screen with specified confidence levels, so that should be installed as well.

    sudo pip install pyautogui opencv-python

## Running the Bot
Navigate to where you want to keep this project and clone it: 

    git clone https://github.com/meganma/cookie-clicker-bot

Open [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) (the game must be visible on your main screen). 

Run the cookie_clicker_bot.py script:
    
    cd cookie-clicker-bot
    ./cookie-clicker-bot.py

To interrupt the program, move the mouse to the top-left corner of your screen.  

# Credits 
This bot was heavily inspired by a [Sushi Go Round Bot](https://github.com/asweigart/sushigoroundbot/tree/master) developed by Al Sweigart (also the developer of the PyAutoGUI library!) I also referenced this [Sushi Go Round bot](https://code.tutsplus.com/how-to-build-a-python-bot-that-can-play-web-games--active-11117t) by Chris Kiehl. 