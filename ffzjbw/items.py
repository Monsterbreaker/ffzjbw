# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FfzjbwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    oriUrl = scrapy.Field()  # 页面URL
    host = scrapy.Field()  # 域名

    charSet = scrapy.Field()  # 编码格式
    fileSize = scrapy.Field()  # content-length 感觉可能没用？？
    lastModified = scrapy.Field()  # 最后修改时间，老师的要求
    contentType = scrapy.Field()  # 媒体类型格式

    keywords = scrapy.Field()  # 关键词，用于计算页面权值
    description = scrapy.Field()  # 描述，用于计算页面权值
    title = scrapy.Field()  # 标题，用于计算页面权值
    author = scrapy.Field()  # 作者，感觉可能没用？？

    urls = scrapy.Field()  # 所有跳转URL
    weight=scrapy.Field()
    pass
