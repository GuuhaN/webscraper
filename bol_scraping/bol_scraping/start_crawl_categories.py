import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
# with open('bol_categories.json') as json_file:
#     data = json.load(json_file)
#     for sub_cat in data:
#         for url in sub_cat['sub_categories']:
#             process.crawl("categoryscraper", url=url['url'])

# process.crawl("categoryscraper", url='https://www.bol.com/nl/l/klusspullen/N/13155/')
process.crawl("productinfo", url='https://www.bol.com/nl/l/videogames/N/18200/', reviewCount=5)
process.start()