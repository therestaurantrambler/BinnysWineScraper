# This program scraps binnys.com for wine prices. There are 12,089 wimes listed on the site

import requests
from bs4 import BeautifulSoup
import csv

# Define a variable for the binny's page to be scraped
URL = "https://www.binnys.com/wine?p=1"


# Send a request to the server and store the data in an object called r
r = requests.get(URL)

# Create a Beautiful soup instance and pass in the content r and the parsing library
soup = BeautifulSoup(r.content, 'html5lib')


#Create an array (called wine) to store the content of the scrape.
wines = []

# Examine the parse tree table. Find the division that holds all the products.
table = soup.find('div', attrs= {'class':'row'})
#print(table.prettify())

#Iterate through all the products to find division where name and price are located.

for row in table.findAll('div', attrs= {'class':'col'}):

    wine = {}
    wine['name'] = row.a['data-product-name']
    wine['brand'] = row.a['data-brand']
    wine['color'] = row.a['href'].split("/")[2]
    wine['varietal'] = row.a['href'].split("/")[3]
    wine['price'] = row.a['data-price']


    wines.append(wine)


# Create the csv file with wine name and price

filename = 'binnys_wine_05_28_21.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','brand','color','varietal','price'])
    w.writeheader()
    for wine in wines:
        w.writerow(wine)