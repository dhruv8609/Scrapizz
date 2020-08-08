# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class movieitem(scrapy.Item):
    
    title = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
    writers  = scrapy.Field()
    popularity = scrapy.Field()
    year = scrapy.Field()
    
class superdatascience(scrapy.Item):
    text = scrapy.Field()
    lists = scrapy.Field()
    image = scrapy.Field()
    