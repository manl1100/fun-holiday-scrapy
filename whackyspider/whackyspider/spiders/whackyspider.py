from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import WhackyHolidayItem

class HolidaySpider(Spider):

    name = "holidayspider"
    allowed_domains = ["http://www.timeanddate.com/"]
    start_urls = ["http://www.timeanddate.com/holidays/fun/"]

    def parse(self, response):
        sel = Selector(response)
        rows = sel.xpath('//div[@class="main-content-div"]/article/section[@class="article eight columns"]//tbody//tr')
        items = []

        for row in rows:
            item = WhackyHolidayItem()
            item['date'] = ''.join(row.xpath('./th/text()').extract())
            item['day'] = ''.join(row.xpath('./td/text()').extract())
            item['holiday'] = ''.join(row.xpath('./td/a/text()').extract())
            items.append(item)

        return items
