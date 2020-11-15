from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options


'''Breadth first search is an algorithm used for tree transversal on graphs or tree data structures. BFS can be easily implemented
using recursion and data structures like dictionaries and lists.
The algorithm: 
1)Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
2)If there are no remaining adjacent vertices left, remove the first vertex from the queue.
3)Repeat step 1 and step 2 until the queue is empty or the desired node is found.'''
#the graph will be represented by an adjacency list


emails = []
def openscrape(url):
  chrome_options = Options()
  chrome_options.add_argument("--headless") 
  chrome_options.add_argument("user-agent= G.Alonso Scraper contact me if my bot is behaving intrusively: geronimoalonso@icloud.com")
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #set the search engine
  driver.get(url)
  doc = driver.page_source
  emails.extend(list(set(re.findall(r'''
    (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
    (?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
    @(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|
    [0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|
    [a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''', doc)))) #regex to search emails

  href_list = []
  links = driver.find_elements_by_tag_name("a")
  for link in links:
    href_list.append(link.get_attribute('href'))
  driver.quit()
  return href_list
'''This function algorithm is the following:
      1) opens the url defined in the parameter
      2) scrape for emails in said url.
      3) save the emails into a global list
      4) finds all links in url, hereby defined as sons
      5) saves sons into a list '''


def localurlchecker(trial, url):
  base = urlparse('url').netloc
  test = urlparse('trial').netloc
  if base == test:
    return True
  else:
    return False

    '''This function algorithm is the following:
    We are trying to see if the child node is part of the initial url and not a large non local site such as facebook which would
    collapse out system as scraping it approximates to infinity
    1) Receives parameter (trial) which is the child node we are testing to see if it is part of the original site
    2) Receives parameter (url) which is the url from the original node from our site
    3) with netlock whe extract the most basic part of the urls
    4) we compare both netlocs, if they are true, they belong to the same site and the function returns True.
    5) in the other cases it returns false '''

def crawling(baseurl, emaillimit):
  graph = {}
  visited = []
  queue = []
  visited.append(baseurl)
  queue.append(baseurl)

  while queue:
    if len(emails) < emaillimit:
      try:
        s = queue.pop(0)
        openscrape(s)
        print(s)
        graph[s] = openscrape(s)
        for hijo in graph[s]:
          url_local = localurlchecker(hijo, baseurl)
          if hijo not in visited and url_local == True :
            visited.append(hijo)
            queue.append(hijo)
      except:
        continue
    else:
      break
  print(emails)

crawling('https://www.dentalplanet.com/',100)
crawling('https://rtechdental.com/',100)
crawling('https://www.atlasresell.com/',100)
crawling('https://www.useddentalequipment.net/',100)
crawling('https://abcdentalworks.com/',100)
crawling('https://qualitydentalequip.com/',100)
crawling('https://www.recycledental.com',100)
crawling('https://bimedis.com/',100)
crawling('https://dentalequipmentused.net/',100)
crawling('https://www.collinsdentalequipment.com',100)
crawling(r'https://www.idsdental.com',100)
crawling(r'https://dentistmiami.com',100)
crawling(r'https://www.dentalpanam.com',100)
crawling(r'http://www.dent-all.com',100)
crawling(r'http://www.stabident.com/contact.html',100)
crawling(r'https://www.henryschein.com',100)
crawling(r'http://deepakproducts.com',100)
crawling(r'http://www.sunrisedentalequipment.com',100)


with open('emails_file.txt', 'w') as f:
    for email in emails:
        f.write("%s\n" % item)


