import csv as book

new_file_name = input('Введите имя нового файла: ')

with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    books_data = [
        {'Название': 'Утро', 'Автор': 'Максим Горький', 'Год издания': 1910},
        {'Название': 'Рикки Тикки Тави', 'Автор': ' Редьярд Киплинг', 'Год издания': 1893},
    ]

    writer = book.writer(file)
    for item in books_data:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

with open(new_file_name, newline='', encoding='utf-8') as file:
    reader = book.reader(file)

    reader = list(reader)
