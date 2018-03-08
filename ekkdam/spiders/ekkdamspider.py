# -*- coding: utf-8 -*-
import scrapy
import PIL
from PIL import Image
from scrapy import Selector
from scrapy.http import Request

next_page_urls = ["https://dei.com.sg/drinks-and-snacks-page-{}.html".format(i) for i in range(1, 15)]

class EkkdamspiderSpider(scrapy.Spider):
    
    name = 'ekkdamspider'
    allowed_domains = ['dei.com.sg/drinks-and-snacks.html']
    start_urls = ['http://dei.com.sg/drinks-and-snacks.html/']

    def start_requests(self):
		for url in next_page_urls:
			yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        titles = response.css('.product-title::attr(title)').extract()
        price_with_symbol = response.xpath('.//*[@class="ty-price-num"]/text()').extract()
        price = price_with_symbol[1::2]
        images = response.css('img::attr(data-src)').extract()

        for product in zip(titles,price,images):
            scraped_info = {
                'title' : product[0],
                'price' : product[1],
                'images' : product[2]
            }

           
            yield scraped_info
