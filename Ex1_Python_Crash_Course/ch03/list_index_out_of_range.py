# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 0:39
@Author ： captain
@File ：list_index_out_of_range.py
"""
guests = ['zhangfei', 'guanyu', 'liubei', 'zhugeliang']
try:
    guests.pop(5)
except Exception as e:
    print(f"索引操作异常: {e}")
