import time
from threading import Thread


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


threads = [Thread(target=get_thread, args=[f'Поток №{i + 1}']) for i in range(5)]

t_seq = time.time()
thread_names = [f'Поток №{i + 1}' for i in range(5)]
for i in range(5):
    get_thread(thread_names[i])
print(f'Время последовательного выполнения: {time.time() - t_seq}')
t_par = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время параллельного выполнения: {time.time() - t_par}')
