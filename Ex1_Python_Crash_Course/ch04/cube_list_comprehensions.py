# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:20
@Author ： captain
@File ：cube_list_comprehensions.py
"""
cube_list = [value ** 3 for value in range(1, 11)]
for value in cube_list:
    print(value, end=" ")
