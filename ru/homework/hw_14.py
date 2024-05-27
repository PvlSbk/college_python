# # 1) Скачать XML файл https://drive.google.com/file/d/1_TNSX3RAzlhUx-CabYZznyQrwnsGsoGL/view?usp=sharing
# # 1.1) Спарсить все категории товаров и сохранить в отдельный текстовый файл

import xml.etree.ElementTree as ET
tree = ET.parse('lite_yafbs_prices.ext.xml')
categories = tree.findall(".//category")
with open('parsed_category.txt', 'w', encoding='utf-8') as file:
    for category in categories:
        file.write(f"id: {category.get('id')}\n")
        file.write(f"category: {category.text}\n")
        file.write("\n")
print("Категории товаров сохранены в файл 'parsed_category.txt'")

# 1.2) Спарсить всю информацию о товарах offers(все вложенные теги и атрибуты) и сохранить в отдельный текстовый файл

tree = ET.parse('lite_yafbs_prices.ext.xml')
offers = tree.findall(".//offer")
with open('parsed_info.txt', 'w', encoding='utf-8') as file:
    for offer in offers:
        file.write(f"id: {offer.get('id')}\n")
        file.write(f"available: {offer.get('available')}\n")
        file.write(f"url: {offer[0].text}\n")
        file.write(f"currencyId: {offer[1].text}\n")
        file.write(f"categoryId: {offer[2].text}\n")
        file.write(f"picture: {offer[3].text}\n")
        file.write(f"store: {offer[4].text}\n")
        file.write(f"pickup: {offer[5].text}\n")
        file.write(f"delivery: {offer[6].text}\n")
        file.write(f"name: {offer[7].text}\n")
        file.write(f"count: {offer[8].text}\n")
        file.write(f"vendorCode: {offer[9].text}\n")
        file.write(f"weight: {offer[10].text}\n")
        file.write(f"price: {offer[11].text}\n")
        file.write("\n")

print("Информация о товарах offers(все вложенные теги и атрибуты) сохранена в файл 'parsed_info.txt'")

# 2) Скачать JSON файл https://drive.google.com/file/d/1kLJJLlCbRgZy23lRauFDsIkgDUQts4cm/view?usp=sharing
# Спарсить всю информацию о первых 100 товарах и сохранить её в отдельный текстовый файл

import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('parsed_100.txt', 'w', encoding='utf-8') as parsed_file:
    count = 0
    for item in data['items']:
        if count < 100:
            parsed_file.write(f"item_number: {item}\n")
            parsed_file.write(f"id: {data['items'][item]['id']}\n")
            parsed_file.write(f"title: {data['items'][item]['title']}\n")
            parsed_file.write(f"price: {data['items'][item]['price']}\n")
            parsed_file.write(f"category: {data['items'][item]['category']}\n")
            parsed_file.write(f"sku: {data['items'][item]['sku']}\n")
            parsed_file.write(f"url: {data['items'][item]['url']}\n")
            parsed_file.write(f"yandex, name: {data['items'][item]['yandex, name']}\n")
            parsed_file.write(f"yandex, price: {data['items'][item]['yandex, price']}\n")
            parsed_file.write(f"yandex, url: {data['items'][item]['yandex, url']}\n")
            parsed_file.write(f"sima-land, price: {data['items'][item]['sima-land, price']}\n")
            parsed_file.write(f"sima-land, updated: {data['items'][item]['sima-land, updated']}\n")
            parsed_file.write(f"other, name: {data['items'][item]['other, name']}\n")
            parsed_file.write(f"other, price: {data['items'][item]['other, price']}\n")
            parsed_file.write(f"other, url: {data['items'][item]['other, url']}\n")
            parsed_file.write(f"updated: {data['items'][item]['updated']}\n")
            parsed_file.write("\n")
            count += 1
        else:
            break
    parsed_file.write(str(item) + '\n')
print('Информация о первых 100 товарах была успешно сохранена в файл parsed_100.txt!')
