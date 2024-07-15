'''
Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

'''
from pathlib import Path

def get_cats_info(path:str):

    cats = []

    # Проверяем наличие файла
    if Path(path).is_file():
        
        # Открываем файл с гарантией закрытия
        with open(path, 'r', -1, 'UTF-8', 'strict') as fh:
            for item in fh.readlines():
                # Разделим и очистким каждую строку
                item = item.strip().split(',')
                # Собираем в словарь данные
                cats.append({'id':item[0], 'name':item[1], 'age':item[2]})
    else:

        # Вернем нули и сообщение об ошибке, если файла нет
        print('\n Ошибка, файл не найден или поврежден!\n')
        return
    
    return cats

print(f'{get_cats_info('task_2/cats.txt')}')