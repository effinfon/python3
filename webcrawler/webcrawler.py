import scrapy

# scrapy.Spider
""" Supposedly each spider has a unique "name" (Primary Key), thus
    there is a Spider container class
    The Webcrawler will use multiple spiders for each request, one
    spider for each search engine. For example, if Google SCholar is
    called with "Memory" as the keyword, then a spider will be created
    that handles all the results from Google; but another spider will
    be create to handle the results from Microsoft Academic for the same
    keyword. As more and more search engines are added, more spiders will
    be created.
"""

# future
""" The webcrawler will explore the world wide web for research sites /
article journals, such as to rely less on search engines. It will steadily
write to a file a database of discovered journals. Whenever a request is made
there will be the option to use +/- search engines, which search engines, or
if to use journals, and which journals.
    There will be two separate categories of urls, one that holds active urls
to journals
"""


class Webcrawler():

    # scrapy.Spider

    # a list of special characetrs used by the url parser
    at = "@ = %40"
    sharp = "# = %23"
    dollar = "$ = %24"
    percent = "% = %25"
    ampersand = "& = %26"
    plus = "= = %2B"

    """ urlKeyword will have to be transformed into a Url
        what this means is that there are some characters
        that are represented by a different encoding rather
        than just raw char. For example, '@' is replaced by "%40"
        or '#' is replaced by "%23", because these characters are
        specially used by the url parser for something else"""

    def stringToUrl(self):
        pass

    urlPrefix = ["https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=",
                 "https://academic.microsoft.com/search?q="]
    urlPostfix = ["&btnG=", "&f=&orderBy=0&skip=0&take=10"]
    #urlKeyword = ""

    #urlFinal = urlPrefix + urlKeyword + urlPostfix

    def start_requests(self, urlKeyword):
        urlKeyword = self.stringToUrl(urlKeyword)

        for i in range(0, 2):
            yield scrapy.Request(url=self.urlPrefix[i] + urlKeyword + self.urlSuffix[i], callback=self.parseArticles)

    def parseArticles(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('saved file %s' % filename)
