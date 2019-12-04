import lxml
import requests
import html
response = requests.get('http://packtpub.com/tech/python')
tree = html.fromstring(response.content)

books = tree.xpath('//div[@class=""price-wrapper]')/text()
print(books)