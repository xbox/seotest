'''
Created on 2012-8-16

@author: Administrator
'''
from BeautifulSoup import BeautifulSoup
import re
#First example
'''html = "<p><b>Test</b></p>"
soup = BeautifulSoup(html)
print soup.prettify()'''
#Finding Tags
'''html = "<p><b>Test</b></p>"
soup = BeautifulSoup(html)
b_tag = soup.find("b")
p_tag = soup.find("p")
print b_tag
print b_tag.string
print p_tag
print p_tag.string'''
#Traversing the parse tree
'''html = "<p><b>Test</b><b>Test2</b></p>"
soup = BeautifulSoup(html)
b_tag = soup.find("b")
p_tag = soup.find("p")
print b_tag
print p_tag.next
print b_tag.parent
print b_tag.nextSibling'''
#Accessing html Attributes
'''html = "<a href='http://www.redsox.com'>2007 world series champions</a>"
soup = BeautifulSoup(html)
a_tag = soup.find("a")
print a_tag
print a_tag["href"]
print a_tag.string'''
#Remember lists from python
'''html = "<p><b>Test</b><b>Test2</b></p>"
soup = BeautifulSoup(html)
b_tags = soup.findAll("b")
print b_tags[0]
print b_tags[1].string'''
#Example from last time
import urllib2
'''url = "http://www.malegislature.gov/People/Senate"
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
a_tags = soup.findAll("a")
for tag in a_tags:
    try:
        if "People/Profile" in tag["href"]:
            print tag
    except:pass
'''
url = "http://www.malegislature.gov/People/Senate"
'''page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
a_tags = soup.findAll("a",attrs = {"title":True})
for tag in a_tags:
    print tag
'''
#Sucess
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
'''a_tags = soup.findAll("a",attrs={"title":True})
for tag in a_tags:
    if "People" in tag["href"]:print tag
'''
#Storing the links
'''links={}
a_tags = soup.findAll("a",attrs={"title":True})
for tag in a_tags:
    if "People" in tag["href"]:links[tag["title"]] = tag["href"]
print links
print "this is" +links["James E. Timilty"]
'''
#Getting the edu info