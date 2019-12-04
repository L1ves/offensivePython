# import required modules
import requests
from bs4 import BeautifulSoup
import urlparse


# Get the page with the requests
response = requests.get(
    'https://www.freeimages.co.uk/galleries/food/breakfast/index.htm')
# Parse the page with BeautifulSoup
parse = BeautifulSoup(response.text)
# Get all image tags
image_tags = parse.find_all('img')

# Get urls to the images
images = [url.get('src') for url in image_tags]
# if no images found in the page
if not images:
	sys.exit('Found No images')
images = [urlparse.urljoin(response.url, url) for url in images]
# Convert relative urls to absolute urls if any
print('Found %s images' % len(images)

# Download images to downloaded folder
for url in images:
	r=requests.get(url)
	f=open('opt/%s', % url.split('.')[-1], 'w')
	f.write(r.content)
	f.close()
	print('Downloaded %s', % url)