import scrapy

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

def stringToUrl():
    pass


urlPrefix = ["https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=", "https://academic.microsoft.com/search?q="]
urlPostfix = ["&btnG=", "&f=&orderBy=0&skip=0&take=10"]
urlKeyword = ""

urlFinal = urlPrefix + urlKeyword + urlPostfix
