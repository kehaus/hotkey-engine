#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:44:37 2020


code snippet from here:
https://stackoverflow.com/questions/24072790/detect-key-press-in-python

@author: kh2
"""

import keyboard  # using module keyboard




# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#     except:
#         break  # if user pressed a key other than the given key the loop will break





# ========================================
# 
# ========================================
def do_case_a():
    print('this is case a')

def do_case_b():
    print('this is case BBBBB')


# ========================================
# hotkey engine
# ========================================
HOTKEY_TABLE = {
    'k':            do_case_a,
    'b':            do_case_b,    
#    'p':            None,           # reserved for quitting program
}


class HotkeyEngine():
    
    
    def __init__(self, verbose=False):
        self.hotkey_table = HOTKEY_TABLE.copy()
        self.is_running = False
        self.verbose = verbose
        

    def start(self):
        self.is_running = True
        while self.is_running:
            k = self.read_key()
            self.perform_task(k)
            if k == 'p':
                self.stop()
                
        if self.verbose:
            print('loop stopped')
            
    def stop(self):
        if self.verbose:
            print('stop loop')
        self.is_running = False

    def read_key(self):
        k = keyboard.read_key()
        if self.verbose: 
            print('key detected: {}', k)
        return k
        
    
    def perform_task(self, k):
        func = self.hotkey_table.get(k)
        if callable(func):
            func()