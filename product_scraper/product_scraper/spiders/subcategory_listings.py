import scrapy


class SubcategorySpider(scrapy.Spider):
    name = 'subcategory_listings'
    start_urls = ['https://www.luluhypermarket.com/en-ae/electronics']

    def parse(self, response):
        base_url = "https://www.luluhypermarket.com"

        subcategories = response.css('div.col-lg-2.col-md-2.col-auto')  # getting all the subcategories section

        for subcategory in subcategories:

            yield {
                "subcategory": subcategory.css("div.col-lg-2.col-md-2.col-auto .img-caption::text").get(),
                "url": base_url + subcategory.css("div.col-lg-2.col-md-2.col-auto a::attr(href)").get()
            }




