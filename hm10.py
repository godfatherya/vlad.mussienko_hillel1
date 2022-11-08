# # Импортируем необходимую нам модуль.
import json


def create_db():
    # Создаем список имен:
    name = ['Иван', 'Андрей', 'Яков', 'Юрий', 'Татьяна', 'Мария',
             'Авдотья', 'Елизавета', 'Альберт', 'Руслан', 'Жанна',
             'Лейла', 'Станислав', 'Радомир', 'Добромила', 'Рада']

    # Создаем список возрастов рандомно, чтобы в базе данных возраст всех 'name' имели разные значении:
    import random
    age = []
    for i in range(16):
        a = random.randint(15, 35)
        age.append(a)

    # Создаем список хобби:
    hobby = ['Астрономия', 'Дайвинг', 'Настольные игры', 'Косплей', 'Переписка по обычной почте', 'Блоггерство',
             'Кроссворды', 'Жонглирование',
             'Рисование', 'Пчеловодство',
             'Батут', 'Фейерверки', 'Фокусы', 'Фотография и фотокниги', 'Футбол',
             'Шитье и вышивание']

    # Здесь создал переменную DateBasa, в которую в последующем буду добавлять словарей с именем, возрастом и с хобби:
    DateBasa = []
    for i in range(16):
        data = {
            'name': name[i],
            'age': age[i],
            'hobby': hobby[i]
        }
        DateBasa.append(data)

    # Сохраняем полученную базу данных(DateBasa) в виде json файла(DateBasa.json):
    with open('DateBase.json', 'w', encoding="utf-8") as file:
        json.dump(DateBasa, file, ensure_ascii=False, indent=4)


def return_data():
    # Открываем созданную ранее Базу данных(DateBase.json)
    with open('DateBase.json', 'r', encoding='utf-8') as file:
        DateBase = json.load(file)

    # Создаем новую Базу данных(new_DB), с индексированными элементами старой Базы данных(DateBase)
    new_DB = {}
    count_el = len(DateBase)

    for i in range(count_el):
        new_DB[i+1] = DateBase[i]

    return new_DB


def main():
    # Вызываем по очереди созданных ранее функций:
    create_db()
    DateBase = return_data()

    # В виде обработки исключений по запросу пользователя возвращаем элемент из Базы данных!
    try:
        request = int(input('Введите индекс элемента(от 0 до 17), чтобы получить данную элемент из Базы данных >>> '))
        print(f'\nВаш результат: {DateBase[request]}')

    except:
        print('\nПерезапустите программу и введите соответствующую к описанию данную!*')


if __name__ == '__main__':
    main()
