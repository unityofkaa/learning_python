# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/10 0:12
@Author ： captain
@File ：user_login_check.py
"""
current_users = ['zhangfei', 'admin', 'liubei', 'guanyu', 'zhugeliang']
new_users = ['aDmin', 'liuBei', 'Caocao', 'xuchu', 'guojia']
for user in new_users:
    if user.lower() in current_users:
        print(f"{user.lower()} alreday exists!")
    else:
        print(f"{user.lower()} is not use!")
