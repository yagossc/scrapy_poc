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

    # Parse the championship links in the given page
    def parse_championship_links(self, response):
        # The championships' links share the same base xpath
        championships_xpath = '/html/body/section/div/div[1]/div/p'

        # Allocate variable for championships' links
        championship_links = []

        # Iterate over the <p> elements and get the championship links
        for p in response.xpath(championships_xpath):
            next_link = p.xpath('./a/@href').get()
            championship_links.append(response.urljoin(next_link))

        # Iterate/crawl each championship link
        for championship_link in championship_links:
            yield scrapy.Request(url=championship_link, callback=self.crawl_championships)

    # Crawl/Fetch the game results (if available)
    def crawl_championships(self, response):
        print(response)
