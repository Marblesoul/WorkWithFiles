from pprint import pprint

cook_book = {}

temp_dish = []

with open('input_data.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()