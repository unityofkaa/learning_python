# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 23:29
@Author ： captain
@File ：pizza_update.py
"""
pizzas = ['beef', 'onion', 'pepperoni']
friend_pizzas = pizzas[:]
pizzas.append('tomato')
friend_pizzas.append('potato')
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza, end=" ")
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza, end=" ")
