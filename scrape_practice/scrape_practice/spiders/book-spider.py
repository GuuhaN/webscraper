import scrapy

i = 0
page_num = 1

class BookScrape(scrapy.Spider):
    name = 'bookscrape'
    start_urls = [
        'http://books.toscrape.com/'
    ]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'books.json'
    }
    
    def __init__(self, name=None, pages=None, *args, **kwargs):
        super(BookScrape, self).__init__(name, **kwargs) # <- important
        self.pages = pages
        print(pages)

    def parse(self, response):
        # for category in response.xpath("//div[@class='side_categories']/ul/li/ul/li/a"):
        #     yield {
        #         'Category': category.xpath("text()").extract_first().strip(),
        #         'Link': category.xpath("@href").extract_first().strip()
        #     }
        
        global i
        global page_num

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        page_number = response.xpath("//li[@class='current']/text()")
        print("PAGE NUMBER" + page_number.re(r'Page (\w+) of')[0])
        if(page_number):
            yield {
                'category': response.xpath("//div[@class='page-header action']/h1/text()").extract_first(),
                'page':  page_number.re(r'Page (\w+) of')[0],
                'books': response.xpath("//article[@class='product_pod']/h3/a/text()").extract()
            }
        else:
            yield {
                'category': response.xpath("//div[@class='page-header action']/h1/text()").extract_first(),
                'page':  '1',
                'books': response.xpath("//article[@class='product_pod']/h3/a/text()").extract()
            }

        # if(next_page):
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, self.parse)
        # else:
        #     next_cat = response.xpath("//div[@class='side_categories']/ul/li/ul/li/a/@href")[i].extract().strip()
        #     next_cat = response.urljoin(next_cat)
        #     yield scrapy.Request(next_cat, self.parse)
        #     i += 1

        # for category in response.xpath("//div[@class='side_categories']/ul/li/ul/li/a"):
        #     next_cat = self.start_urls[0] + category.xpath("@href").extract_first().strip()
        #     while(next_page):
        #         yield scrapy.Request(next_page, self.parse_books)
        #     if(next_cat):
        #         yield scrapy.Request(next_cat, self.parse_books)

