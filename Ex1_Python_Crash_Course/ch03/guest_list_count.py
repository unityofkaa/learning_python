# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 0:36
@Author ： captain
@File ：guest_list_count.py
"""
guests = ['zhangfei', 'guanyu', 'liubei', 'zhugeliang']
# for guest in guests:
#     print(f"Hello {guest}, How about we enjoy a delightful dinner together?")
print("We find a big table!")
guests.insert(0, 'machao')
guests.insert(2, 'zhaoyun')
guests.append('huangzhong')
for guest in guests:
    print(f"Hello {guest}, How about we enjoy a delightful dinner together?")
print(f"total invite {len(guests)} guest.")
