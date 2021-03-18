#-*-encoding: utf-8 -*-
import wikipediaapi

wiki = wikipediaapi.Wikipedia('ru')
cat = wiki.page("Категория:Животные по алфавиту")
dict_letters = {}
for page in cat.categorymembers.values():
    if "Категория:" not in page.title:
        if page.title[:1] not in dict_letters.keys():
            dict_letters[page.title[:1]] = 1
        else:
            dict_letters[page.title[:1]] += 1
for key in sorted(dict_letters):
    print(f"{key}: {dict_letters[key]}")
