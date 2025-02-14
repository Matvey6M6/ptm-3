import csv 
import re 
import checksum

VAR=33
PATTERNS ={
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "http_status_message" : "^\\d{3}\\s[^\n\r]+$",
    "snils": "^\d{11}$",
    "passport": "^\d{2} \d{2} \d{6}$",
    "ip_v4": "^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "hex_color": "^#[0-9a-fA-F]{6}$",
    "issn": "^\d{4}-\d{4}$",
    "isbn": "\\d+-\\d+-\\d+-\\d+(:?-\\d+)?$",
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$"
}


def read_file(name:str = str(VAR)) -> list:
    '''
        Считываем данные с csv файла
        name(str): имя csv файла
        return: двумерный массив считанных данных 
    '''
    rows = []
    with open(f"{name}.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for i in read_data:
            rows.append(i)
    rows.pop(0)
    return rows


def check_row(row: list) -> bool:
    '''
    Проверяет одну строку на валидность 
    row(list): данные одной строки по типу(email и тд)
    return(bool): возвращает False если данные невалидные
    '''
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
    return True


def get_index_invalid_data(data:list)->list:
    '''
        Функция возвращает индексы невалидных данных
        data(list): данные которые нужно проверить 
        return(list): массив с индексами невалидных данных
    '''
    index_data = []
    i = 0
    for row in data:
        if(check_row(row) == False):
            index_data.append(i)
        i+=1
    return index_data


if __name__ == "__main__":
    data = read_file()
    summ = checksum.calculate_checksum(get_index_invalid_data(data))
    print(sum(get_index_invalid_data(data)))
    checksum.serialize_result(VAR, summ)