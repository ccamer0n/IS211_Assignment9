from bs4 import BeautifulSoup
import requests
import csv


url = "https://chemazone.com/unit_periodictable.htm"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html5lib")
#print(soup.prettify())

links = soup.find("div", attrs={"class":"periodic-table"})
#links = soup.find_all("input", attrs={"name":"elements"})
for link in links.find_all("div", attrs={"class":"label"}):
    print(link)

#    for row in link.find("div", attrs={"class":"name"}):
#        print(link)
