from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from subjectcrawler.items import SubjectItem

class SubjectSpider(BaseSpider):
    name = "subject"
    allowed_domains = ["gla.ac.uk"]
    start_urls = [
        "http://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30200000&name=School+of+Computing+Science"
    ]

    def parse(self, response):
        sel = Selector(response)
        main = sel.xpath("//div[@class='maincontent']")
       	subjects = []
        for p in main.xpath(".//a"):
            item = SubjectItem()
            item['visitingStudents'] = []
            try:
                item['link'] = p.xpath("@href").extract()
            except Exception, e:
                raise e
                item['link'] = []
            item['name'] = p.xpath("text()").extract()
            print item['name']
            subjects.append(item)
       	return subjects
        # "http://www.gla.ac.uk" + 