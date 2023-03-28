from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html5lib")
print(soup.prettify())

links = soup.find("tbody", attrs={"class":"lister-list"})
for link in links.find_all("td", attrs={"class":"titleColumn"}):
    print(link)

#    for row in link.find("div", attrs={"class":"name"}):
#        print(link)
