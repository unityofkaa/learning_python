# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 0:07
@Author ： captain
@File ：user_login_prompt.py
"""
users_list = ['zhangfei', 'admin', 'liubei', 'guanyu', 'zhugeliang']
for user in users_list:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
