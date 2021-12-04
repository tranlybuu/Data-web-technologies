import scrapy
from ..items import WebtechsItem
from scrapy_selenium import SeleniumRequest
import os
from selenium import webdriver
from scrapy.utils.project import get_project_settings

class WebBotSpider(scrapy.Spider):
    name = 'web_bott'
    
    def start_requests(self):
        list_url = [
            'https://www.similartech.com/categories/',
        ]
        for item in list_url:
            yield SeleniumRequest(
                url = item,
                wait_time = 3,
                callback = self.parse,
            )
    def parse(self, response):
        settings= get_project_settings()
        driver_path = 'E:\Data-web-technologies\chromedriver.exe'
        options= webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get("https://www.similartech.com/categories/")
        link_elements = driver.find_elements_by_xpath('//*[@class="table-list"]//a/text()')
        driver.quit()
        Date = link_elements
        item = WebtechsItem()
        item["Date"] = Date
        yield item