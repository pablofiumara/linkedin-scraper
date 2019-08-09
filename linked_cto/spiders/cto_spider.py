import scrapy


class CTOSpider(scrapy.Spider):
    name = "cto"

    def start_requests(self):
        urls = []
	for page in xrange(1,101):
        	urls.append("https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%5D&keywords=Chief%20Transformation%20Officer&origin=FACETED_SEARCH&page="+str(page))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
	self.log(response.url)
