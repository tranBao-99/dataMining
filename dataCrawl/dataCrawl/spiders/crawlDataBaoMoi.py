import  scrapy
from dataCrawl.items import DatacrawlItem
from scrapy.loader import ItemLoader

class crawling(scrapy.Spider):
    name = 'test'
    start_urls = [
        'https://baomoi.com/nang-luong-tich-cuc/top/338.epi',
        'https://baomoi.com/kham-pha-viet-nam/top/335.epi',
        'https://baomoi.com/phong-chong-covid-19/top/328.epi',
        'https://baomoi.com/hoc-bong-du-hoc.epi',
        'https://baomoi.com/lao-dong-viec-lam.epi',
        'https://baomoi.com/thiet-bi-phan-cung.epi',
    ]

    def parse(self, response):
        for items in response.xpath("//div[@class='story']"):
            l = ItemLoader(item = DatacrawlItem, selector = items )
            l.add_xpath('name', ".//h4[@class='story__heading']/a/@title")
            l.add_xpath('source', ".//div[@class='story__meta']/a[@class='source']")
            l.add_xpath('relate', ".//div[@class='story__meta']/a[@class='relate']")
            l.add_xpath('time', ".//div[@class='story__meta']/time[@class='time friendly']")
            yield l.load_item()