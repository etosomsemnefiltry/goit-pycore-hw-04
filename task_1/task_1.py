'''
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
Alex Korp,3000
Nikita Borisenko,2000
Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
'''
from pathlib import Path

def total_salary(path:str):
    total = 0 
    iteration = 0

    # Проверяем наличие файла
    if Path(path).is_file():

        # Открываем файл с гарантией закрытия
        with open(path, 'r', -1, 'UTF-8', 'strict') as fh:
            for line in fh.readlines():

                # Преобразуем каждую строку
                line = line.split(',')

                # Подсчитываем значения
                total += int(line[1])
                iteration += 1
    else:

        # Вернем нули и сообщение об ошибке, если файла нет
        print('\n Ошибка, файл не найден или поврежден!\n')
        return (0,0)

    return (total, total/iteration)
    
total, average = total_salary("devs2.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")