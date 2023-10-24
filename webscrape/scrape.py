from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy as np

from webscrape.siteseparator import separete

browser = webdriver.Edge()
linklist = []
browser.get('https://www.bundle.app/gundem')
for i in range(0, 1):
    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

leftside = browser.find_element(By.CLASS_NAME,'leftside')
rightside = browser.find_element(By.CLASS_NAME,'rightside')

leftlinks = leftside.find_elements(By.TAG_NAME, 'a')
rigthlinks = rightside.find_elements(By.TAG_NAME,'a')

links = leftlinks + rigthlinks
for link in links:
    linklist.append(link.get_attribute("href"))#numpye �evirilcek
linklist = np.array(linklist)
#�imdi bunu bir fonskiyon �ekline �evirip linklisti bize d�nd�recek �ekilde yazal�m
#her bir listeyi bundleappler ve di�erleri olucak �ekilde katagorize edelim
print(separete(linklist))
