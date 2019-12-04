import lxml
import requests
response = requests.get('http://packtpub.com/tech/python')
tree = html.fromstring(response.content)

books = tree.xpath('/html/body/div[2]/main/div[6]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/a/div[3]/div')/text()
print(books)