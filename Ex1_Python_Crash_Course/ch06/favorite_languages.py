# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 4:49
@Author ： captain
@File ：favorite_languages.py
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
investigation_list = ['edward', 'zhangfei']
for name in investigation_list:
    if name in favorite_languages.keys():
        print(f"Thank you {name}, for your participation!")
    else:
        print(f"{name}, Would you like to participate investigation?")
