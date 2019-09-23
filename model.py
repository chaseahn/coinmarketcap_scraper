#!/usr/bin/env python3

import os
import time
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

        self.url        = 'https://www.coinmarketcap.com'
        self.coins_href = '/all/views/all/'
    
    def scrape_site(self):

        data    = {} #final object for list_to_csv
        coin_id = 0  

        res  = requests.get(self.url + self.coins_href)
        html = BeautifulSoup(res.content, 'html.parser')

        if html:
            
            coin_list = html.find_all('tr')

            for coin in coin_list[1:]:

                coin_container = coin.find_all('td')
                
                coin_name = coin_container[1].text.strip().split('\n')[2]
                coin_symb = coin_container[1].text.strip().split('\n')[0]
                coin_href = '/currencies/' + coin_name.lower()

                print([coin_name, coin_symb, coin_href])

                #download image

                #seed to database

                break
        else:
            print("Couldn't Find")

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
        row              = dict(row)
        self.pk          = row.get('pk')
        self.coin_name   = row.get('coin_name')
        self.coin_symbol = row.get('coin_symbol')
        self.coin_href   = row.get('coin_href')

class SQLite():

    def __init__(self):
        self.path        = ' '
    
    def load_dictionary(filename):
        """imports json file as a dictionary"""
        with open(filename, 'r') as json_file:
            return json.load(json_file)

    def run():

        # open connection to db
        conn = sqlite3.connect(dbname)
        cur  = conn.cursor()

        PARENT_SQL = """INSERT INTO coins (
                     name, symbol, href ) 
                     VALUES (?, ?, ?); """

        # importing the raw data json file created through scraper
        dcty = load_dictionary(self.path)

        for key in dcty.keys():

            name   = key.strip()
            symbol = dcty[key]['symbol']
            href   = dcty[key]['href']

            # populate all values in table
            sql_values = (name, symbol, href)
            cur.execute(PARENT_SQL, sql_values)

        # close connection to db
        conn.commit()
        conn.close()


        


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape_site()