# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 0:19
@Author ： captain
@File ：guest_list_change.py
"""
guests = ['zhangfei', 'guanyu', 'liubei', 'zhugeliang']
# for guest in guests:
#     print(f"Hello {guest}, How about we enjoy a delightful dinner together?")
print("zhangfei cann't make it!")
guests[0] = 'machao'
for guest in guests:
    print(f"Hello {guest}, How about we enjoy a delightful dinner together?")
