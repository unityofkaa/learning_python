# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:35
@Author ： captain
@File ：foods_tuple.py
"""
foods_tuple = ('beef', 'rice', 'tofu', 'coffee', 'tomato')
for food in foods_tuple:
    print(food, end=" ")
print()
try:
    foods_tuple[0] = 'beef_new'
except Exception as e:
    print(f"修改元组的元素失败:{e}")
foods_tuple_new = foods_tuple[:3] + ('potato', 'noodle')
for food in foods_tuple_new:
    print(food, end=" ")
