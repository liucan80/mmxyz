# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
from scrapy.pipelines.images import ImagesPipeline


class MmxyzPipeline(object):
    def open_spider(self,spider):
        self.file=open("item.json",'w')
    def close_spider(self,spider):
        self.file.close()    
    def process_item(self, item, spider):
        if not os.path.exists(item['folderName']):
            os.makedirs(item['folderName'])
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
# class ImagePipeline(ImagesPipeline):
#     def process_item(self,item,spider):
#         pass
#     pass