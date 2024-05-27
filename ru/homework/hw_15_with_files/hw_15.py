# # 1) Сделать парсинг сайта https://quotes.toscrape.com и вытащить всех авторов с подробной информацией о каждом:
# # дата и место рождения, описание и сохранить в текстовый файл

import requests
from bs4 import BeautifulSoup

# Шаг 1: Получение имен авторов и сохранить их в словарь
def parse_details_of_author(author_url):
    response = requests.get(author_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        birth_date = soup.find('span', class_='author-born-date').text
        birth_place = soup.find('span', class_='author-born-location').text
        description = soup.find('div', class_='author-description').text.strip()
        return f"Date of Birth: {birth_date}\nPlace of Birth: {birth_place}\nDescription: {description}"
    else:
        return None

def parse_authors_from_quotes_website():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    authors_dict = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for author in soup.find_all('small', class_='author'):
            author_name = author.text
            author_url = url + 'author/' + author.find_next('a')['href'].split('/')[2]
            authors_dict[author_name] = author_url
        return authors_dict
    else:
        print('Failed to retrieve data from the website.')
        return None

# 2 Шаг. Получение информации об авторах и сохранение в файл
authors_dict = parse_authors_from_quotes_website()

if authors_dict:
    with open('author_info.txt', 'w', encoding='utf-8') as file:
        for author_name, author_url in authors_dict.items():
            author_info = parse_details_of_author(author_url)
            if author_info:
                file.write(f"{author_name}:\n{author_info}\n\n")
    print('Author information saved to author_info.txt file.')
else:
    print('No author data available to save.')

# 2) Сделать парсинг сайта https://2krossovka.ru
# и вытащить первые 108 товаров с подробной информацией о всех характеристиках,
# которые открываются у каждого товара в отдельной странице.

import requests
from bs4 import BeautifulSoup

k = 1
for page in range(1, 2):
    url = f'https://2krossovka.ru/katalog/?page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='caption')
        for product in products:
            title = product.h4.a.text.strip()
            price = product.p.text.strip()
            url_product = product.h4.a['href'].strip()
            print(k, title, price, url_product)
            k += 1
            print()

# 3) С помощью АПИ сайта https://randomuser.me/api рандомно вытащить полную информацию о 5 юзерах

import requests
params = {
    'results': 5
}
response = requests.get('https://randomuser.me/api', params=params)
if response.status_code == 200:
    data = response.json()
    if 'results' in data:
        users = data['results']
        for index, user in enumerate(users, start=1):
            print(f"User {index}:")
            print(f"Name: {user['name']['first']} {user['name']['last']}")
            print(f"Gender: {user['gender']}")
            print(f"Email: {user['email']}")
            print(f"Location: {user['location']['city']}, {user['location']['country']}")
            print("")
    else:
        print("Нет данных о пользователях.")
else:
    print("Ошибка!")




