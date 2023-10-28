from enum import unique
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from webscrape.csvWriter import csvWriter
from webscrape.siteseparator import separete
#selenium ile web sitesini a�ar
browser = webdriver.Edge()
linklist = []
browser.get('https://www.bundle.app/gundem') # bunu di�erleri i�in de olu�turmam�z laz�m
#scroll eder
for i in range(0, 20):
    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

leftside = browser.find_element(By.CLASS_NAME,'leftside')
rightside = browser.find_element(By.CLASS_NAME,'rightside')

leftlinks = leftside.find_elements(By.TAG_NAME, 'a')
rigthlinks = rightside.find_elements(By.TAG_NAME,'a')

links = leftlinks + rigthlinks
#as�l linkleri
for link in links:
    linklist.append(link.get_attribute("href"))
linklist = np.array(linklist)
#bundlelinklerini bulma
bundlelinks ,otherlinks = separete(linklist)
#i�eri�i ve kayna�� bulup csvye yazd�rma
csv = csvWriter(bundlelinks)
csv.bundletextGenerate()