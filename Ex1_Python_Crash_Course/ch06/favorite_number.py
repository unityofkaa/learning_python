# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 4:29
@Author ： captain
@File ：favorite_number.py
"""
favorite_number_dict = {
    'zhangfei': 666,
    'liubei': 222,
    'guanyu': 999,
    'zhugeliang': 777,
    'zhaoyun': 555
}
print(favorite_number_dict)
for name in favorite_number_dict.keys():
    favorite_number = int(input(f"What's your favorite number? {name}\n"))
    if favorite_number == favorite_number_dict[name]:
        print(f"It's true,{name} favorite number is {favorite_number}.")
    else:
        print(f"It's false,{name} favorite number is {favorite_number}.")
