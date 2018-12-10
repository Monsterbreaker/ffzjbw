# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class FfzjbwPipeline(object):
    def process_item(self, item, spider):
        self.insert(item)
        return item

    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "12345678", "ffzjbw1", charset='utf8')
        self.cursor = self.db.cursor()
        self.insertion1 = "insert into related values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.insertion2 = "insert into unrelated values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def insert(self, item):
        if (item['isrelated']):
            try:
                self.cursor.execute(
                    self.insertion1,
                    [item['oriUrl'],
                     item['host'],
                     item['charSet'],
                     item['lastModified'],
                     item['contentType'],
                     item['keywords'],
                     item['description'],
                     item['title'],
                     item['weight']])
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print("发生异常",e)
            return
        else:
            try:
                self.cursor.execute(
                    self.insertion2,
                    [item['oriUrl'],
                     item['host'],
                     item['charSet'],
                     item['lastModified'],
                     item['contentType'],
                     item['keywords'],
                     item['description'],
                     item['title'],
                     item['weight']])
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                print("发生异常",e)
            return
