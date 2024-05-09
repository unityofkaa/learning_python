# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:18
@Author ： captain
@File ：cube_list.py
"""
cube_list = list(map(lambda x: x ** 3, range(1, 11)))
for value in cube_list:
    print(value, end=" ")
