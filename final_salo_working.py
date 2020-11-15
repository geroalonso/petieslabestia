from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options
from datetime import date
from twilio.rest import Client

urls = []
base = "https://www.dentalplanet.com/"
for i in range(1,158):
    urls.append((base + str(i))) 

realtor_names = []
realtor_phones = []
for i in urls :
  chrome_options = Options()  
  chrome_options.add_argument("--headless") 
  chrome_options.add_argument("user-agent= G.Alonso Scraper contact me if my bot is behaving intrusively: geronimoalonso@icloud.com")
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #set the search engine
  driver.implicitly_wait(10) #set implicit wait
  driver.get(i) #open the browser
  names = driver.find_elements_by_xpath("//div[contains(@class, 'agent-name')]")
  phones = driver.find_elements_by_xpath("//div[contains(@class, 'agent-phone')]")
  for i in names:
    realtor_names.append(i.text)
  for i in phones:
    realtor_phones.append(i.text)

  print('Process completed ' + str(i) + 'out of 158')

dictionary = dict(zip(realtor_names, realtor_phones))
print(dictionary)



