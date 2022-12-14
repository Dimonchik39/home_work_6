# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

text_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "йцу", "цук", "йцукен", "йцу"]

def find_sec_str(txt_1, sec_str):
    '''
    Функция поиска второго вхождения строки в списке
    Список строк начинается с индекса 1
    '''
    list_index = [i for i, string in enumerate(txt_1, start = 1) if sec_str == string] 
    print(list_index)
    try:
        return list_index[1]
    except IndexError:
        return -1

find_str = 'йцу'
index_result = find_sec_str(text_1, find_str)
print(index_result)