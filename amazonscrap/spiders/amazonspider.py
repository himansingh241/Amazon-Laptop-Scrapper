# -*- coding: utf-8 -*-
import scrapy
from .. items import AmazonscrapItem

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    page_number = 2
    start_urls = ['https://www.amazon.in/s?k=laptops']

    def parse(self, response):
        items = AmazonscrapItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_price = response.css('.a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.in/s?k=laptops&page=' + str(AmazonspiderSpider.page_number)
        if AmazonspiderSpider.page_number <= 20:
            AmazonspiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
