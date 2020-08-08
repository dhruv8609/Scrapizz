# -*- coding: utf-8 -*-
"""
Created on Wed May 20 00:02:44 2020

@author: Dhruv Sharma
"""

import scrapy

# generating the first simple spider web crawler
class firstspider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
            ]
        for url in urls:
            yield scrapy.Request(url = url , callback = self.parse)
    
    def parse(self , response):
        page = response.url.split("/")[-2]
        filename = 'quotes' + str(page) + '.html' 
        with open(filename , 'wb') as f:
            f.write(response.body)
        self.log("saved file -" , filename)
        
    
            
        
    
    