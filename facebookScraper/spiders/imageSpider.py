import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from facebookScraper.items import ImageItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    start_urls = ['https://www.facebook.com/pg/SystemanalystUzhnu/photos/?ref=page_internal']
    # default_headers = {
    #     "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "accept-language":"uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6",
    # }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url = self.start_urls[0],
                callback = self.parse,
                wait_time=20,
            )

    def parse(self, response):
        all_photos = response.xpath('//body/div/div[3]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div')
        for photo in all_photos:
            img = ImageItem()
            img["image"] = photo.xpath('a/img/@src').get()
            yield img

