import  scrapy

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
        for item in response.xpath("//div[@class='story']"):
            yield {
                'name': item.xpath(".//h4[@class='story__heading']/a/@title").extract_first(),
                'source': item.xpath(".//div[@class='story__meta']/a[@class='source']").extract_first(),
                'relate': item.xpath(".//div[@class='story__meta']/a[@class='relate']").extract_first(),
                'time': item.xpath(".//div[@class='story__meta']/time[@class='time friendly']").extract_first(),
            }