password = input('Введите пароль: ')
while True:
	i = 0
	count_1 = 0
	count_2 = 0
	while i < len(password):
		if password[i].islower():
			count_1 += 1
		elif password[i].isupper():
			count_2 += 1
		i += 1
	if len(password) > 8 and count_1 >= 1 and count_2 >= 1:
		break
	password = input('Повторите ввод пароля: ')
