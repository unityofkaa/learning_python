# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 0:29
@Author ： captain
@File ：desire_place.py
"""
desire_place = ['huangshan', 'taishan', 'songsan', 'hengshan north', 'hengshan south']
print(f"original desire place: {desire_place}")

print(f"sorted desire place: {sorted(desire_place)}")
print(f"desire place: {desire_place}")

print(f"reverse sorted desire place: {sorted(desire_place,reverse=True)}")
print(f"desire place: {desire_place}")

desire_place.reverse()
print(f"after reverse, desire place: {desire_place}")

desire_place.reverse()
print(f"after reverse again, desire place: {desire_place}")

desire_place.sort()
print(f"after sort, desire place: {desire_place}")

desire_place.sort(reverse=True)
print(f"after reversed sort, desire place: {desire_place}")