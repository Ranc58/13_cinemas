import requests
from bs4 import BeautifulSoup as bs


def fetch_afisha_page(url):
    afisha_raw_html = requests.get(url).content
    return afisha_raw_html


def parse_afisha_list(afisha_raw_html):
    parse_info = bs(afisha_raw_html, "lxml")
    movie_list = parse_info.find('div', {'class': 'b-theme-schedule m-schedule-with-collapse'})
    movies = movie_list.findAll('div', {'class': 'object s-votes-hover-area collapsed'})
    films_and_cinemas_count_list = []
    for item in movies:
        film_name = item.find('h3', {'class': 'usetags'})
        cinemas = item.findAll('td', {'class': 'b-td-item'}, 'a')
        cinemas_count = len(cinemas)
        kinos = {'name': film_name.text,
                 'cinemas_count:': cinemas_count}
        films_and_cinemas_count_list.append(kinos)
    return films_and_cinemas_count_list


def fetch_movie_info(movie_title):
    pass


def output_movies_to_console(movies):
    pass


if __name__ == '__main__':
    url = 'https://www.afisha.ru/msk/schedule_cinema/#'
    afisha_raw_html = fetch_afisha_page(url)
    parse_afisha_list(afisha_raw_html)
