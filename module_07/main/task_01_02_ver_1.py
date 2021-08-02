import bs4
import requests
import matplotlib.pyplot as plt


response = requests.get('http://mfd.ru/currency/?currency=USD')
text_page = response.text

soup = bs4.BeautifulSoup(response.text, 'lxml')
table_kurs_usd = soup.find_all('table', {'class': 'mfd-table mfd-currency-table'})
table = [usd.text for usd in table_kurs_usd]
table = table[0].split('\n')
table = [i for i in table if i != '']
usd_table_dict = {}
for data in range(3, len(table), 3):
    usd_table_dict[table[data]] = table[data + 1]
print(usd_table_dict)

dates = [i for i in reversed(usd_table_dict)]
value_usd = [usd_table_dict[i] for i in dates]
for i in range(len(value_usd)):
    value_usd[i] = float(value_usd[i].replace(',', '.'))

plt.plot(dates, value_usd)
plt.show()
