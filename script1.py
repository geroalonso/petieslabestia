from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://bathforliving-com.3dcartstores.com/crm.asp?action=contactus' #set the website
xmlurl = '/sitemap.xml'
print(url +)
driver = webdriver.Chrome(ChromeDriverManager().install()) #set the search engine
driver.get(url) 



