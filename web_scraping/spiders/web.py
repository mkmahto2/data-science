import scrapy


class WebSpider(scrapy.Spider):
    name = 'web'
    allowed_domains = ['pythonscaping.com']
    start_urls = ['http://pythonscaping.com/']

    def parse(self, response):
        pass
