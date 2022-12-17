import sqlite3

connection = sqlite3.connect('db_english.db')
cursor = connection.cursor()


def create_table(table='english'):
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {table} (word text, translate text)"""
    cursor.execute(create_table_query)
    return table


# create_table()


# вставляет данные
def insert_data():
    # функция запрашивает две строки, executemany() вставляет строки в траблицу english
    word = input('Введите слово на англ: ')
    translate = input(f'Введите перевод слова {word}: ')
    cursor.executemany("INSERT INTO english VALUES(?, ?)", [(word, translate)])
    connection.commit()


# insert_data()


# функция для просмотра таблицы
def show_table(table):
    # запрос для просмотра тыблицы в бд
    for i in cursor.execute(f"SELECT * FROM {table}"):
        print(i[0] + ' - ' + i[1])
    print(len(table))


# редактировать запись
def edit_data():
    # edit_data_query = """UPDATE english SET translate = 'five' WHERE word ='five' """
    edit_data_query = """UPDATE english SET translate = 'принуждать' WHERE word ='force' """
    cursor.execute(edit_data_query)
    connection.commit()


# edit_data()
# функция с аргументом функции, возвращает table


# удаляет данные из таблицы
def delete_data():
    delete_data_query = "DELETE FROM english WHERE word='force'"
    cursor.execute(delete_data_query)
    connection.commit()


#delete_data()
#show_table(create_table())


#
def main():
    while True:
        query = input('i - создать запись, s - посмотреть таблицу, q - выход: ')
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


main()


