# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:56
@Author ： captain
@File ：alien_color_03.py
"""


def check_hit(alien_color):
    if alien_color == 'green':
        print("You got 5 points!")
    elif alien_color == 'yellow':
        print("You got 10 points!")
    elif alien_color == 'red':
        print("You got 15 points!")


alien_color = 'green'
check_hit(alien_color)
alien_color = 'yellow'
check_hit(alien_color)
alien_color = 'red'
check_hit(alien_color)
