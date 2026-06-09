import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["sandbox.oxylabs.io"]
    start_urls = [f"https://sandbox.oxylabs.io/products?={page}" for page in range(3)]

    def parse(self, response):
        for card in response.css("div.product-card"):
            link = card.css("a::attr(href)").get()
            yield response.follow(link, callback=self.parse_produto)
            # yield {
            #     "title": card.css("h4.title::text").get(),
            #     "price": card.css("div.price-wrapper::text").get(),
            # }

    def parse_produto(self, response):
        yield {
            "title": response.css("h2.title::text").get(),
            "price": response.css("div.price::text").get(),
        }
