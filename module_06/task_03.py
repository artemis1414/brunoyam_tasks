import time
from requests import get
from threading import Thread

def get_html(link):
    text_web = get(link)
    print(f'Загрузка {link} завершена успешно!')
    return text_web


list_html = ['https://yandex.ru/', 'https://github.com/', 'https://www.google.ru/',
             'https://projecteuler.net/', 'https://www.flaticon.com/']
threads = [Thread(target=get_html, args=[list_html[i]]) for i in range(5)]

t_seq = time.time()
for i in range(5):
    get_html(list_html[i])
print(f'Время последовательного выполнения: {time.time() - t_seq}')
t_par = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время параллельного выполнения: {time.time() - t_par}')