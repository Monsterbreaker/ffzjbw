import redis
r=redis.Redis(host="localhost",port=6379,db=0)
key="ffzjbwSpider:start_urls"
urls=[
    #'https://www.baidu.com/s?ie=UTF-8&wd=%E5%8C%BA%E5%9D%97%E9%93%BE',
    'https://www.8btc.com',
    'https://www.cnblogs.com/zhuweiheng/p/8206188.html',
    'http://www.nteweixiu.com',
    'http://www.lianzhidao.com',
    'http://www.chinaz.com/blockchain/2018/0828/930357.shtml',
    'http://lianask.26595.com',
    'https://www.chainfor.com',
    'http://www.qukuailianh.com',
]
for url in urls:
    r.rpush(key,url)