from bs4 import BeautifulSoup

parse = BeautifulSoup('<html><head><title>Title of the page</title></head><body><p id="para1 " align="center">This is a paragraph<b>one</b><a href="http://example.com">Example Link 1</a> </p><p id="para2">This is a paragraph<b>Two</b><a href="http://example2.com">Example Link 2</a></p></body></html>')
print(parse.prettify())