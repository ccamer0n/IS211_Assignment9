from bs4 import BeautifulSoup
import requests

'''This script scrapes periodic table data from https://chemazone.com/unit_periodictable.htm
It outputs the atomic number, symbol, and name of each element in the table.'''

url = "https://chemazone.com/unit_periodictable.htm"
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

table = soup.find(class_="periodic-table")
table_symbol = table.find_all(class_="symbol")
table_name = table.find_all(class_="name")
table_atomic_num = table.find_all(class_="atomic-number")

print("Atomic\nNo     Symbol Element")
print("------ ------ -------")
for symbol, name, atomic_num in zip(table_symbol, table_name, table_atomic_num):
    print(f'{atomic_num.contents[0]}'.ljust(6), f'{symbol.contents[0]}'.ljust(6), name.contents[0])