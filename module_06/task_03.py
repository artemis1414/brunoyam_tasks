import time
import requests
from threading import Thread

def get_html(link):
    response = requests.get(link)
    head = response.headers
    body = [head[i] for i in head]
    print(f'Загрузка {link} завершена успешно!')
    return body


list_html = ['https://yandex.ru/', 'https://github.com/', 'https://www.google.ru/',
             'https://projecteuler.net/', 'https://www.flaticon.com/']
threads = [Thread(target=get_html, args=[list_html[i]]) for i in range(5)]

t_seq = time.time()
for i in range(5):
    print(get_html(list_html[i]))
print(f'Время последовательного выполнения: {time.time() - t_seq}')
t_par = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время параллельного выполнения: {time.time() - t_par}')