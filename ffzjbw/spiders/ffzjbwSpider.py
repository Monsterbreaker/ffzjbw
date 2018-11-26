# -*- coding: utf-8 -*-
import scrapy
import re
from ffzjbw.items import FfzjbwItem
from urllib import parse
from ffzjbw.scrapy_redis.spiders import RedisSpider


class FfzjbwspiderSpider(RedisSpider):
    name = 'ffzjbwSpider'
    redis_key = 'ffzjbwSpider:start_urls'
    #allowed_domains = ['com', 'net', 'biz', 'info', 'edu', 'org', 'eu', 'cn', 'gov']
    count1 = 0
    count2 = 0
    curHost = ""

    # start_urls = ['http://www.qukuailianh.com']

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        # domain = kwargs.pop('domain', '')
        # self.allowed_domains = filter(None, domain.split(','))

        # 修改这里的类名为当前类名
        super(FfzjbwspiderSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = FfzjbwItem()

        # 拿header信息
        item["oriUrl"] = response.url
        item["host"] = parse.urlparse(response.url).netloc

        item["charSet"] = response.headers.encoding
        item["contentType"] = response.headers["Content-Type"].decode(item["charSet"]).split(";")[0]
        if 'Last-Modified' in response.headers:
            item["lastModified"] = response.headers["Last-Modified"].decode(item["charSet"])
        else:
            item["lastModified"] = ''

        # 拿body信息
        keywords = response.xpath("head/meta[@name='keywords']/@content")
        if keywords:
            item["keywords"] = keywords.extract_first()  # .split(",")
        else:
            item["keywords"] = ''

        description = response.xpath("head/meta[@name='description']/@content")
        if description:
            item["description"] = description.extract_first()
        else:
            item["description"] = ''
        item["title"] = response.xpath("//title/text()").extract_first()

        self.calWeight(item)
        urlslist = []
        if self.useStrategy1(item) and self.useStrategy2(item):
            # 拿URL
            urls = response.xpath("//a/@href").extract()
            for url in urls:
                u = re.search(("(http|https):.+"), url)
                if u and self.isHtml(u[0]):
                    urlslist.append(u[0])
        yield item
        for url in urlslist:
            yield scrapy.Request(url, callback=self.parse)
        pass

    def calWeight(self, item):
        weight = 0
        if self.MatchOne(item["keywords"]):
            weight = weight + 5
        if self.MatchOne(item["title"]):
            weight = weight + 3
        if self.MatchOne(item["description"]):
            weight = weight + 2
        item["weight"] = weight

    def MatchOne(self, keywords):
        if keywords:
            result = re.search("(区块链)|(block chain)|(Block Chain)|(blockchain)|(BlockChain)", keywords)
            if result:
                return True
        return False

    def useStrategy1(self, item):
        if item["weight"] > 5:
            self.count1=0
        self.count1=self.count1+1
        if self.count1>=3 and item["weight"]<6:
            return False
        else:
            return True

    def useStrategy2(self, item):
        if self.curHost != item["host"]:
            self.count2 = 0
            self.curHost = item["host"]
        self.count2 = self.count2 + 1
        if self.count2 > 100 and item["weight"] < 8:
            return False
        return True

    def isHtml(self,url):
        suffix = [".jpg", ".png", "/"]
        for one in suffix:
            if url.endswith(one):
                return False
        if re.search("(login)|(forum.php)|(home.php)",url):
            return False
        return True