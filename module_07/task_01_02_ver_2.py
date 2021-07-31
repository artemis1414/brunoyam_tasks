import bs4
import requests
import matplotlib.pyplot as plt

response = requests.get('https://yandex.ru/news/quotes/1.html')
text_page = response.text

soup = bs4.BeautifulSoup(response.text, 'lxml')
table_kurs_usd = soup.find_all('div', {'class': 'news-stock-table__cell'})
table = [usd.text for usd in table_kurs_usd]
usd_table_dict = {}
for data in range(3, len(table), 3):
    usd_table_dict[table[data]] = table[data + 1]


dates = [i for i in reversed(usd_table_dict)]
value_usd = [usd_table_dict[i] for i in dates]
for i in range(len(value_usd)):
    value_usd[i] = float(value_usd[i].replace(',', '.'))

plt.plot(dates, value_usd)
plt.show()
