import csv
import sqlite3


def database(file):
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = []
        for row in csv_reader:
            new_dict = {}
            for k, v in row.items():
                if k != 'id':
                    new_dict[k] = v
            data_list.append(new_dict)

    conn = sqlite3.connect('ScrapDB.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE ScrapData
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      headline TEXT,
                      URL TEXT,
                      author TEXT,
                      date TEXT)''')
    except:
        for row in data_list:
            c.execute('''SELECT * FROM ScrapData WHERE headline=? AND URL=? AND author=? AND date=?''',
                      (row['headline'], row['URL'], row['author'], row['date']))
            if c.fetchone() is not None:
                continue
            else:
                c.execute('''INSERT INTO ScrapData (headline, URL, author, date)
                         VALUES (?, ?, ?, ?)''', (row['headline'], row['URL'], row['author'], row['date']))
        conn.commit()
        # uncomment the below if you need to see stored data in database
        print('=========================================Database Query=========================================')
        c.execute('''SELECT * FROM ScrapData''')
        results = c.fetchall()
        for row in results:
            print(row)
        conn.close()
