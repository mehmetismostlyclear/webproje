from enum import unique
from os import link
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
from webscrape.csvWriter import csvWriter
from webscrape.siteseparator import separete

#edgeoptions = Options()
#edgeoptions.add_argument("--headless")
#selenium ile web sitesini a�ar
browser = webdriver.Edge()
linklist = []

#scroll eder
def get_links():
    linklist=[]
    for i in range(0, 50):
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
    
    print(linklist)
    return linklist
browser.get('https://www.bundle.app/gundem')
list1 = get_links()
browser.get('https://www.bundle.app/yasam')
list2 = get_links()
list1.extend(list2)
browser.get('https://www.bundle.app/finans')
list3 = get_links()
list1.extend(list3)
linklist.extend(list1)

bundlelinks,bbclinks,hurriyetlinks,donanimlinks,ekonomimlinks,gazeteoksijenlinks = separete(linklist)
print(bundlelinks)
#i�eri�i ve kayna�� bulup csvye yazd�rma
csv = csvWriter(bundlelinks,bbclinks)
csv.bundletextGenerate()
csv.bbctextGenerate()