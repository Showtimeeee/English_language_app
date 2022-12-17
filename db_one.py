import sqlite3


def create_table(table='english'):
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {table} (word text, translate text)"""
    cursor.execute(create_table_query)
    return table


# вставляет данные
def insert_data():
    # функция запрашивает две строки, executemany() вставляет строки в траблицу english
    word = input('Введите слово на англ: ')
    translate = input(f'Введите перевод слова {word}: ')
    cursor.executemany("INSERT INTO english VALUES(?, ?)", [(word, translate)])
    connection.commit()


# функция для просмотра таблицы
def show_table(table):
    # запрос для просмотра тыблицы в бд
    for i in cursor.execute(f"SELECT * FROM {table}"):
        print(i[0] + ' - ' + i[1])
    print(len(table))


# редактировать запись
def edit_data():
    edit_dat = input('Исправить слово или перевод? w - англ слово, t - перевод ')
    a = input('Введите слово для редактирования: ')
    b = input('Новое слово: ')

    numb = (b, a)
    numb1 = (a, b)

    if edit_dat in ['w', 'W', 'Ц', 'ц']:
        edit_data_query = """UPDATE english SET translate = ? WHERE word = ? """
        cursor.execute(edit_data_query, numb)

    if edit_dat in ['t', 'T']:
        edit_data_query = """UPDATE english SET word = ? WHERE translate = ? """
        cursor.execute(edit_data_query, numb)

    connection.commit()


# удаляет данные из таблицы
def delete_data():
    del_data = input('Какое слово удалить?: ')
    delete_data_query = f"DELETE FROM english WHERE word= '{del_data}'"
    cursor.execute(delete_data_query)
    connection.commit()
    print('')
    print(f'Запись {del_data} удалена')
    print('')


#
def main():
    while True:
        query = input('i - создать запись, s - посмотреть таблицу, u - обновить данные, d - удалить запись, q - выход: ')
        print('')
        if query in ['q', 'й', 'Q', 'Й']:
            print('Программа завершена')
            break
        if query in ['s', 'S', 'ы', 'Ы']:
            show_table(create_table())
            print('*' * 20)
        if query in ['i', 'I', 'ш', 'Ш']:
            insert_data()
        print('')
        if query in ['u', 'U', 'г', 'Г']:
            edit_data()
        if query in ['d', 'D', 'в', 'В']:
            delete_data()


if __name__ == '__main__':
    database = 'db_english.db'
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    main()


