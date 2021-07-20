password = input('Введите пароль: ')
while len(password) < 8 or password.islower() or password.isupper():
	password = input('Повторите ввод пароля: ')
