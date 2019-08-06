import scrapy

class ctSpider(scrapy.Spider):

    name = 'clinic'

    start_urls = ['https://clinicaltrials.gov/ct2/show/NCT04006106']

    def parse(self, response):

        table = response.xpath('//*[@class="ct-layout_table"]')[0]

        rows = table.xpath('//tr')

        for row in rows:

            string = " ".join(row.xpath('td//text()').extract()).strip()
            string.replace('\n', '')
            string.replace('\r', '')
            string.strip()
            if ":" in string:
                arr = string.split(':')
                for a in arr:
                    a.strip()
                    a.replace('\n', '')
                print(arr)
                yield {
                    'title': arr[0],
                    'data': arr[1]
                }
            else:
                string.strip()
                string.strip('\n')
                print(string)