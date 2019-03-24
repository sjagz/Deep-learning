
import scrapy
from rt_crawler.items import RTItem

class RTSpider(scrapy.Spider):
    # 3개의 정해진 변수를 설정해야 해요!
    name = "My_First_Crawler"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = [
        "https://www.rottentomatoes.com/top/bestofrt/?year=2018"
    ]

    def parse(self, response):
        tr_list = response.xpath('//*[@id="top_movies_main"]/div/table/tr')

        for tr in tr_list:
            href = tr.xpath('./td[3]/a/@href').extract()[0]
            url = response.urljoin(href)
            # 화면에 찍는 대신에 Request를 보내야 해요!!
            # 해당 page로 이동하겠다는 의미
            yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        item = RTItem()
        item["title"] = \response.xpath('//*[@id="topSection"]/div[2]/div[1]/h1/text()').extract()[0]
        # item["score"] =
        yield item