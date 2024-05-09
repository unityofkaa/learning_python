# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:25
@Author ： captain
@File ：slice_list.py
"""
million_list = list(range(1, 1000001))
print(f"The first three items in the list are: {million_list[:3]}")
print(f"The items from the middle of the list are: {million_list[len(million_list) // 2:len(million_list) // 2 + 3]}")
print(f"The last three items in the list are: {million_list[-3:]}")
