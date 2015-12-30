# Learning Web Scraping
# https://docs.python.org/3/library/urllib.html
# urllib is a package that collects several modules for working with URLs:
#  urllib.request for opening and reading URLs
#  urllib.error containing the exceptions raised by urllib.request
#  urllib.parse for parsing URLs
#  urllib.robotparser for parsing robots.txt files

# Beautiful Soup sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.


from urllib.request import urlopen
from pprint import pprint

html = urlopen("http://pythonscraping.com/pages/page1.html")
pprint(html.read())
