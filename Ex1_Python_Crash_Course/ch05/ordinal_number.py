# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 0:15
@Author ： captain
@File ：ordinal_number.py
"""
number_list = list(range(1, 10))
for num in number_list:
    if num == 1:
        print(f"{num}st", end=" ")
    elif num == 2:
        print(f"{num}nd", end=" ")
    elif num == 3:
        print(f"{num}rd", end=" ")
    else:
        print(f"{num}th", end=" ")
