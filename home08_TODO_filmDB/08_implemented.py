# -*- coding: utf-8 -*-

import sys

TABLE_CSV = """budget,homepage,id,title,vote_average,vote_count
237000000,http://www.avatarmovie.com/,19995,Avatar,7.2,11800
300000000,http://disney.go.com/disneypictures/pirates/,285,Pirates of the Caribbean: At World's End,6.9,4500
245000000,http://www.sonypictures.com/movies/spectre/,206647,Spectre,6.3,4466
250000000,http://www.thedarkknightrises.com/,49026,The Dark Knight Rises,7.6,9106
260000000,http://movies.disney.com/john-carter,49529,John Carter,6.1,2124
258000000,http://www.sonypictures.com/movies/spider-man3/,559,Spider-Man 3,5.9,3576
260000000,http://disney.go.com/disneypictures/tangled/,38757,Tangled,7.4,3330
280000000,http://marvel.com/movies/movie/193/avengers_age_of_ultron,99861,Avengers: Age of Ultron,7.3,6767
250000000,http://harrypotter.warnerbros.com/harrypotterandthehalf-bloodprince/dvd/index.html,767,Harry Potter and the Half-Blood Prince,7.4,5293
250000000,http://www.batmanvsupermandawnofjustice.com/,209112,Batman v Superman: Dawn of Justice,5.7,7004
270000000,http://www.superman.com,1452,Superman Returns,5.4,1400
200000000,http://www.mgm.com/view/movie/234/Quantum-of-Solace/,10764,Quantum of Solace,6.1,2965
200000000,http://disney.go.com/disneypictures/pirates/,58,Pirates of the Caribbean: Dead Man's Chest,7.0,5246"""

HELP = """

Available commands:

.help - show help message
.exit - exit from the program

Available queris:

SELECT * FROM TABLE;
SELECT * FROM TABLE ORDER BY column ASC;
SELECT * FROM TABLE ORDER BY column DESC;

"""

# Разделитель данных и заголовка
OUTPUT_DELIM = '| '

# Формат запроса
FMT_ORDER_BY_FIELD_OFFSET = 2  # Смещение поля, по которому следует соритровать данные
FMT_ORDER_BY_ORDER_OFFSET = 3  # Смещение типа сортировки ASC либо DESC


def help_cmd():
    """ Отобразить справку по программу """
    print(HELP)


def exit_cmd():
    """ Выйти из программы """
    sys.exit()


def bind(fun, args):
    """ Замкнем аргументы команды на функцию, которая выполняет команду"""

    #  Можно было бы использовать functools, но иногда вроще написать самому
    def wrapper():
        return fun(args)

    return wrapper


def load_data():
    """
    Загрузим данные из переменной TABLE_CSV и вернем  список фильмов в виде словарей следующего вида:
    [
      {
      'budget': '237000000',
      'homepage': 'http://www.avatarmovie.com/',
      'id': '19995',
      'title': 'Avatar',
      'vote_average': '7.2',
      'vote_count': '11800'
      },
      {
     'budget': '300000000',
      'homepage': 'http://disney.go.com/disneypictures/pirates/',
      'id': '285',
      'title': "Pirates of the Caribbean: At World's End",
      'vote_average': '6.9',
      'vote_count': '4500'}
      ,
    ]

    """
    # list_of_keys = ['budget', 'homepage', 'id', 'title', 'vote_average', 'vote_count']
    list_of_dicts = []
    list_of_substrings = TABLE_CSV.split('\n')
    for _ in list_of_substrings:
        # d = {key: None for key in list_of_keys}
        d = dict()
        comma_separated_list = _.split(',')
        d['budget'] = comma_separated_list[0]
        d['homepage'] = comma_separated_list[1]
        d['id'] = comma_separated_list[2]
        d['title'] = comma_separated_list[3]
        d['vote_average'] = comma_separated_list[4]
        d['vote_count'] = comma_separated_list[5]
        list_of_dicts.append(d)
    return list_of_dicts


def sort_data(data, order_by_order, order_by_field):
    """ Возрнем отсортированные данных по полю order_by_field, если задан order_by_order """
    if order_by_order:
        sorted_list = sorted(data, key=lambda k: k[order_by_field], reverse=True)
        return sorted_list


def check_query(tokens):
    """ Проверить синтаксис запроса """
    if not ' '.join(tokens[0:4]).startswith('select * from table'):
        sys.exit("Bad Query: 'select * from table'' missed")

    if not (tokens[-1] == ';' or tokens[-1].endswith(';')):
        sys.exit("Bad Query: ';' missed")


def parse_order_by(tokens):
    """ Проверить задан ли order by, если да вернуть параметры order by """
    if tokens.count("order"):
        order_by_idx = tokens.index("order")
        order_by_order = tokens[order_by_idx + FMT_ORDER_BY_ORDER_OFFSET]
        order_by_field = tokens[order_by_idx + FMT_ORDER_BY_FIELD_OFFSET]
        return order_by_order, order_by_field

    else:
        return None, None


def write_result(data):
    """ Выведем результат на экран """
    header = list(data[0].keys())
    print(OUTPUT_DELIM.join(header))
    print("-" * len((' ' * len(OUTPUT_DELIM)).join(header)))
    for row in data:
        print(OUTPUT_DELIM.join([str(val) for val in list(row.values())]))


def process_query(query_text):
    """ Обработать запрос """

    # Разобьем строку на токеныо
    query = query_text.split()
    tokens = [elem.strip().lower() for elem in query if elem.strip()]

    check_query(tokens)
    tokens[-1] = tokens[-1].rstrip(';')

    order_by_order, order_by_field = parse_order_by(tokens)
    data = load_data()
    if order_by_order:
        data = sort_data(data, order_by_order, order_by_field)

    write_result(data)


def next_command():
    """ Запросить у пользователя ввод следующей команды и вернуть соответсвующую функцию """

    COMMANDS = {
        ".help": help_cmd,
        ".exit": exit_cmd,
    }

    cmd_text = input("> ")
    # Если начинается с точки - это служебная команда
    if cmd_text.startswith("."):
        cmd_name = cmd_text.split()[0]
        if cmd_name in COMMANDS:
            return COMMANDS[cmd_name]
        else:
            return help_cmd
    else:
        # Иначе попробуем обработать как запрос
        return bind(process_query, cmd_text)


def main():
    """ Главная функция """

    # Организуем ввод команд пользователя с помощью вечного цикла
    while True:
        cmd = next_command()
        cmd()


main()
