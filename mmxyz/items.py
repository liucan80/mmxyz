# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmxyzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    pageLink=scrapy.Field()
    viewsNum=scrapy.Field()
    commentsNum=scrapy.Field()
    likesNum=scrapy.Field()
    fileName = scrapy.Field()  # 文件夹名，每一个MM一个文件夹
    path = scrapy.Field()  # 图片存储路径（绝对路径）
    pageURL = scrapy.Field()  # 每一张图片入口URL
    detailURL = scrapy.Field()  # 图片原图地址
    image=scrapy.Field
    pass
