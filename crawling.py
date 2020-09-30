from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options  



result = {}

def crawling(url):
	chrome_options = Options()  
	chrome_options.add_argument("--headless") 
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #set the search engine
	driver.get(url)
	doc = driver.page_source
	emails = []
	emails.extend(list(set(re.findall(r'[\w\.-]+@+[\w\.-]+', doc)))) #regex to search emails

	href_list = []
	links = driver.find_elements_by_tag_name("a")
	for link in links:
		href_list.append(link.get_attribute('href'))
	driver.quit()
	
	for href in href_list:
		try: 
			chrome_options = Options()  
			chrome_options.add_argument("--headless") 
			url = href
			driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #set the search engine
			driver.get(url)
			doc = driver.page_source
			emails.extend(list(set(re.findall(r'[\w\.-]+@+[\w\.-]+', doc)))) #regex to search emails
			driver.quit()
			print('Crawling: ' + href)

		except:
			continue

	#remove duplicates
	localemails = [] 
	for i in emails: 
	    if i not in localemails: 
	        localemails.append(i)

	result[url] = localemails

crawling(r'http://bathforliving.com')
print(result)

