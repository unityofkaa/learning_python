# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 0:09
@Author ： captain
@File ：user_login_prompt_nouser.py
"""


def user_login_prompt(users_list):
    if users_list:
        for user in users_list:
            if user == 'admin':
                print(f"Hello {user}, would you like to see a status report?")
            else:
                print(f"Hello {user}, thank you for logging in again.")
    else:
        print("We need to find some users!")


users_list = ['zhangfei', 'admin', 'liubei', 'guanyu', 'zhugeliang']
user_login_prompt(users_list)
users_list.clear()
user_login_prompt(users_list)
