import  scrapy
from ..items import QuotetutorialItem

class Quotespider(scrapy.Spider):

    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/'
    ]


    def parse(self,response):
        item = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')


        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            item['title'] = title
            item['author'] = author
            item['tag'] = tag

            yield item

        next_page = 'http://quotes.toscrape.com/page/'+str(Quotespider.page_number)+'/'
        #response.css('li.next a::attr(href)').get()
        #if next_page is not None:
        if  Quotespider.page_number<=10:
            Quotespider.page_number+=1
            yield response.follow(next_page, callback = self.parse)
