# English simulator

import re
import os

# проверка на наличие файла если нет то создать
if not os.path.exists('words.txt'):
    open('words.txt', 'w')

while True:

    word = input('Введите слово на английском или нажмите Q: ')
    if word in ['q', 'й', 'Q', 'Й']:
        print('Программа завершена')
        print('')
        break

    elif not re.search(r'[а-яА-ЯёЁ0-9]', word):
        # контекст менеджер
        with open('words.txt', 'r', encoding='utf-8') as read_txt:
            dct = read_txt.readlines()

            lst_clear = [j[0].strip() for j in (i.split('-') for i in dct)]
            
            # проверка на повтор
            if word in lst_clear:
                print(f'Слово {word} уже существуетв базе')
                print('')

            else:
                translate = input('Введите перевод на русском: ')
                if not re.search(r'[a-zA-Z0-9]', translate):
                    # записывает инф в файл
                    with open('words.txt', 'a', encoding='utf-8') as write_txt:
                        write_txt.write(word + ' - ' + translate + '\n')



