# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseImageItem

class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'
    #allowed_domains = ['shiyanlou.com/courses']
    start_urls = ['http://shiyanlou.com/courses/']

    def parse(self, response):
        item = CourseImageItem()
        item['image_urls'] = response.xpath('//img[@class="cover-image"]/@src').extract()
        yield item
