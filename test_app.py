import re

my_english_dict = {}

while True:
    word = input('Введите слово на английском: или нажмите Q ')
    if word in ['q', 'й', 'Q', 'Й']:
        print('Программа завершена')
        print('')
        break

    elif not re.search(r'[а-яА-ЯёЁ0-9]', word):

        # проверка на повтор
        if word in my_english_dict:
            print(f'Слово {word} уже существуетв базе')
            print('')
        else:
            translate = input('Введите перевод на русском: ')
            if not re.search(r'[a-zA-Z0-9]', translate):

                # добавление в словарь
                my_english_dict[word] = translate
                print('')

print(my_english_dict)