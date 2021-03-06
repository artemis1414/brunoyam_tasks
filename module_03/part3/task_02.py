import re

def search_small_words(string):
    my_list = re.split(r'\W', string)
    small_words = [word for word in my_list if (len(word) < 5 and word != '')]
    return small_words


s = """Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошел с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжет листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!"""

print(search_small_words(s))
