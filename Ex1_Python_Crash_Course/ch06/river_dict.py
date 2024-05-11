# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 4:42
@Author ： captain
@File ：river_dict.py
"""
river_dict = {
    'nile': 'egypt',
    'changjiang': 'china',
    'rhine': 'europe'
}
for river, country in river_dict.items():
    print(f"The {river.title()} runs through {country.title()}.")
