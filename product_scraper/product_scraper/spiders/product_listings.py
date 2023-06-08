import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'product_listings'
    start_urls = ['https://www.luluhypermarket.com/en-ae/electronics']

    def parse(self, response):
        subcategories = response.css('div.col-lg-2.col-md-2.col-auto')  # getting all the subcategories
        all_subcategories_url = subcategories.css("div.col-lg-2.col-md-2.col-auto a::attr(href)").getall()  # getting all the subcategories url

        for product in all_subcategories_url:
            yield response.follow(product, callback=self.parse_products)  # callback the parse_product method to parse the product data leads from subcategory page

    def parse_products(self, response):
        products = response.css("div.product-desc")  # getting all the items from products section

        for product in products:
            title = product.css("h3::text").get()
            price = products.css('span.old-price::text').extract_first()
            yield {
                "title": title.replace('\n', ''),
                "price": "AED " + price,
            }







