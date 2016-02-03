PATH=$PATH:/usr/local/bin
export PATH
cd /var/www/infinitewritingprompts.com/public_html/nn/data/writingprompts
scrapy runspider append-new-24hours.py
