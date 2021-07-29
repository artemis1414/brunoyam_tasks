

class StringVar:

    def __init__(self, string):
        self.__string = string

    def set(self, string):
        self.__string = string
        return self.__string

    def get(self):
        return self.__string


s = StringVar(input('Введите строку: '))
print(s.get())
print(s.set('new string'))

