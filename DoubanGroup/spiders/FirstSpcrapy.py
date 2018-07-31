__author__ = 'WanyeXie'

import scrapy
from DoubanGroup.items import ScrapytestItem
import win_unicode_console
win_unicode_console.enable()

class firstSpider(scrapy.spiders.Spider):
    name = "firstSpider"
    #允许的域名
    allow_domains = ["www.douban.com"]
    #入口url
    start_urls = ["https://www.douban.com/group/106955/"]

    def parse(self, response):
        tbody = response.xpath("//div[@class='article']//div[@id='group-topics']/div[2]/table[@class='olt']")
        print(tbody)
        for tr in tbody.xpath(".//tr"):

            item = ScrapytestItem()
            item['title'] = tr.xpath('.//td[1]/a/text()').extract()    #文章标题
            item['url'] = tr.xpath('.//td[1]/a/@href').extract()  #文章地址
            item['lastDate'] = tr.xpath('.//td[last()]/text()').extract()  #文章最后更新时间
            yield item
