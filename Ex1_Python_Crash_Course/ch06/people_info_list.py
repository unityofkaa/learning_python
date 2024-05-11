# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 4:55
@Author ： captain
@File ：people_info_list.py
"""
person_info1 = {
    'first_name': 'zhang',
    'last_name': 'fei',
    'age': 30,
    'city': 'jingzhou'
}
person_info2 = {
    'first_name': 'liu',
    'last_name': 'bei',
    'age': 32,
    'city': 'jingzhou'
}
person_info3 = {
    'first_name': 'guan',
    'last_name': 'yu',
    'age': 31,
    'city': 'jingzhou'
}
people_info_list = [person_info1, person_info2, person_info3]
for people in people_info_list:
    print(people)
