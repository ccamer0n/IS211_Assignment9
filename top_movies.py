from bs4 import BeautifulSoup
import requests

'''This script scrapes IMDB's top 250 movies from https://www.imdb.com/chart/top/?ref_=nv_mv_250
It outputs the top ten movies, the year they were released, and the community rating.'''

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page = requests.get(url)
count = 0

soup = BeautifulSoup(page.content, "lxml")

movie_list = soup.find(class_="lister-list")
movie_title = movie_list.find_all(class_="titleColumn")
movie_rating = movie_list.find_all(class_="ratingColumn imdbRating")

for movie, rating in zip(movie_title[:10], movie_rating[:10]):
    count += 1
    print(f'{count}.\n{movie.find("a").contents[0]} {movie.find("span").contents[0]} \nIMDB rating: {rating.find("strong").contents[0]}\n')


