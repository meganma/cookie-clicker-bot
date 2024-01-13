#! python3
"""Mac PyAutoGui Compat

Wrapper functions for mac compatibility with PyAutoGui's locate functions (mac screenshots automatically double pixel density). 
PyAutoGui documentation: https://pyautogui.readthedocs.io/en/latest/screenshot.html
"""

import pyautogui
from collections import namedtuple

def macLocateOnScreen(image_path, *args, **kwargs):
    """Returns (left, top, width, height) coordinate of first found instance of the image on the screen."""
    result = pyautogui.locateOnScreen(image_path, *args, **kwargs)
    macResult = (result[0]//2, result[1]//2, result[2]//2, result[3]//2)
    return macResult

def macLocateCenterOnScreen(image_path,*args, **kwargs):
    """Returns (x, y) coordinates of the center of the first found instance of the image on the screen."""
    result = pyautogui.locateCenterOnScreen(image_path, *args, **kwargs)
    macResult = (result[0]//2, result[1]//2)
    return macResult

def macLocateAllOnScreen(image_path,*args, **kwargs):
    """Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen."""
    Box = namedtuple('Box',['left', 'top', 'width', 'height'])
    for region_tuple in pyautogui.locateAllOnScreen(image_path, *args, **kwargs):
        yield Box(left=region_tuple.left//2, top=region_tuple.top//2, width=region_tuple.width//2, height=region_tuple.height//2)
