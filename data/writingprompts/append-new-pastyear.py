'''
Appends to "top last 24 hours" posts to the input file
'''

from __future__ import print_function

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http.request import Request

class IMDbDetailsPageSpider(CrawlSpider):

        name = 'writingprompcrawler'
        allowed_domains = ['reddit.com']
        start_urls = ['https://www.reddit.com/r/WritingPrompts/search?q=flair%3A%28Writing+Prompt%29&restrict_sr=on&sort=new&t=year']

	rules = (
		# Extract links for next pages
		Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div[contains(@class, "nav-buttons")][1]//a[contains(@rel, "next")]')), callback='parse_listings', follow=True),
	)

	def parse_start_url(self, response):
		'''
		Crawl start URLs
		'''

		return self.parse_listings(response)

	def parse_listings(self, response):
		'''
		Extract data from listing pages
		'''

                prompts = open('input.txt','a')
                
                for post_title in response.css('.search-result-header a.search-title::text').extract():
                    print(post_title.lstrip('[').lstrip('wp').lstrip('WP').lstrip('eu').lstrip('EU').lstrip('] ').encode('utf-8') + '\n', file=prompts)
