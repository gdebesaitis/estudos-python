import json
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from scrapy.product_scraper.product_scraper.spiders.products import ProductsSpider

results = []


def on_item_scrapped(item):
    print(f"Item Scraped: {item['title']}")
    results.append(item)


def main():
    process = CrawlerProcess(get_project_settings())
    crawler = process.create_crawler(ProductsSpider)
    crawler.signals.connect(on_item_scrapped, signal=signals.item_scraped)
    process.crawl(crawler)
    process.start()

    with open("products.json", "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    main()
