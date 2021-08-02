import bs4
import requests

class RateParser:

    def __init__(self, link_site):
        '''
        Parsing the specified page to find the currency exchange rate table.
        :param link_site:
        '''
        self.__link = link_site
        response = requests.get(self.__link)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        dollar_full_table = soup.find_all('div', {'class': 'news-stock-table__cell'})
        dollar_rate_table = [usd.text for usd in dollar_full_table]
        self.usd_rate_table_dict = {}
        for data in range(3, len(dollar_rate_table), 3):
            self.usd_rate_table_dict[dollar_rate_table[data]] = dollar_rate_table[data + 1]
        for i in self.usd_rate_table_dict:
            self.usd_rate_table_dict[i] = float(self.usd_rate_table_dict[i].replace(',', '.'))

    def site_processing(self):
        return self.usd_rate_table_dict


