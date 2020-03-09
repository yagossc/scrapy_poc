import scrapy

class InterMatches(scrapy.Spider):
    name = "inter"

    def start_requests(self):
        # define url to crawl
        urls = [
            'http://www.internacional.com.br/conteudo?modulo=3&setor=62'
        ]

        # make a request for each url
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_championship_links)

    def parse_championship_links(self, response):
        championships_xpath = '/html/body/section/div/div[1]/div/p'

        championship_links = []

        for p in response.xpath(championships_xpath):
            next_link = p.xpath('./a/@href').get()
            championship_links.append(response.urljoin(next_link))

        print(championship_links)
