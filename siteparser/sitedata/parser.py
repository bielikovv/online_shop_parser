import requests
from bs4 import BeautifulSoup
import pymysql


def parser(url, tag, clas):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    items = soup.find_all(tag, class_=clas)
    return items

def add_to_db(item, title_of_table):
    for el in item:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='vitrum15',
            db='actual_info_parser',
        )
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO {title_of_table} (title, price, link, reviews)
            VALUES ('{el['title']}', '{el['price']}', '{el['link']}', '{el['reviews']}')
        """)
        connection.commit()





# #ROZETKA
# for item in parser('https://hard.rozetka.com.ua/computers/c80095/', 'div', 'goods-tile ng-star-inserted'):
#     lst = []
#     lst.append({
#         'title': item.find('span', class_='goods-tile__title').get_text(),
#         'price': item.find('span', class_='goods-tile__price-value').get_text(),
#         'link': item.find('a', class_='goods-tile__heading ng-star-inserted').get('href'),
#         'reviews': item.find('div', class_='goods-tile__stars ng-star-inserted').get('span'),
#     })
#
#     add_to_db(lst, 'sitedata_rozetkasite')



#FOXTROT.UA
for item in parser('https://www.foxtrot.com.ua/ru/search?query=%D0%9A%D0%9E%D0%9C%D0%9F%D0%AC%D0%AE%D0%A2%D0%95%D0%A0%D0%AB', 'div', 'card'):
    lst = []
    lst.append({
        'title': item.find('a', class_='card__title').get_text(),
        'price': item.find('div', class_='card-price').get_text(),
        'link': item.find('a', class_='card__title').get('href'),
        'reviews': item.find('div').get('span'),
    })
    for i in lst:
        i['link'] = 'https://www.foxtrot.com.ua' + i['link']

    add_to_db(lst, 'sitedata_foxtrotsite')



# # ALLO.UA
# for item in parser('https://allo.ua/ru/kompjutery/', 'div', 'product-card'):
#     lst = []
#     lst.append({
#         'title': item.find('a', class_='product-card__title').get_text(),
#         'price': item.find('span', class_='sum').get_text(),
#         'link': item.find('a', class_='product-card__title').get('href'),
#         'reviews': item.find('span', class_='review-button__text').get_text(),
#     })
#
#     add_to_db(lst, 'sitedata_allosite')






