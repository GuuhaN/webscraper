import scrapy
import time

class BolProduct(scrapy.Item):
    productname = scrapy.Field()
    brand = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    reviewcount = scrapy.Field()
    visible_description = scrapy.Field()

class ProductInfo(scrapy.Spider):
    name = "productinfo"

    def __init__(self, pages='', reviewcount='', start_url='', *args, **kwargs):
        super(ProductInfo, self).__init__(*args, **kwargs)
        try:
            # self.pages = int(input("Hoeveel pagina's wilt u scrapen? "))
            self.pages = int(pages)
            self.start_url = start_url
        except ValueError:
            self.pages = 1
            self.start_url = 'https://www.bol.com/nl/l/fietsen-accessoires/N/15670/?view=list'

        if(reviewcount == ''):
            reviewcount = 5

        self.reviewCriteria = int(reviewcount)
        # self.start_url = start_url if start_url == 'None' else "https://www.bol.com/nl/l/fietsen-accessoires/N/15670/?view=list"
        self.pageCount = 0

    def start_requests(self):
        yield scrapy.Request(self.start_url)

    def parse(self, response):
        if(self.pageCount < self.pages):
            start = time.time()
            next_page = response.xpath("//div[@id='js_pagination_control']/ul/li[@class='[ pagination__controls pagination__controls--next ]']/a/@href").extract_first()
            for productContent in response.xpath("//li[@class='product-item--row js_item_root ']/div[@class='product-item__content']"):
                # print(productContent.xpath("wsp-buy-block/div/section/div/div/span[@class='promo-price']/text()").re(r'(\w+)')[0] + "." + productContent.xpath("wsp-buy-block/div/section/div/div/span[@class='promo-price']/sup/text()").re(r'(\w+)')[0] if len(productContent.xpath("wsp-buy-block/div/section/div/div/span[@class='promo-price']/text()").re(r'(\w+)')) > 0 & len(productContent.xpath("wsp-buy-block/div/section/div/div/span[@class='promo-price']/sup/text()").re(r'(\w+)')) > 0 else "GEEN PRIJS")
                # # print(productContent.xpath("wsp-buy-block/div/section/div/div/span[@class='promo-price']/sup/text()").re(r'(\w+)')[0])
                product = BolProduct()
                product['productname'] = productContent.xpath("div/div[1]/a/text()").extract_first()
                product['brand'] = productContent.xpath("div/ul[1]/li/a/text()").extract_first()
                product['tags'] = productContent.xpath("div/ul[2]/li/span/text()").extract_first()
                product['price'] = '19.99'
                product['rating'] = float(productContent.xpath("div['star-rating']/div/div/@title").re(r': (\w+).(\w+)')[0] + "." + productContent.xpath("div['star-rating']/div/div/@title").re(r': (\w+).(\w+)')[1]) if len(productContent.xpath("div['star-rating']/div/div/@title").re(r': (\w+)')) > 0 else 0
                product['reviewcount'] = productContent.xpath("div['star-rating']/div/div/@data-count").extract_first() if product['rating'] > 0 else 0
                product['visible_description'] = productContent.xpath("div/p/text()").extract_first().strip() if productContent.xpath("div/p/text()").extract_first() else ''
                if(product['rating'] <= self.reviewCriteria):
                    yield product
            
            end = time.time()

            if(next_page):
                self.pageCount += 1
                yield response.follow(next_page, callback=self.parse)      

            print("time elapsed", end - start)
        # print(response.xpath("//li[@class='product-item--row js_item_root ']/div[@class='product-item__content']/div/ul[1]/li/a/text()").extract())
        # print(response.xpath("//li[@class='product-item--row js_item_root ']/div[@class='product-item__content']/div/div[1]/a/text()").extract())
        # print(response.xpath("//li[@class='product-item--row js_item_root ']/div[@class='product-item__content']/div/ul[2]/li/span/text()").extract())
        # print(response.xpath("//li[@class='product-item--row js_item_root ']/div[@class='product-item__content']/div/div[2]/div/@title").re(r': (\w+)'))
        # print(response.xpath("//li[@class='product-item--row js_item_root ']/div[@class='product-item__content']/div/p/text()").extract())
1