import json


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


url = input('Адрес сайта: ')

inputs_id = []

inputs_count = int(input("Количество вводов: "))

print("""
    \n
    1 - Имя
    2 - Фамилия
    3 - Отчество
    4 - Рандомная банковская карта
    5 - Срок действия карты ММ/ГГ
    6 - CVV
    7 - Рандомное число (круглое)
    8 - Рандомная почта
    \n
""")

for i in range(inputs_count):
    _temp_id = input(f'Input #{i+1} Name: ')
    _temp_type = int(input('Тип поля: '))
    _temp = {
        'id': _temp_id,
        'type': _temp_type
    }
    inputs_id.append(_temp)

data = {
    'url': url,
    'ids': inputs_id
}

write(data, 'settings.json')
