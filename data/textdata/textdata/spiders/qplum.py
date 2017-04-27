import json

from scrapy.spiders import CrawlSpider
from w3lib.html import remove_tags, remove_tags_with_content


class QplumSpider(CrawlSpider):
    name = 'qplum'
    start_urls = ['https://www.qplum.co/articles/{}.json'.format(i) for i in range(300)]

    def parse(self, response):
        """
        Parse the response page
        """
        # Skip error URLs
        if response.status != 200:
            return

        data = json.loads(response.text)
        data = data['content']

        # Remove <script>, <sup>, <math> tags with the content
        paragraph = remove_tags_with_content(data, which_ones=('script', 'sup', 'math'))
        # Remove the rest of the tags without removing the content
        paragraph = remove_tags(paragraph)

        # Replace &amp; with &
        paragraph = paragraph.replace('&amp;', '&')
        # Replace &#39; with '
        paragraph = paragraph.replace('&#39;', "'")
        paragraph = paragraph.replace('&rsquo;', "'")
        # Replace &nbsp; with a space
        paragraph = paragraph.replace('&nbsp;', ' ')

        # Some more replacements to improve the default tokenization
        for c in ['\n', '\r', '\t']:
            paragraph = paragraph.replace(c, ' ')
        for c in '();.,[]"\'-:/%$+':
            paragraph = paragraph.replace(c, ' {} '.format(c))

        filename = 'qplum_data.txt'
        f = open(filename, 'a')
        f.write(paragraph + '\n')
        f.close()
