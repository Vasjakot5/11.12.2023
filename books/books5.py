import csv

file_name = 'books.csv'

name = input("Введите название: ")
author = input("Введите автора: ")
age = input("Введите год издания: ")

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([name, author, age])

print(f'Книга {name}, успешно добавлен в файл: {file_name}')
