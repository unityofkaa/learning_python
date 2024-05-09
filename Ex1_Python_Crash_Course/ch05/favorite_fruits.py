# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 0:02
@Author ： captain
@File ：favorite_fruits.py
"""
favorite_fruits = ['apple', 'orange', 'banana']
check_fruits = ['banana', 'watermelon', 'strawberry', 'apple', 'orange']
for fruit in check_fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!"
              f"")
