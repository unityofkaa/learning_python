# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:16
@Author ： captain
@File ：triple_list.py
"""
triple_list = [value for value in range(3, 31) if value % 3 == 0]
for i in triple_list:
    print(i, end=" ")
