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
        game_results = []
        matches = response.xpath('//a[@data-reveal-id]')

        for match in matches:
            matchup_list = match.xpath('./ul/li')
            game_text = []
            for matchup_info in matchup_list:
                team_name = matchup_info.xpath('./strong/text()').get()
                if team_name != None:
                    game_text.append(team_name)
                result = matchup_info.xpath('./span/text()').get()
                if result != None:
                    game_text.append(result)
            if len(game_text) == 4:
                game_results.append(game_text)
        print(game_results)
