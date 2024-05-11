# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 4:59
@Author ： captain
@File ：favorite_place.py
"""
favorite_places = {
    'zhangfei': [],
    'liubei': [],
    'zhugeliang': []
}
for name in favorite_places.keys():
    favorite_places[name] = input(f"{name}, which place do you love?\n").split(',')
for name, favorite_place in favorite_places.items():
    print(f"{name} favorite place {favorite_place}")
