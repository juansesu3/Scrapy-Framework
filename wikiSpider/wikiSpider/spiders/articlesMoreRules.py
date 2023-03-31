from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticleSpider(CrawlSpider):
	name = 'articles'
	allowed_domains = ['wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
	rules = [
		Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'), callback='parse_items', follow=True, cb_kwargs={'is_article': True}),
		Rule(LinkExtractor(allow='.*'), callback='parse_items', cb_kwargs={'is_article': False})
	]
	def parse_items(self, response, is_article):
		print(response.url)
		title = response.css('#firstHeading>span::text').extract_first()
		if is_article:
			url = response.url
			text = response.xpath('#mw-content-text > div.mw-parser-output').extract()
			lastUpdated = response.css('li#footer-info-lastmod::text')
			lastUpdated = lastUpdated.replace('This page was edited on', '')
			print('Title is: {}'.format(title))
			print('title is: {}'.format(title))
			print('text is : {}'.format(text))
		else:
			print('Title is: {}'.format(title))

			print('This not an article: {}'.format(title))
