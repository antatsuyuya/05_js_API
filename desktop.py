import scrapy
import logging

class DesktopSpider(scrapy.Spider):
    name = 'desktop'
    allowed_domains = ['xn--kck6a0a828yuit.com']
    start_urls = ['https://xn--kck6a0a828yuit.com/odds/20220108nakayama/']

    def parse(self, response):
        # logging.info(response.url)
        products=response.xpath('//div[contains(@class, "post_content clearfix")]')
        
        for product in products:
            name = product.xpath('.//td[@class=""]/text()').get()
            odds = product.xpath('.//td[@class="align2"]/text()').get()
            name2 = product.xpath('.//td[@class="kisu"]/text()').get()
            odds2 = product.xpath('.//td[@class="align2 kisu"]/text()').get()

            yield{
            "name":name,
            "odds":odds,
            "name2":name2,
            "odds2":odds2,
            }

        # next_page=response.xpath('//td/a/@href').get()
        # if next_page:
        #     yield response.follow(url=next_page,callback=self.parse)

