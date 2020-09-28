from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re


url = 'http://bathforliving.com'
driver = webdriver.Chrome(ChromeDriverManager().install()) #set the search engine
driver.get(url)
doc = driver.page_source
emails = list(set(re.findall(r'[\w\.-]+@+[\w\.-]+', doc)))
print(emails)
driver.quit()
print('siguiente')


url = 'https://bathforliving-com.3dcartstores.com/crm.asp?action=contactus' #set the website
driver = webdriver.Chrome(ChromeDriverManager().install()) #set the search engine
driver.get(url)
doc = driver.page_source
emails = list(set(re.findall(r'[\w\.-]+@+[\w\.-]+', doc)))
print(emails)
driver.quit()

