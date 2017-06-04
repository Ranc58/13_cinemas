import requests
import random
from bs4 import BeautifulSoup as bs
from kinopoisk.movie import Movie


def fetch_afisha_page(url_afisha):
    afisha_raw_html = requests.get(url_afisha).content
    return afisha_raw_html


def parse_afisha_list(afisha_raw_html):
    parse_info = bs(afisha_raw_html, "lxml")
    movie_list = parse_info.find('div',
                                 {'class':
                                  'b-theme-schedule m-schedule-with-collapse'})
    movies = movie_list.findAll('div',
                                {'class':
                                 'object s-votes-hover-area collapsed'})
    films_cinemas_count_list = []
    for item in movies:
        film_name = item.find('h3', {'class': 'usetags'})
        cinemas = item.findAll('td', {'class': 'b-td-item'}, 'a')
        cinemas_count = len(cinemas)
        film_info_dict = {'name': film_name.text,
                          'cinemas_count:': cinemas_count}
        films_cinemas_count_list.append(film_info_dict)
    return films_cinemas_count_list


def get_kinopoisk_films_id(films_cinemas_count_list):
    kinopoisk_ids = []
    for movie in films_cinemas_count_list:
        movies = Movie.objects.search(movie['name'])
        movie_from_afisha = movies[0]
        movie_id_and_name = {'id':movie_from_afisha.id,
                             'name':movie_from_afisha.title}
        kinopoisk_ids.append(movie_id_and_name)
    return kinopoisk_ids


def get_rate_kinopoisk(kinopoisk_ids):
    kinopoisk_rates = []
    for movie in kinopoisk_ids:
        context = requests.get('https://rating.kinopoisk.ru/{}.xml'. # TODO edit format to params!
                               format(movie['id']))
        moive_rate = bs(context.text, 'lxml')
        rate = moive_rate.find('kp_rating')
        counts_rate = moive_rate.find('kp_rating')['num_vote']
        rating_dict={'rate':rate.text,
                     'counts_rate':counts_rate}
        kinopoisk_rates.append(rating_dict)
    return kinopoisk_rates


def dicts_unite(kinopoisk_ids,kinopoisk_rates):
    for movie in kinopoisk_ids:
        for rate in kinopoisk_rates:
            movie.update(rate)
    print(kinopoisk_ids)


if __name__ == '__main__':
    url_afisha = 'https://www.afisha.ru/msk/schedule_cinema/#'
    afisha_raw_html = fetch_afisha_page(url_afisha)
    films_cinemas_count_list = parse_afisha_list(afisha_raw_html)
    kinopoisk_ids = get_kinopoisk_films_id(films_cinemas_count_list)
    kinopoisk_rates=get_rate_kinopoisk(kinopoisk_ids)
    dicts_unite(kinopoisk_ids,kinopoisk_rates)