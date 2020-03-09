import scrapy

# read teams list from file
def read_list(file_name):
    f = open(file_name)
    teams = [team.strip() for team in f.readlines()]
    f.close()
    return teams

def gen_csv_entry(entry):
    csv_entry = []
    for item in entry:
        csv_entry.append(item)
        csv_entry.append(",")

    # pop unwanted ,
    csv_entry.pop()
    csv_entry.append("\n")
    csv_string = ''.join(csv_entry)
    return csv_string

# Target teams array
global target_teams
target_teams = []

class InterMatches(scrapy.Spider):
    name = "inter"

    def start_requests(self):
        # define url to crawl
        urls = [
            'http://www.internacional.com.br/conteudo?modulo=3&setor=62'
        ]

        # this crawler requires a list of teams as input
        try:
            file_name = self.teams_list
        except:
            raise Exception("No teams list provided")
            exit(1)

        # set the teams list
        global target_teams
        target_teams = read_list(file_name)

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

        # Create file to store results
        f = open('tmp_output.csv', 'a+')
        for game in game_results:
            for team in target_teams:
                if game[0] == team or game[2] == team:
                    csv_entry = gen_csv_entry(game)
                    try:
                        f.write(csv_entry)
                    except:
                        raise Exception("Could not write to file")
        f.close()
