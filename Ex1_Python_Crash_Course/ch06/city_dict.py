# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 5:07
@Author ： captain
@File ：city_dict.py
"""
cities = {
    'shanghai': {
        'country': 'china',
        'population': 25000000,
        'fact': 'modu'
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'neat and tidy'
    },
    'seoul': {
        'country': 'keroa',
        'population': 10000000,
        'fact': 'fashion'
    }
}
for city, city_info in cities.items():
    for attribute, info in city_info.items():
        print(f"{city} {attribute} {info}")
