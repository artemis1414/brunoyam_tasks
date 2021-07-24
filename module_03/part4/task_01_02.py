import json


def register(login, passwd):

    with open('Data.json', mode='r') as file:
        dict_logins = json.loads(file.read())
        if login in dict_logins:
            print('Пользователь с логином', login, 'уже существует!')
        else:
            dict_logins.setdefault(login, passwd)
            print('Пользователь с логином', login, 'добавлен')
    with open('Data.json', mode='w') as f:
        f.write(json.dumps(dict_logins))


try:
    with open('Data.json', mode='r') as file:
        pass
except FileNotFoundError:
    with open('Data.json', mode='w') as file:
        file.write(json.dumps({}))
while True:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    register(login, password)
    i = input('Продолжить? Введите YES или NO: ').upper()
    if i == 'NO':
        break
