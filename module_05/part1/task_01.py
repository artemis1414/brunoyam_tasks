

class StringVar:

    def __init__(self, string):
        self.string = string

    def set(self):
        self.string = input('Введите измененную строку: ')
        return self.string

    def get(self):
        return self.string


s = StringVar(input('Введите строку: '))
print(s.set())
print(s.get())
