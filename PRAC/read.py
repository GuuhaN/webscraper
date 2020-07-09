import json

with open('bol_categories.json') as json_file:
    data = json.load(json_file)
    for sub_cat in data:
        for url in sub_cat['sub_categories']:
          print(url)