# Scrapy settings for subjectcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'subjectcrawler'

SPIDER_MODULES = ['subjectcrawler.spiders']
NEWSPIDER_MODULE = 'subjectcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'subjectcrawler (+http://www.yourdomain.com)'
