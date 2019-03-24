import scrapy


# 영화정보에 대한 class 정의
class RTItem(scrapy.Item):
    title = scrapy.Field()
    # score = scrapy.Field()
