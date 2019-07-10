## commands/crawl.py
#
from django.core.management.base import BaseCommand
from Farmscrape.Farmscrape.spiders import Farmspider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(Farmspider.Farmspider)
        process.start()

# from scrapy.crawler import CrawlerProcess
# from scrapy.settings import Settings
# from Farmscrape.Farmscrape.spiders import Farmspider
# from Farmscrape.Farmscrape import settings as my_settings
# from django.core.management.base import BaseCommand
#
# class Command(BaseCommand):
#     help = "Release the spiders"
#
#     def handle(self, *args, **options):
#         crawler_settings = Settings()
#         crawler_settings.setmodule(my_settings)
#         process = CrawlerProcess(settings=crawler_settings)
#
#         process.crawl(Farmspider.Farmspider)
#         process.start()
