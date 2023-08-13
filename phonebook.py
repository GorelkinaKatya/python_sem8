# Комаров Иван;89101234567;Работа
# Комаров Анатолий;89201234567;Такси
# Мишкин Владислав;89801234567;Работа
file = open('python_sem8/phonebook.txt', 'r+', encoding='UTF-8')
data = file.readlines()

def show_phonebook(data):
    print('\nСписок контактов')
    for i in range(len(data)):
        name = data[i].split(';')[0]
        print(f'{i+1} {name}')
    print('\nСписок команд\n1. Открыть контакт\n2. Вернуться в главное меню')
    request_num = int(input('Введите номер команды: '))
    if request_num == 1:
        open_contact(data)

def open_contact(data):
    contact_num = int(input('Введите порядковый номер контакта: '))
    contact_index = 0
    for i in range(len(data)):
        if i + 1 == contact_num:
            name = data[i].split(';')[0]
            phonenumber = data[i].split(';')[1]
            comment = data[i].split(';')[2]
            contact_index = i
    print(f'\nВыбранный контакт\nИмя: {name}\nНомер телефона: {phonenumber}\nКомментарий: {comment}')
    print('\nМеню контакта\n1. Изменить контакт\n2. Удалить контакт\n3. Вернуться в главное меню')
    request_num = int(input('Введите номер команды: '))
    if request_num == 1:
        change_contact(data, contact_index)
    elif request_num == 2:
        delete_contact(data)

def find_contact(data):
    search = input('Введите запрос: ')
    count = 0
    print('\nСовпадения по вашему запросу')
    for i in range(len(data)):
        if search.lower() in data[i].lower():
            name = data[i].split(';')[0]
            print(f'{i+1} {name}')
            count += 1
    if count == 0:
        print('не найдены\n\nСписок команд\n1. Ввести другой запрос\n2. Вернуться в главное меню')
        request_num = int(input('Введите номер команды: '))
        if request_num == 1:
            find_contact(data)
    else:
        print('\nСписок команд\n1. Открыть контакт\n2. Найти другой контакт\n3. Вернуться в главное меню')
        request_num = int(input('Введите номер команды: '))
        if request_num == 1:
            open_contact(data)
        elif request_num == 2:
            find_contact(data)     

def add_contact():
    name = input('Введите фамилию и имя: ')
    phonenumber = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    contact = f'{name};{phonenumber};{comment}/n'
    file.write(contact)
    print('\nКонтакт успешно сохранен\nЧтобы воспользоваться им, необходимо выйти из главного меню')

def change_contact(data, contact_index):
    name = input('Введите новые фамилию и имя: ')
    phonenumber = input('Введите новый номер телефона: ')
    comment = input('Введите новый комментарий: ')
    contact = f'{name};{phonenumber};{comment}\n'
    for i in range(len(data)):
        if i == contact_index:
            data[i] = contact
    print(data)
    
    file.seek(0)
    for i in data:
        file.write(i)
    
    print('\nКонтакт успешно изменен\nЧтобы воспользоваться им, необходимо выйти из главного меню')

def delete_contact(data):
    print()

# file.write('Комаров Иван;89101234567;Работа\n')
# file.write('Комаров Анатолий;89201234567;Такси\n')
# file.write('Мишкин Владислав;89801234567;Работа\n')

request_num = 0
while request_num < 4:
    print('\nГлавное меню\n1. Показать контакты\n2. Найти контакт\n3. Добавить контакт\n4. Выход')
    request_num = int(input('Введите номер команды: '))
    if request_num == 1:
        show_phonebook(data)
    elif request_num == 2:
        find_contact(data)
    elif request_num == 3:
        add_contact()

file.close()
