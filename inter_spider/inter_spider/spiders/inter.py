import scrapy

class InterMatches(scrapy.Spider):
    name = "inter"

    def start_requests(self):
        # define url to crawl
        urls = [
            'http://www.internacional.com.br/conteudo?modulo=3&setor=62'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
