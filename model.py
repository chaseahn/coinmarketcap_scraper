# this is a scraper for coinmarketcap.com
# the goal of the program is to extract:
# coin name, symbol and image

import os
import requests

from bs4 import BeautifulSoup


class Scraper():

    def __init__(self):

        self.url        = 'https://www.coinmarketcap.com/all/views/all/'
    
    def scrape_site(self):

        data    = {} #final object for list_to_csv
        coin_id = 0  

        res  = requests.get(self.url)
        html = BeautifulSoup(res.content, 'html.parser')

        if html:
            
            coin_list = html.find_all('tr')

            for coin in coin_list[1:]:

                coin_container = coin.find_all('td')
                
                coin_name = coin_container[1].text.strip().split('\n')[2]
                coin_symb = coin_container[1].text.strip().split('\n')[0]
                coin_href = '/currencies/' + coin_name.lower()

                print([coin_name, coin_symb, coin_href])

                #seed to database

                break
        else:
            print("Couldn't Find")

class SQLite():

    def __init__(self):
        pass



        


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape_site()