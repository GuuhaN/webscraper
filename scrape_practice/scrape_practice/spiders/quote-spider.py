import scrapy

class Quote(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class QuoteSpider(scrapy.Spider):

    name = "quotescraper"
    start_urls = ["http://quotes.toscrape.com"]
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'quotes.json'
    }


    def parse(self, response):
        
        for quote in response.xpath("//div[@class='quote']"):
            newQuote = Quote()
            tags = []

            newQuote['quote'] = quote.xpath("span[@class='text']/text()").extract_first()
            newQuote['author'] = quote.xpath("span/small[@class='author']/text()").extract_first()
            # print("\033[93m" + quote.xpath("span[@class='text']/text()").extract_first() + "\033[0m")
            # print("\033[91m" + quote.xpath("span/small[@class='author']/text()").extract_first() + "\033[0m")
            for tag in quote.xpath("div[@class='tags']/a[@class='tag']"):
                tags.append(tag.xpath("text()").extract_first())
                # print("\033[92m" + tag.xpath("text()").extract_first() + "\033[0m")

            newQuote['tags'] = tags
            yield newQuote
        

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if(next_page):
            yield response.follow(next_page, callback=self.parse)

        
        # yield {
        #     'quote': response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first(),
        #     'tags': response.xpath("//div[@class='quote']/span[@class='tags']/a[@class='tag']/text()").extract(),
        # }
