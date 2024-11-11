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

def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': ingredient['measure'],
                                                  'quantity': int(ingredient['quantity'] * person_count)}
                else:
                    shop_list[ingredient_name]['quantity'] += int(ingredient['quantity'] * person_count)
        else:
            print(f'Блюдо "{dish}" отсутствует в книге рецептов')
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))