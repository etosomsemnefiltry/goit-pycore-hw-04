'''
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і 
візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
'''

import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

if len(sys.argv) != 2:
        print(Fore.RED + '\nНазвание директории не может быть пустым\n')
        sys.exit(1)
else:
    path = Path(sys.argv[1])

if not path.exists():
    print(Fore.RED + '\nДиректория не существует!\n')
    sys.exit(1)

if not path.is_dir():
    print(Fore.RED + f'\nПуть {path} не является директорией.\n')
    sys.exit(1)


def print_directory(path, prefix=''):
    '''
    Функция для вывода цветного списка с содержимым всех вложенных файлов и директорий
    Для теста берем "python task_3.py test_folder"
    '''
    # Определим счетчик итераций и получим начальный список в директории для отступов
    i = 0
    items = sorted(path.iterdir())
    try:
        for x in path.iterdir():
            i +=1
            if x.is_dir(): # Папка
                print(Fore.LIGHTYELLOW_EX + prefix + f'{x.name}' + Style.RESET_ALL)
                # Если это директория, запускаем рекурсию с добавлением отступов
                print_directory(x, prefix + ('   ' if i < len(items) - 1 else '    '))
            else: # Файл
                print(Fore.LIGHTBLUE_EX + prefix + f'{x.name}' + Style.RESET_ALL)
    except BaseException as e:
        print(Fore.RED + f'Ошибка - {e}' + Style.RESET_ALL)


print_directory(path)