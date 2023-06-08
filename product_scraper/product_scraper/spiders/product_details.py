import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'product_details'
    start_urls = ['https://www.luluhypermarket.com/en-ae/electronics']

    def parse(self, response):
        subcategories = response.css('div.col-lg-2.col-md-2.col-auto')  # getting all the subcategories
        all_subcategories_url = subcategories.css("div.col-lg-2.col-md-2.col-auto a::attr(href)").getall()  # getting all the subcategories url

        for product in all_subcategories_url:
            yield response.follow(product, callback=self.parse_products)

    def parse_products(self, response):
        products = response.css("div.row.product-listing-sectionfashion-products")  # getting all the items from products section
        all_products_url = products.css("div.row.product-listing-sectionfashion-products a::attr(href)").getall()  # that is for all the products url

        for product in all_products_url:
            yield response.follow(product, callback=self.parse_product_details)

    def parse_product_details(self, response):
        product_desc = response.css('div.product-description')
        for p in product_desc:
            title = p.css("h1::text").get()
            summary = p.css("div.description-block li::text").extract()

            yield {
                "title": title.replace('\n', ''),  # sanitizing the string
                "price": "AED " + p.css("span::text").extract()[4],  # [4] means we're parsing only the 4th index which contains the price
                "product summary": "".join(summary)

            }
