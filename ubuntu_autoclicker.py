#!/usr/bin/env python3.5
"""
Toggles autoclick on F5 key press and closes program with ESC.
"""

__author__ = "Raimonds Vanags"
__copyright__ = "Copyright 2017, Raimonds Vanags"

__license__ = "GPL"
__version__ = "0.4"
__maintainer__ = "Raimonds Vanags"
__email__ = "writetoraimonds@gmail.com"
__status__ = "Beta Version"

import threading, os, time
from pynput.keyboard import Key, Listener

'''
Setting hotkeys for autoclicking functionality.
'''

holdKey = Key.f4
switchKey = Key.f2
closeKey = Key.esc

'''
switch variable turns the autoclicking on or off.
pushButton enables holding key autoclicking option.
closeApp closes program when True.
'''
switch = False
pushButton = False
closeApp = False


def on_press(key):
    '''
    Push button type autoclicker functionality on keypres (F4) added.
    '''
    global pushButton
    if key == holdKey:
        pushButton = True


def on_release(key):
    """
    Detect which keys are pressed and on release the chosen activity is executed.
    """
    global closeApp, switch
    if key == switchKey:
        switch = not switch
    if key == closeKey:
        closeApp = True
        # Stop listener
        return False


def keyboard_input():
    '''
    Defines Listner to read input from keyboard.
    '''
    global switch, closeApp
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def autoclicker():
    '''
    Starts or stops autoclicking, or ends the thread if the according key has been pressed.
    '''
    global switch, closeApp, pushButton
    while (True):
        # Starts autoclicking
        if (switch == True):
            # executes linux click command
            # x = number of clicks in one cycle?
            # y = time interval between clicks
            # z = whice mouse button to click (1 - left, 2- middle, 3-right)
            os.system(r"xdotool click --repeat 10 --delay 10 1")
        elif (pushButton == True):
            os.system(r"xdotool click --repeat 10 --delay 10 1")
            pushButton = False
        if (closeApp == True):
            # Closes autoclicker thread
            break


# Create two threads for keyboard input and autoclicking
thread1 = threading.Thread(target=keyboard_input)
thread2 = threading.Thread(target=autoclicker)

# Start created Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
