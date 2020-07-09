from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib.request
import scrapy


# baseUrl = 'https://www.bol.com'
# source = urllib.request.urlopen(baseUrl).read()
# soup = BeautifulSoup(source, 'lxml')

# Change value parameter in a html tag
# soup.find('input')["value"] = 100
# print(soup.find('input'))

# Get all head categories on a site bol.com
#final_results = []

#for tmp in soup.findAll('a', {'class': 'wsp-category-nav__link js_cat_link'}):
#    final_results.append(baseUrl + tmp['href'])

#print(final_results)

#customUrl = 'https://www.bol.com/nl/l/decoratieve-accessoires/N/35450/'
#customSource = urllib.request.urlopen(customUrl)
#soup2 = BeautifulSoup(customSource, 'html5lib')

##products = soup2.findAll('div', {'class': 'product-item__image'}, 'data-test')
#sponsoredProducts = soup2.findAll('div', text='Gesponsord')
#productRatings = soup2.findAll('div', {'class': 'star-rating',}, 'title')

#print(len(products))
#print(sponsoredProducts[0])
#print(len(productRatings))

class BlogSpider(scrapy.Spider):
    name = "brickset_spider" #Naam voor de specifieke web "spider"
    start_urls = ['https://www.bol.com/nl/l/decoratieve-accessoires/N/35450/'] #URLs die gebruikt worden binnen deze spider

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }