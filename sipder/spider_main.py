# encoding=utf-8
import urls, downloader, html_parser, html_outer

class SpiderMain():
    def __init__(self):
        self.urls = urls.Urls()
        self.downloader = downloader.Downloader()
        self.parser     = html_parser.Parser()
        self.html_outer = html_outer.HtmlOuter()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls ,new_data = self.parser.parse(new_url,html_content)
                self.urls.add_new_urls(new_urls)
                self.html_outer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.html_outer.output()




if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/8461.htm"
    spider = SpiderMain()
    spider.craw(root_url)
