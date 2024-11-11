import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'input_data.txt')

cook_book = {}
temp_dish = []

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
    for line in lines:
        if not line:
            cook_book[temp_dish[0]] = temp_dish[2:]
            temp_dish.clear()
        elif '|' in line:
            ingredient_name, quantity, measure = line.split(' | ')
            temp_dish.append(
                dict(ingredient_name=ingredient_name.strip(),
                     quantity=int(quantity),
                     measure=measure.strip()))
        else:
            temp_dish.append(line)
    else:
        cook_book[temp_dish[0]] = temp_dish[2:]

pprint(cook_book)