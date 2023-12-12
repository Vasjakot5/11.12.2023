import csv


students_list = [
    {
        'Название': 'Теремок',
        'Автор': 'Самуил Маршак',
        'Год издания': 1833
    },
    {
        'Название': 'Сказка о рыбаке и рыбке',
        'Автор': 'А. С. Пушкина',
        'Год издания': 1833
    },
    {
        'Название': 'Лебедь, рак и щука',
        'Автор': 'Ивана Андреевича Крылова',
        'Год издания': 1814
    },
]

file_name = 'books.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Название', 'Автор', 'Год издания']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for item in students_list:
        writer.writerow(item)

print(f'Создан новый файл: {file_name}')
