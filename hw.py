from pprint import pprint
import operator
import os

print("\nTASK1\n")

file_name = "recipes.txt"

def get_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            meal = line.strip()
            cook_book[meal] = []
            ingredients_quantity = int(file.readline().strip())
            for item in range(ingredients_quantity):
                ingredient_dict = {}
                ingredient = file.readline().strip().split(' | ')
                ingredient_dict['ingredient_name'] = ingredient[0]
                ingredient_dict['quantity'] = int(ingredient[1])
                ingredient_dict['measure'] = ingredient[2]
                cook_book[meal].append(ingredient_dict)
            file.readline()
    return cook_book

outcome = get_cook_book(file_name)
pprint(outcome)



print("\nTASK2\n")

def get_shop_list_by_dishes(dishes, number_of_persons):
    ingeridients = {}
    for dish in dishes:
        if dish in outcome.keys():
            for ingredient in outcome[dish]:
                if ingredient['ingredient_name'] not in ingeridients:
                    ingeridients[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (number_of_persons*ingredient['quantity']) }
                else:
                    ingeridients[ingredient['ingredient_name']]['quantity'] += number_of_persons*ingredient['quantity']
    return ingeridients

ingredients_and_quantity_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(ingredients_and_quantity_dict)



print("\nTASK3\n")

def get_info_and_writing_to_list(file_names):
    '''Считывание содержимого файлов и запись информации в список'''
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data


def writing_info_to_file(my_data, my_file):
    '''Запись в файл информации (создание файла при условии отсутствия другого с таким же именем)'''
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

print(writing_info_to_file(get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt']), 'result.txt'))