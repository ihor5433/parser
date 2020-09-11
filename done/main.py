import csv
import os
import time

from alive_progress import alive_bar

import Alphavantage as av
import Earning_TradingView as Earning_TradingView
import General_functions as gf
import Screener_parser as Screener_parser
import Write_to_sql as wts


def DownloadData_and_write(symbol, api):
    '''Совмещает все функции.
        Получает данные, проверяет на ошибку.
        Если все хорошо, производит запись в csv,
        после записывает в базу данных
    '''
    functions = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]

    av.delete_folder(symbol)
    for param in functions:
        req = av.get_data_alphavantage_and_check_requests(symbol, param)
        if req == 'ConnectionError':
            return 'ConnectionError'
        elif req == 'EmptyData':
            return 'EmptyData'
        elif req == 'NotData':
            return 'NotData'
        elif req == 'error':
            return 'error'
        av.write_to_json(req, symbol, param)
    av.convert_json_to_csv(symbol, functions)
    # av.delete_temp_files(symbol,param)
    wts.create_table_and_header(symbol)
    wts.insert_into_table_value(gf.path('quarterly_db'), gf.path('annual_db'), symbol)


def write_ticker_to_csv(name_csv='ticker.csv'):
    print('Записываю тикеры в файл csv из finviz_list')
    path_file = os.path.join(gf.path('csv'), name_csv)
    path = os.path.join(gf.path('csv'), 'finviz_list.csv')
    data = csv.reader(open(path), quoting=csv.QUOTE_MINIMAL)
    row_count = sum(1 for row in data)  # длина файла для прогрес бара
    data = csv.reader(open(path), quoting=csv.QUOTE_MINIMAL)
    if os.path.exists(path_file):
        os.remove(path_file)
    with alive_bar(row_count) as bar:
        for row in data:
            bar()
            name = []
            name.append(row[2])
            file1 = (open(os.path.join(gf.path('csv'), name_csv), 'a', newline=''))
            with file1:
                writer = csv.writer(file1)
                writer.writerow(name)


def gen_count():
    n = 0
    while True:
        n += 1
        yield n


def add_ticker_to_txt():
    path = os.path.join(gf.path('csv'), 'finviz_list.csv')
    string = ''
    file = open(path)
    data = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
    for row in data:
        string += row[2] + ','
    string = string[:-1]
    f = open(os.path.join(gf.path('csv'), 'ticker.txt'), 'w')
    f.write(string)
    f.close()


def abar(len):
    '''Строка состояния для цыкла'''
    with alive_bar(len) as bar:
        for a in range(len):
            bar()
            time.sleep(1)


def check_input():
    n = input('---> ')
    if n.isdigit():
        n = int(n)
        return n
    else:
        print('Введите число, а не строку\n')
        time.sleep(1)
        return 'string'


def clear_shell():
    return os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    clear_shell()
    while True:
        clear_shell()
        print(
            '1) Finviz screener\n2) TradingView earning\n3) Finviz and TradingView\n4) Download data and write to SQL\n5) Other\n\n0) Exit')
        # a = input('---> ')
        a = check_input()
        if a == 'string':
            continue
        if a == 1:
            while True:
                clear_shell()
                print('1 - Вывести весь список\n2 - Только которые ниже 10$\n\n0 - Return back ')
                b = check_input()
                if b == 'string':
                    continue
                if b == 1:
                    Screener_parser.finviz_all_stocks()
                    print('Готово!\nДанные загружены')
                    os.system('pause')
                elif b == 2:
                    Screener_parser.finviz_all_stocks(all_ticker=False)
                elif b == 0:
                    break
                else:
                    print("Неправильное значение!")
                    time.sleep(1)
                    continue
            continue
        elif a == 2:
            Earning_TradingView.tradingview_earning()
        elif a == 3:
            Earning_TradingView.tradingview_earning()
            Screener_parser.finviz_all_stocks()
        elif a == 4:
            clear_shell()
            a = gen_count()
            b = gen_count()
            c = gen_count()
            conError, NotData, EmptyData = 0, 0, 0
            iter, last_iter = [int(x) for x in input(
                "Введите начало и конец интервала через дефис (для отменны введите '0-0')\n--->\t").split('-')]
            if (iter and last_iter) == 0:
                continue
            count = 1
            f = av.read_ticker()
            api = av.read_api_key()
            for i in range(iter, last_iter):
                if (conError or NotData or EmptyData) > 0:
                    print('Ошибка соеденения: {}, нету данных {}, пустой ответ {}'.format(conError, NotData, EmptyData))
                print(i)
                print('Обрабатываю {}'.format(f[i]))
                func = DownloadData_and_write(f[i], api[7])
                if func == 'ConnectionError':
                    conError = next(a)
                    abar(60)
                    continue
                elif func == 'NotData':
                    NotData = next(b)
                    abar(60)
                    continue
                elif func == 'EmptyData':
                    EmptyData = next(c)
                    abar(60)
                    continue
                elif func == 'error':
                    abar(60)
                    continue
                abar(60)

        elif a == 5:
            while True:
                clear_shell()
                print('1- Add ticker to txt from finviz_list\n\n0 - Return back ')
                key = check_input()
                if key == 'string':
                    continue
                if key == 1:
                    write_ticker_to_csv()
                    add_ticker_to_txt()
                    print('Готово!\nДанные загружены')
                    os.system('pause')
                elif key == 0:
                    break
                else:
                    print("Неправильное значение!")
                    time.sleep(1)
            continue
        elif a == 0:
            break
        else:
            print("Неправильное значение!")
            time.sleep(1)
            continue
