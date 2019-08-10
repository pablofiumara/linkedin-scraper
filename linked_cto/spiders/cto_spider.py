import scrapy
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
        self.login(user, password)
        self.driver.get("https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%5D&keywords=Chief%20Transformation%20Officer&origin=FACETED_SEARCH")

    def start_requests(self):
        self.log("inside start_requests method")
        urls = []
	for page in xrange(1,101):
        	urls.append("https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%5D&keywords=Chief%20Transformation%20Officer&origin=FACETED_SEARCH&page="+str(page))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("inside parse method")
        url = response.url
        self.log("response url: " + url )
        self.driver.get(url)
        self.log("response request url: " + response.request.url)
        self.scroll_down()
        self.log("finished scrolling down")
        search_result = self.get_search_result_list()
    

    def login(self, user, password):
        self.log("starting login")
        self.driver.get("https://www.linkedin.com/login")

        self.driver.find_element_by_id("username").send_keys(user)
        self.driver.find_element_by_id("password").send_keys(password)

        self.driver.find_element_by_tag_name("button").click()

    def scroll_down(self):
        self.log("scrolling down")
        self.driver.find_element_by_tag_name('html').send_keys(Keys.END)


    def get_search_result_list(self):
       search_result = self.driver.find_element_by_class_name("search-results__list").find_elements_by_xpath(".//li")
       self.log(len(search_result))
       return search_result
