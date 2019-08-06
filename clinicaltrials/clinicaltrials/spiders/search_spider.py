import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


from .ctspider import ctSpider

names = ['Status', 'Study Title', 'Conditions', 'Interventions', 'Study Type', 'Phase', 'Sponsor/Collaborator', 'Funder Type',
         'Study Design', 'Outcome Measures', 'Number Enrolled', 'Sex', 'Age', 'NCT Number', 'Other IDs',
         'Title Acronym', 'Study Start', 'Primary Completion', 'Study Completion', 'First Posted', 'Last Update Posted',
         'Results First Posted', 'Locations']

class searchSpider(CrawlSpider):

    name = 'search'

    allowed_domains = ['https://clinicaltrials.gov/ct2/']

    start_urls = ['https://clinicaltrials.gov/ct2/results']

    # rules = (
    #     Rule(LinkExtractor(allow= r'/ct2/show/NCT\d+\?=\d+'), callback= searchSpider.parse_product),
    # )
    #
    # def parse_product(self, response):
    #
    #     table = response.xpath('//*[@class="ct-layout_table"]')[0]
    #
    #     rows = table.xpath('//tr')
    #
    #     for row in rows:
    #
    #         string = " ".join(row.xpath('td//text()').extract()).strip()
    #         string.replace('\n', '')
    #         string.replace('\r', '')
    #         string.strip()
    #         if ":" in string:
    #             arr = string.split(':')
    #             for a in arr:
    #                 a.strip()
    #                 a.replace('\n', '')
    #             print(arr)
    #             yield {
    #                 'title': arr[0],
    #                 'data': arr[1]
    #             }
    #         else:
    #             string.strip()
    #             string.strip('\n')

    def parse(self, response):

        # links = response.css('a').xpath('@href').extract()
        #
        # for link in links:
        #     if str(link).startswith('/ct2/show/NCT'):
        #         print(link)
        #         yield scrapy.Request('https://clinicaltrials.gov' + link, callback=self.parse_product)

        table = response.xpath('//*[@id="theDataTable"]')

        rows = table.xpath('//tr')

        for row in rows[3:103]:

            for i in range(3, len(row.xpath('td'))):
                arr = row.xpath('td[(%d)]//text()' % i).extract()
                string = ", ".join(arr)
                yield {
                    names[i-3]: string
                }




