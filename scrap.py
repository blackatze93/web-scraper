from bs4 import BeautifulSoup
import requests
import pandas as pd
from pprint import pprint

pub_names = []
journals = []
data = []
url='https://scienti.minciencias.gov.co/gruplac/jsp/visualiza/visualizagr.jsp?nro=00000000005315'
# url = input("Ingrese URL del grupo: ")

# Get info from the page with requests and analyzing with bs4
page=requests.get(url)
if (page.status_code == 200):
    soup=BeautifulSoup(page.content, 'lxml')

    # Find all tables in the page
    tables = soup.find_all('table')

    # Table 0 contain the info for the group and 13 contain the productions
    info = tables[0]
    prod = tables[13]

    # Find all rows containing info from the table
    rows = prod.find_all('td', align=False)

    # Delete the first row containing table title
    del rows[0]

    for i in range(len(rows)):
        # Get the row info from bs4    
        pub_name = rows[i].contents[2].strip()
        journal = rows[i].contents[4].strip().split(', ')
        # Split the journal info and the data for year of pub
        journal[1] = journal[1].split(' ISSN: ')
        journal[2] = journal[2].split(' ')
        # Add item to the list
        pub_names.append(pub_name)
        journals.append(journal)

    for journal in journals:
        pprint(journal)

    for pub_name in pub_names:
        pprint(pub_name)
else:
    print('Error: ' + str(page.status_code))
# TODO
# Search the journal info in the db 

# data = {'Publication Name': pub_names,
#         'Journal': journals}
# df = pd.DataFrame(data)

# print(df)
# Obtaining data info from the page and saving in table_info.html
# f = open("table_info.html", "w")
# for table in tables:
#     f.write(info.prettify())
#     f.write("<br>")
#     f.write(prod.prettify())
# f.close 

# Obtaining data structure from the page and saving in table.html
# f = open("table.html", "w")
# i = 0
# for table in tables:
#     f.write(str(i) + "<br>")
#     f.write(table.prettify())
#     f.write("<br>")
#     i += 1
# f.close 