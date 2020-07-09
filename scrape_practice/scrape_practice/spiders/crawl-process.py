import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class CrawlStarter(scrapy.Spider):
    process = CrawlerProcess(get_project_settings())

    def scrapeUrl(url):
        process.crawl("bookscrape")
        process.crawl("quotescraper")
        process.start()
    