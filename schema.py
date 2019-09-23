import sqlite3


def run(dbname='coins.db'):

    CON = sqlite3.connect(dbname)
    CUR = CON.cursor()

    CUR.execute("""DROP TABLE IF EXISTS coins;""")
    # create USER table FOR LOGIN AND SESSION
    CUR.execute("""CREATE TABLE coins(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        symbol VARCHAR,
        href INTEGER);""")

    # CUR.execute("""DROP TABLE IF EXISTS search_terms;""")
    # #search term history
    # CUR.execute("""CREATE TABLE search_terms(
    #     pk INTEGER PRIMARY KEY AUTOINCREMENT,
    #     time INTEGER,
    #     coin_pk INTEGER,
    #     FOREIGN KEY(coin_pk) REFERENCES coins(pk)
    # );""")

    CON.commit()
    CUR.close()
    CON.close()

if __name__ == '__main__':
    run()