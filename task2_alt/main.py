#-*-encoding: utf-8 -*-
import wikipediaapi
import pymorphy2
import locale
from functools import cmp_to_key

wiki = wikipediaapi.Wikipedia('ru')
cat = wiki.page("Категория:Животные по алфавиту")
animals = []
morph = pymorphy2.MorphAnalyzer()
for page in cat.categorymembers.values():
    if "Категория:" not in page.title and "(род)" not in page.title:
        for word in page.title.split():
            if '(' not in word:
                tag = morph.parse(word)[0].tag
                if "NOUN" in tag and "plur" not in tag and word.capitalize() not in animals:
                    animals.append(word.capitalize())
dict_letters = {}
for animal in animals:
    if animal[:1] in dict_letters:
        dict_letters[animal[:1]] += 1
    else:
        dict_letters[animal[:1]] = 1
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
for key in sorted(dict_letters, key = cmp_to_key(locale.strcoll)):
    print(f"{key}: {dict_letters[key]}")


