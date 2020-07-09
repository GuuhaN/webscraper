import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pymongo
from pymongo import MongoClient
import json

myclient = MongoClient("mongodb+srv://test:test@helloworld-cluster-mongodb-jrnrm.azure.mongodb.net/bolscraper?retryWrites=true&w=majority")
mydb = myclient["bolscraper"]
mycol = mydb["categories"]

class BolCategory(scrapy.Item):
    base_category = scrapy.Field()
    base_url = scrapy.Field()
    sub_categories = scrapy.Field()

class SubCategory(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()

class CategoryScraper(scrapy.Spider):
    name = 'categoryscraper'
    # start_urls = ['https://www.bol.com/nl/l/alle-artikelen/']

    def __init__(self, url = None):
        self.url = url

    def start_requests(self):
        print(self.url)
        yield scrapy.Request(self.url)

    def parse(self, response):
        base_category = BolCategory()
        cats = []
        for category in response.xpath("//div[@class='facet-control__filter facet-control__filter--no-padding']/a"):
            subCategory = SubCategory()
            subCategory['category'] = category.xpath("text()").extract_first().strip()
            subCategory['url'] = response.urljoin(category.xpath('@href').extract_first())
            cats.append(subCategory)
        
        base_category['base_category'] = response.xpath("//h1[@class='h1 bol_header']/text()").extract_first()
        base_category['base_url'] = response.url
        base_category['sub_categories'] = cats

        yield base_category
    
