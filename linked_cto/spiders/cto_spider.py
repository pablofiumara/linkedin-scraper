import scrapy
from selenium import webdriver

'''

run with

scrapy crawl cto -a user=test -a password=123

'''


class CTOSpider(scrapy.Spider):
    name = "cto"

    def __init__(self, user,password):
        self.log("inside __init__ method")
        self.driver = webdriver.Chrome('/home/paf/Downloads/chromedriver')
        self.driver.fullscreen_window()

    def start_requests(self):
        self.log("inside start_requests method")
        urls = []
	for page in xrange(1,101):
        	urls.append("https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%5D&keywords=Chief%20Transformation%20Officer&origin=FACETED_SEARCH&page="+str(page))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("inside parse method")
	self.log(response.url)
