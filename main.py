import csv
import datetime
from Scrapper import HomePage, SpecificPage
from db import database
import os

# getting date in ddmmyy format using strftime method
ddmmyy = datetime.datetime.now().strftime("%d%m%y")
# storing ddmmyy_verge.csv files in Csv_Data_Files directory
file_name = os.getcwd() + '/' + ddmmyy + "_verge.csv"
# calling scrap data method which are declared in module Scrapper
resData = HomePage().getData() + SpecificPage().getData()
# opening csv file in write mode
# csv_file is a identifier of csv file object
with open(file_name, mode="w", newline="") as csv_file:
    # declaring coloumn names
    fieldnames = ['id', 'headline', 'URL', 'author', 'date']
    # creating writter object
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # writing header to csv file using wwriter object
    writer.writeheader()
    id = 1
    for my_dict in resData:
        # writing each dict as row to csv file
        writer.writerow({'id': id, 'headline': my_dict['headline'], 'URL': my_dict['URL'], 'author': my_dict['author'],
                         'date': my_dict['date']})
        # incrementing id value
        id += 1
# calling database method in db module in order store or update the daily scraped data
database(file_name)
