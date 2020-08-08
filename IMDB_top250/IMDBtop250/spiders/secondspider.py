# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:14:54 2020
@author: Dhruv Sharma
"""

import scrapy
from Example.items import movieitem
 
class secondspider(scrapy.Spider):
    name = "secondspider"
    
    allowed_domains = ["imdb.com"]
    start_urls = (
        "http://www.imdb.com/chart/top" ,)
        
        
    
    
    def parse(self , response):
        links = response.xpath("//div[@class = 'lister']/table/tbody/tr/td[2]/a/@href").extract()
        i = 1
        self.log("entering into loop")
        for link in links:
            abs_url = response.urljoin(link)
            url_next = "//div[@class = 'lister']/table/tbody/tr[1]/td[3]/strong/text()"
            rating = response.xpath(url_next).extract()
            if (i <= len(links)):
                i += 1
                yield scrapy.Request(abs_url , callback = self.init_parse , meta = {'rating' : rating})
            self.log("entered into loop")
                
    def init_parse(self , response):
        item =  movieitem()
        item['title'] = response.xpath("//div[@class = 'title_bar_wrapper']/div[2]/div[2]/h1/text()").extract()
        item['year'] = response.xpath("//div[@class = 'title_bar_wrapper']/div[2]/div[2]/h1/span/a/text()").extract()
        item['director'] = response.xpath("//div[@class = 'plot_summary ']/div[2]/a/text()").extract()
        item['writers'] = response.xpath("//div[@class = 'plot_summary ']/div[3]/a/text()").extract()
        item['stars'] = response.xpath("//div[@class = 'plot_summary ']/div[4]/a/text()").extract()
            
        return(item)