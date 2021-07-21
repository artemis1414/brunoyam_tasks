password = input('Введите пароль: ')
while True:
	i = 0
	nLowers = 0
	nUppers = 0
	for i in password:
		if i.islower():
			nLowers += 1
		elif i.isupper():
			nUppers += 1
		i += 1
	if len(password) > 8 and nLowers >= 1 and nUppers >= 1:
		break
	password = input('Повторите ввод пароля: ')
