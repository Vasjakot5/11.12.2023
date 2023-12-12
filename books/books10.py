import csv as book2

file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = book2.reader(file)

    next(reader, None)

    reader = list(reader)
    '''
    Название - 0
    Автор - 1
    Год издания - 2
    '''
    sorted_students = sorted(reader, key=lambda item: item[1])

    with open('sorted_books.csv', 'w', newline='', encoding='utf-8') as new_file:
        writer = book2.writer(new_file)
        fieldnames = ['Название', 'Автор', 'Год издания']
        writer.writerow(fieldnames)
        writer.writerows(sorted_students)

