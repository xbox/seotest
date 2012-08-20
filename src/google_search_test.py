'''
Created on 2012-8-6

@author: Administrator
'''
import mechanize
from BeautifulSoup import BeautifulSoup
BASE_URL = "http://www.packtpub.com/article-network"
br = mechanize.Browser()
data = br.open(BASE_URL).get_data()
def scrape_links(base_url,data):
    '''Scrape links pointing to the article page'''
    soup = BeautifulSoup(data)
    #
    #
#    links = []
#    for anchor in soup.right.findAll("a"):
#        tmpAttrs =[(str(name), str(value)) for name, value in anchor.attrs]
#        tmpLink = mechanize.Link(base_url = base_url,url = str(anchor['href']),text = str(anchor.string),tag = str(anchor.name),attrs = tmpAttrs)
#        links.append(tmpLink)
    links = [mechanize.Link(base_url = base_url,url = str(anchor['href']),text = str(anchor.string),tag = str(anchor.name),attrs = [(str(name), str(value)) for name, value in anchor.attrs]) for anchor in soup.right.findAll("a")]
    return links
def scrape_articles(data):
    '''Scrape the title and url of all the articles in this page'''
    #
    #
    ARTICLE_URL_PREFIX="http://www.packtpub.com/article-network"
    soup = BeautifulSoup(data)
    articles = [{"title":str(anchor.string),"url":str(anchor["href"])}
                for anchor in [li.a for li in soup.findAll('li')]
                if anchor["href"].startwith(ARTICLE_URL_PREFIX)]
    return articles
def main():
    '''Get article network main page and follow the links to get the whole list of articles available'''
    articles = []
    #Get main page and get links to all article pages
    BASE_URL = "http://www.packtpub.com/article-network"
    br = mechanize.Browser()
    data = br.open(BASE_URL).get_data()
    links = scrape_links(BASE_URL,data)
    #Scrape article in main page
    articles.extend(scrape_articles(data))
    br.back()
    #Output is the list of titles and URLS for each article found
    print ("Article Networkn"
           "----------------")
    print "nn".join(['Title:"%(title)s"nURL:"%(url)s"' %article for article in articles])
if __name__ == "__main__":
    main()