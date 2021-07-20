import json


def login_function(login, passwd):
    with open('Data.json', mode='r') as file:
        dict_logins = json.loads(file.read())
        if login in dict_logins:
            if dict_logins[login] == passwd:
                print('Вход в систему произошел успешно!')
                return 0
            else:
                print('Проверьте правильность пароля.')
                return 1
        else:
            print('Такого логина не существует, проверьте правильность введенного логина.')
            return 1


x = 1
while x:
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    x = login_function(login, password)
