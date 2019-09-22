# this is a scraper for coinmarketcap.com
# the goal of the program is to extract:
# coin name, symbol, href, and image

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
            div = html.find_all('tr')

            print(div)
            print(len(div))


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape_site()