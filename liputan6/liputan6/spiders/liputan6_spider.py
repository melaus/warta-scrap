import scrapy
from scrapy.selector import Selector
from liputan6.items import Liputan6Item


class RepublikaSpider(scrapy.Spider):
    name = "liputan6"
    allowed_domains = ["liputan6.com"]
    start_urls = [
        "http://www.liputan6.com/indeks",
    ]

    def parse(self, response):
        """ This function parses a property page.

        @url http://www.liputan6.com/indeks
        @returns items
        """

        indeks = Selector(response).xpath('//*[@id="indeks-articles"]/div[@class="articles--list articles--list_rows"]/article')

        for indek in indeks:
            item = Liputan6Item()
            item['title'] = indek.xpath('aside/header/h4/a/@title').extract()[0].strip()
            item['link'] = indek.xpath('aside/header/h4/a/@href').extract()[0].strip()
            item['images'] = ""
            item['category'] = indek.xpath('aside/header/a/text()').extract()[0].strip()
            item['date'] = indek.xpath('aside/header/span/time/@datetime').extract()[0].strip()
            item['desc'] = indek.xpath('aside/div/text()').extract()[0].strip()

            yield item
