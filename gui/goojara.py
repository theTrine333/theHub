import requests
from bs4 import BeautifulSoup
import multitasking

main_url = "https://www.goojara.to"
local_headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*",
    "Accept-Language": "en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36",
    "Connection": "keep-alive"
}

def getMovies(page):
    moviesList = []
    movies_url = f"{main_url}/watch-movies?p={page}"
    try:
        req = requests.get(movies_url)
        soup = BeautifulSoup(req.text, "html.parser")
        movies = soup.findAll("div",class_="dflex")
        for movie in movies:
            details = movie.findAll("a")
            for detail in details:
                movie = detail.find('img')
                movie_name = detail['title']
                movie_link = detail['href']
                movie_image = movie['data-src']
                moviesList.append([movie_name, movie_link, movie_image])     
        return moviesList
    except Exception as E:
        print(f"An error occurred: {E}")
def getMovieDetails(detailsurl):
    try:
        movie_details_page = f"{main_url}{detailsurl}"
        movie_req = requests.get(movie_details_page)
    except Exception as E:
        movie_details_page = f"{detailsurl}"
        movie_req = requests.get(movie_details_page)
    detailsSoup = BeautifulSoup(movie_req.text,"html.parser")
    movieDetails = []
    movie_details_ = detailsSoup.find("div",class_='fimm').findAll('p')
    description = movie_details_[0].text
    movie_director = movie_details_[1].text
    cast = movie_details_[2].text
    movieDetails.append([description,movie_director,cast])
    movie_req.close
    return movieDetails

def getPopularMovies():
    popular_movie_page = "https://www.goojara.to/watch-movies-popular"
    try:
        req = requests.get(popular_movie_page)
        popular_movies = []
        soup = BeautifulSoup(req.text, "html.parser")
        movies = soup.findAll("div",class_="dflex")

        for movie in movies:
            details = movie.findAll("a")
            for detail in details:
                movie = detail.find('img')
                movie_name = detail['title']
                movie_link = detail['href']
                movie_image = movie['data-src']
                popular_movies.append([movie_name, movie_link, movie_image])
                
        return popular_movies
    except Exception as E:
        print(f"An error occurred: {E}")
        
def getAnimations():
    animations_page = "https://www.goojara.to/watch-movies-genre-Animation"
    try:
        req = requests.get(animations_page)
        animated_movies = []

        soup = BeautifulSoup(req.text, "html.parser")

        animated_movies = soup.findAll("div",class_="dflex")

        for animated_movie in animated_movies[1]:
            details = animated_movie.findAll("a")
            for detail in details:
                movie = detail.find('img')
                movie_name = detail['title']
                movie_link = detail['href']
                movie_image = movie['data-src']
                animated_movies.append([movie_name, movie_link, movie_image])
                
        return animated_movies
    except Exception as E:
        print(f"An error occurred: {E}")
        
def getAction():
    action_movies_page = "https://www.goojara.to/watch-movies-genre-Action"
    try:
        req = requests.get(action_movies_page)
        action_movies = []
        soup = BeautifulSoup(req.text, "html.parser")
        movies = soup.findAll("div",class_="dflex")
        for movie in movies:
            details = movie.findAll("a")
            for detail in details:
                movie = detail.find('img')
                movie_name = detail['title']
                movie_link = detail['href']
                movie_image = movie['data-src']
                action_movies.append([movie_name, movie_link, movie_image])
                
        return action_movies
    except Exception as E:
        print(f"An error occurred: {E}")