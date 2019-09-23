
import os
import time
import sqlite3
import requests

from time import sleep
from random import randint
from opencursor import OpenCursor

from bs4 import BeautifulSoup


class Scraper():

    # this is a scraper for coinmarketcap.com
    # the goal of the program is to extract:
    # coin name, symbol and href

    def __init__(self):

        self.url      = 'https://www.coinmarketcap.com'
        self.view_all = '/all/views/all/'
    
    def scrape_site(self):

        data    = {} #final object for list_to_csv
        coin_id = 0  

        res  = requests.get(self.url + self.view_all)
        html = BeautifulSoup(res.content, 'html.parser')

        if html:
            
            coin_list = html.find_all('tr')

            for coin in coin_list[1:]:

                coin_container = coin.find_all('td')
                
                coin_name   = coin_container[1].text.strip().split('\n')[2]
                coin_symbol = coin_container[1].text.strip().split('\n')[0]
                coin_href   = '/currencies/' + coin_name.lower()

                coin_dict = { 'name': coin_name,
                              'symbol': coin_symbol, 
                              'href': coin_href.replace(' ', '-') }

                print('Seeding ' + coin_dict['name'])

                #seed to database
                db = SQLite()
                db.add_coin(coin_dict)

        else:
            print("Couldn't Find Page.")

        def coin_page(self):
            pass 

class Coins():

    def __init__(self, row={}, coin_name=''):
        if coin_name:
            self.check_coin(coin_name)
        else:
            self.row_set(row)

    def __enter__(self):
        return self

    def __exit__(self,exception_type,exception_value,exception_traceback):
        sleep(randint(10,10000)/10000)

    def row_set(self,row={}):
        row         = dict(row)
        self.pk     = row.get('pk')
        self.name   = row.get('name')
        self.symbol = row.get('symbol')
        self.href   = row.get('href')

class SQLite():

    def __init__(self):
        self.path        = ' '

    def add_coin(self, coin_dict):

        # open connection to db
        conn = sqlite3.connect("coins.db")
        cur  = conn.cursor()

        PARENT_SQL = """INSERT INTO coins (
                     name, symbol, href ) 
                     VALUES (?, ?, ?); """

        name   = coin_dict['name']
        symbol = coin_dict['symbol']
        href   = coin_dict['href']

        # populate all values in table
        sql_values = (name, symbol, href)
        cur.execute(PARENT_SQL, sql_values)

        # close connection to db
        conn.commit()
        conn.close()

    def __exit__(self,exception_type,exception_value,exception_traceback):
        sleep(randint(10,10000)/10000)


        


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape_site()