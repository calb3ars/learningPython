# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime


quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'https://www.bloomberg.com/quote/INDU:IND', 'https://www.bloomberg.com/quote/AAPL:US']

# for loop
data = []

for pg in quote_page:
    # query the website and return the html to the variable page'
    page = urllib2.urlopen(pg)

    # parse html and store in variable
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class':'name'})
    name = name_box.text.strip()

    # get index price
    price_box = soup.find('div', attrs={'class':'price'})
    price = price_box.text

    data.append((name, price))

with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
        writer.writerow([name, price, datetime.now()])
