# -*- coding: utf-8 -*-
import copy

import requests
import scrapy

from mmxyz.items import MmxyzItem


class MmxyzspiderSpider(scrapy.Spider):
    name = 'mmxyzspider'
    allowed_domains = ['mmxyz.net']
    base = r'./mm/'
    pageNum=1
    page = "http://www.mmxyz.net/category/rosi-video/?action=ajax_post&cat=rosi-video&pag=%d"%pageNum
    start_urls = [
        page]

    def parse(self, response):
        item=MmxyzItem()
        divs = response.xpath('//div[@class="post-home"]')
        
        for div in divs:
            item['title'] = div.xpath("./div[1]/a/@title").extract_first()
            item['pageLink'] = div.xpath('./div[1]/a/@href').extract_first()
            item['viewsNum'] = div.xpath('./div[@class="post-info"]/div[@class="views"]/span[1]/text()').extract_first()
            item['commentsNum'] = div.xpath(
                './div[@class="post-info"]/div[@class="comments"]/span[1]/a/text()').extract_first()
            item['likesNum'] = div.xpath(
                './div[@class="post-info"]/div[@class="likes"]/span[1]/text()').extract_first()
            item['folderName'] = self.base + item['title']
            yield item
            yield scrapy.Request(url=item['pageLink'], meta={'item1': copy.deepcopy(item)}, callback=self.parse_Two)
           
            
        self.pageNum+=1
        nexturl="http://www.mmxyz.net/category/rosi-video/?action=ajax_post&cat=rosi-video&pag=%d"%self.pageNum
        if self.pageNum<=5:
            yield scrapy.Request(url=nexturl, callback=self.parse)
    def parse_Two(self,response):
        item2 = response.meta['item1']
        imglinks = response.xpath('//dl[@class="gallery-item"]')
        i=0
        for imglink in imglinks:
            i=i+1
            link=imglink.xpath('./dt/a/@href').extract_first()
            # yield scrapy.Request(link)
            image = requests.get(link)
            f = open(item2['folderName']+"/%d.jpg"%i,'wb')
            f.write(image.content)
            f.close()
        yield None
