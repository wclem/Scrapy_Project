import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape_xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            #print(quote.get())
            yield {
                'text': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//small[@class='author']/text()").get(),
                'tags': quote.xpath(".//a[@class='tag']/text()").getall(),
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


# scrapy shell 'http://quotes.toscrape.com/page/1/'
# bb = response.xpath('//div[@class="quote"]/span[@class="text"]/text()')

# bb[0].get()
# Out[21]: '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'