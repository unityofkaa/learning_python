# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:57
@Author ： captain
@File ：age_stage.py
"""


def age_recognition(age):
    if age < 2:
        print("baby!")
    elif age < 4:
        print("infant!")
    elif age < 13:
        print("Children!")
    elif age < 20:
        print("Youth!")
    elif age < 65:
        print("Adult!")
    else:
        print("Old Man!")


age = 20
age_recognition(age)
