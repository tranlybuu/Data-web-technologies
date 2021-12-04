# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebtechsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field()
    NameTechnology = scrapy.Field()
    Websites = scrapy.Field()
    P1month = scrapy.Field()
    UniqueDomains = scrapy.Field()
    TechCategory = scrapy.Field()
