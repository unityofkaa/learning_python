# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:54
@Author ： captain
@File ：alien_color_02.py
"""


def check_hit(alien_color):
    if alien_color == 'green':
        print("You got 5 points!")
    else:
        print("You got 10 points!")


alien_color = 'green'
check_hit(alien_color)
alien_color = 'yellow'
check_hit(alien_color)
