# Cinemas

This script print top-10 movies in Moscow cinemas from [Afisha.ru](https://www.afisha.ru/msk/schedule_cinema/) by rate from [Kinopoisk.ru](https://www.kinopoisk.ru). \
Output can be sorted by rating only or by rating and cinemas counts > 40. \
Script don't output movies with rate counts < 300.

# How to install
1) Recomended use venv or virtualenv for better isolation.\
Venv setup example: \
`python -m venv myenv`\
`source myenv/bin/activate`
2) Install requirements:
`pip3 install -r requirements.txt` (alternatively try add `sudo` before command)
# Quick launch example
1) Output movies only by rate:
```
$ python cinemas.py
Please wait
Movie: "Одержимость".
 have rate: 8.318.
 Cinemas count where shows this movie: 1.

Movie: "Затухающий огонек".
 have rate: 8.118.
 Cinemas count where shows this movie: 1.

Movie: "Ла-Ла Ленд".
 have rate: 8.028.
 Cinemas count where shows this movie: 2.

Movie: "Осенняя соната".
 have rate: 7.981.
 Cinemas count where shows this movie: 1.

Movie: "Большой".
 have rate: 7.922.
 Cinemas count where shows this movie: 54.

Movie: "Любовное настроение".
 have rate: 7.831.
 Cinemas count where shows this movie: 1.

Movie: "Собачья жизнь".
 have rate: 7.776.
 Cinemas count where shows this movie: 3.

Movie: "Невезучие".
 have rate: 7.747.
 Cinemas count where shows this movie: 1.

Movie: "Танцовщик".
 have rate: 7.741.
 Cinemas count where shows this movie: 10.

Movie: "Нелюбовь".
 have rate: 7.679.
 Cinemas count where shows this movie: 118.
```
2) For output movies sorted by rate and cinemas counts use argument `-c`:
```
$ python cinemas.py -c
Please wait
Movie: "Большой".
 have rate: 7.922.
 Cinemas count where shows this movie: 54.

Movie: "Нелюбовь".
 have rate: 7.683.
 Cinemas count where shows this movie: 118.

Movie: "Стражи Галактики. Часть 2".
 have rate: 7.651.
 Cinemas count where shows this movie: 43.

Movie: "Одарённая".
 have rate: 7.43.
 Cinemas count where shows this movie: 57.

Movie: "Меч короля Артура".
 have rate: 7.409.
 Cinemas count where shows this movie: 97.

Movie: "Чудо-женщина".
 have rate: 7.118.
 Cinemas count where shows this movie: 162.

Movie: "Пираты Карибского моря: Мертвецы не рассказывают сказки".
 have rate: 6.685.
 Cinemas count where shows this movie: 170.

Movie: "Чужой: Завет".
 have rate: 6.31.
 Cinemas count where shows this movie: 122.

Movie: "Спасатели Малибу".
 have rate: 5.967.
 Cinemas count where shows this movie: 149.

Movie: "Трио в перьях".
 have rate: 5.807.
 Cinemas count where shows this movie: 50.

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
