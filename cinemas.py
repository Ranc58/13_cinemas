import requests
import argparse
from operator import itemgetter
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
    cinemas_count_list = []
    for item in movies:
        film_name = item.find('h3', {'class': 'usetags'})
        cinemas = item.findAll('td', {'class': 'b-td-item'}, 'a')
        cinemas_count = len(cinemas)
        film_info_dict = {'name': film_name.text,
                          'cinemas_count': cinemas_count}
        cinemas_count_list.append(film_info_dict)
    return cinemas_count_list


def get_kinopoisk_films_id(films_cinemas_count_list):
    kinopoisk_ids = []
    for movie in films_cinemas_count_list:
        movies = Movie.objects.search(movie['name'])
        movie_from_afisha = movies[0]
        movie_id_and_name = {'id': movie_from_afisha.id,
                             'name': movie_from_afisha.title}
        kinopoisk_ids.append(movie_id_and_name)
    return kinopoisk_ids


def get_xml_kinopoisk_list(kinopoisk_ids):
    xml_kinopoisk_list=[]
    for movie in kinopoisk_ids:
        context = requests.get('https://rating.kinopoisk.ru/{}.xml'.  # TODO edit format to params!
                               format(movie['id']))
        xml_kinopoisk_list.append(context)
    return xml_kinopoisk_list


def parse_rate_kinopoisk(xml_kinopoisk_list):
    kinopoisk_rates = []
    for movie in xml_kinopoisk_list:
        moive_rate = bs(movie.text, 'lxml')
        rate = moive_rate.find('kp_rating')
        counts_rate = moive_rate.find('kp_rating')['num_vote']
        rating_dict = {'rate': rate.text,
                       'counts_rate': counts_rate}
        kinopoisk_rates.append(rating_dict)
    return kinopoisk_rates


def get_output_fimls(kinopoisk_ids, kinopoisk_rates, cinemas_count_list):
    movies_info_list = [dict(x, **y)
                        for x, y in zip(kinopoisk_ids, kinopoisk_rates)]
    for d, num in zip(movies_info_list, cinemas_count_list): # TODO change vars
        d['cinemas_count'] = num['cinemas_count']
    for movie in movies_info_list:
        if int(movie['counts_rate']) < 300: # TODO create var for 200
            movies_info_list.remove(movie)
    movies_info_list = sorted(movies_info_list,
                              key=itemgetter('rate'), reverse=True)
    return movies_info_list

"""
def output_films(movies_info_list, parser):
    if parser False:
        for movie in movies_info_list[:10]:
            print('Movie: "{}".\n have rate: {}.\n Cinemas count where show this movie: {}.\n'
                  .format(movie['name'],movie['rate'], movie['cinemas_count']))
    else:
        for movie in movies_info_list:
            if movie['cinemas_count'] < 40:
                movies_info_list.remove(movie)
        for movie in movies_info_list[:10]:
            print('Movie: "{}".\n have rate: {}.\n Cinemas count where show this movie: {}.\n'
                  .format(movie['name'], movie['rate'], movie['cinemas_count']))


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cinemas', nargs='?',
                        help='Only movies in a lot of cinemas')
    return parser
"""

if __name__ == '__main__':
    parser = create_parser_for_user_arguments()
    url_afisha = 'https://www.afisha.ru/msk/schedule_cinema/#'
    afisha_raw_html = fetch_afisha_page(url_afisha)
    cinemas_count_list = parse_afisha_list(afisha_raw_html)
    kinopoisk_ids = get_kinopoisk_films_id(cinemas_count_list)
    xml_kinopoisk_list=get_xml_kinopoisk_list(kinopoisk_ids)
    kinopoisk_rates = parse_rate_kinopoisk(xml_kinopoisk_list)
    movies_info_list=get_output_fimls(kinopoisk_ids, kinopoisk_rates, cinemas_count_list)
    output_films(movies_info_list, parser)