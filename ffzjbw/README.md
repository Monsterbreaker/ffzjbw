环境：需安装redis数据库

包：scrapy-redis……

运行：进入项目根文件

    python3 init.py
    scrapy crawl ffzjbwSpider

写入数据库在/ffzjbw/ffzjbw/pipelines.py

写入两张表，一张是有关的，一张是无关的，根据item['isrelated']判断True是有关的