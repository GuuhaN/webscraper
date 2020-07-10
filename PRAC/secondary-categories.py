import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

i = 0

class BolCategory(scrapy.Item):
    base_category = scrapy.Field()
    url = scrapy.Field()

class ScrapeBaseCategories(scrapy.Spider):

    name = 'treecategory'

    def parse(self, response):
        global i
        next_cat = response.xpath("//div[@class='facet-control__filter facet-control__filter--no-padding']/a/@href").getall()
        process = CrawlerProcess(get_project_settings())
        test_cat = next_cat[20]
        process.crawl("categoryscraper", start_urls=[response.urljoin(test_cat)])
        # for cat in next_cat:
        #     process.crawl("CategoryScraper", start_urls=[response.urljoin(cat)])

        process.start()

    def scrapyCategories(self, url):
        process = CrawlerProcess(get_project_settings())
        process.crawl("categoryscraper")
        process.start()