import csv

file_name = 'books.csv'

new_students = [
    {
        'Название': 'Белоснежка и семь гномов',
        'Автор': 'Братья Гримм',
        'Год издания': 1812
    },
    {
        'Название': 'Волк и семеро козлят',
        'Автор': 'Братья Гримм',
        'Год издания': '1812—1815'
    },
    {
        'Название': 'Сказка о царе Салтане',
        'Автор': 'А. С. Пушкина',
        'Год издания': 1831
    },
]

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for item in new_students:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

print(f'Данные успешно записаны в файл: {file_name}')
