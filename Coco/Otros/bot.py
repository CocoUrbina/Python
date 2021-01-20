# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:15:41 2021

@author: Pmontenegro
"""
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import ctypes

x_pad = 436
y_pad = 269
box = (x_pad, y_pad, 140, 140)

#Colo del pez 54 93 128

def click(x,y):
ctypes.windll.user32.SetCursorPos(x, y)
pyautogui.click()
while keyboard.is_pressed('q') == False:
pic = pyautogui.screenshot (region=(x_pad, y_pad, 140, 140) )
width, height = pic.size
for x in range (0, 140, 2):
for y in range (0, 140, 2):
r, g, b = pic.getpixel((x, y))
if b == 121:
click(x+436, y+269)
time.sleep(1)
break