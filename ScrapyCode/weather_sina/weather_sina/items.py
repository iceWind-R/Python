# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherSinaItem(scrapy.Item):
    city = scrapy.Field()
    date = scrapy.Field()
    dayDesc = scrapy.Field()
    dayTemp = scrapy.Field()