## basic web crawler in python made to extract all the links from the seed page to related pages.
##not complete yet, just testing the waters.


def union(p,q):
    for item in p:
        if item not in q:
            p.append(item)

            
def get_page(url):  ##returns the content of the page whose url is passed in
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def getNextPos(page): ## gets the url and indicates the position for initiating next search
    start_link=page.find("a href")
    if start_link != -1 :
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url,end_quote
    else :
        return None,0
def getAllLinks(page): ##extracts the links and stores in a list
    links=[]
    while True:
          url,endpos= getNextPos(page)
          if url :
                 links.append(url)
                 page=page[endpos:]
          else :
                 break
    return links


   
def crawl_web(seed): ##crawls the links present in tocrawl and adds to crawled after crawling
    tocrawl=[seed]
    crawled=[]
    while tocrawl:
        p = tocrawl.pop()
     
        if p not in crawled:
            crawled.append(p)
            tocrawl.append(getAllLinks(get_page(p)))
            
    return crawled

def  add_to_index(index,keyword,url): ##entries added to index
    for entry in index:
        if entry[0]==keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword): ##responding to querries by finding entries in index
    ind_list=[]
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return ind_list

def add_page_to_index(index,url,content): ##page added to index
    words=content.split()
    for word in words:
        add_to_index(index,word,url)
    

result = crawl_web("https://www.udacity.com/cs101x/index.html")  ##sample test case
i=0
while i < len(result):
    print result[i]
    i=i+1
index=[]
add_page_to_index(index,"http://dilbert.com", 
                  """
Another strategy is to ignore the fact that you are solowly killing yourself
by not sleeping and exercising enough.
""" ) ##sample test for indexing

print index

print lookup(index,"strategy") ##sample test for responding to querries

