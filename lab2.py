import csv
import re

print('Вводите данные через запятую. Если желаете пропустить вопрос, ничего не вводите и жмите enter')

dates = input('Какие года выхода игры вас интересуют?').split(',')
publishers = input('Какие издатели игр вам интересны?').split(',')
platforms = input('На каких платформах планируете устанавливать игру?').split(',')
categories = input('Какие категории игр предпочтительны? (Multi-player, single-player...)').split(',')
genres = input('Каких жанров игры подыскать?(Action, Strategy...)').split(',')
prices = input('Какая максимальная цена в долларах? (введите только один ответ)')
ratings = input('Напишите "yes", если для вас важно, чтобы положительных отзывов было больше, чем отрицательных:')


def get_date(argument):
    return any(date in argument for date in dates) or (dates == [''])


def get_publisher(argument):
    return any(publisher in argument for publisher in publishers) or (publishers == [''])


def get_platform(argument):
    return any(platform in argument for platform in platforms) or (platforms == [''])


def get_category(argument):
    return any(category in argument for category in categories) or (categories == [''])


def get_genre(argument):
    return any(genre in argument for genre in genres) or (genres == [''])


def get_price(argument, res=prices):
    if res == '':
        return 0.0 <= argument <= 421.99
    else:
        k = float(re.findall(r'[\d.]+', res)[0])
        return 0.0 <= argument <= k


def get_rating(argument):
    return ((ratings == "yes") and argument > 0) or (ratings == '')


with open('steam.csv', encoding='utf-8') as f1, \
        open('recommended_games.txt', 'w', encoding='utf-8') as f2:
    reader = csv.reader(f1)
    for row in reader:
        if row[0] == 'appid':
            continue

        res_dates = row[2].split('-')
        res_publishers = row[5].split(';')
        res_platforms = row[6].split(';')
        res_categories = row[8].split(';')
        res_genres = row[9].split(';')
        res_prices = float(row[17])
        res_ratings = int(row[12]) - int(row[13])

        if (get_date(res_dates) and get_publisher(res_publishers) and get_platform(res_platforms) and
                get_category(res_categories) and get_genre(res_genres) and
                get_price(res_prices) and get_rating(res_ratings)):
            f2.write(row[1] + "\n")
