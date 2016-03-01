import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html=urllib.urlopen(url).read()

soup=BeautifulSoup(html)

#Retrieve all of the anchor tags
tags=soup('a')
#print tags[2].get('href',None)

for x in range(0,7):
	url1=tags[17].get('href',None)
	print tags[17].contents[0]
	html1=urllib.urlopen(url1).read()
	soup=BeautifulSoup(html1)
   	tags=soup('a')
	#for tag in tags:
   # Look at the parts of a tag
   		#url1 = tag.get('href', None)
   		#print url1
   		#html=urllib.urlopen(url1).read()
   		#soup=BeautifulSoup(html)
   		#tags=soup('a')