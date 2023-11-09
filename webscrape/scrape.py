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
import re

#edgeoptions = Options()
#edgeoptions.add_argument("--headless")
#selenium ile web sitesini a�ar
browser = webdriver.Edge()
linklist = []

#scroll eder
def get_links():
    linklist=[]
    for i in range(0, 20):
        browser.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

    leftside = browser.find_element(By.CLASS_NAME,'leftside')
    rightside = browser.find_element(By.CLASS_NAME,'rightside')

    leftlinks = leftside.find_elements(By.TAG_NAME, 'a')
    rigthlinks = rightside.find_elements(By.TAG_NAME,'a')


    links = leftlinks + rigthlinks 
    #as�l linkleri
    for link in links:
        link = link.get_attribute("href")
        
        if "web.archive.org" in str(link):
            link = re.sub(r'http://web\.archive\.org/web/\d+/', '', str(link))
        linklist.append(link)
    
    return linklist
def mineNow():
    browser.get('https://www.bundle.app/gundem')
    list1 = get_links()
    browser.get('https://www.bundle.app/yasam')
    list2 = get_links()
    list1.extend(list2)
    browser.get('https://www.bundle.app/finans')
    list3 = get_links()
    list1.extend(list3)
    linklist.extend(list1)
def minePast():
    web_archive_links = [
    #"http://web.archive.org/web/20220126160349/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220405085224/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220409002451/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220428215028/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220517052109/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220528165440/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220607064707/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220712170452/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220823033802/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220908040209/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20220919052609/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20221003112016/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20221016024629/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20221208072443/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20230210173954/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20230326064958/https://www.bundle.app/gundem",
    #"http://web.archive.org/web/20230702193005/https://www.bundle.app/gundem"
    ]
    for link in web_archive_links:
        try:
            browser.get(link)
            list1 =get_links()
            date = re.findall(r'\d+', link)
            return list1, date
            time.sleep(4)
        except:
            print("bu link çalışmadı", link)
        
        
def start():
    linklist, date = minePast()
    #mineNow()
    bundlelinks,bbclinks,hurriyetlinks,donanimlinks,ekonomimlinks,gazeteoksijenlinks,bloomberghtlinks,kayiprihtimlinks,getmidaslinks,haberturklinks = separete(linklist)
    #i�eri�i ve kayna�� bulup csvye yazd�rma
    csv = csvWriter()
    #csv.bundletextGenerate()
    csv.bbctextGenerate(bbclinks)
    csv.donanimtextGenerate(donanimlinks)
    csv.gazeteoksijentextGenerator(gazeteoksijenlinks)
    csv.ekonomimtextGenerate(ekonomimlinks)
    csv.hurriyettextGenerate(hurriyetlinks)
    csv.bloomberghttextGenerator(bloomberghtlinks)
    csv.haberturktextGenerator(haberturklinks)
    csv.write_list_to_csv(date)
    print(csv.df.to_markdown())
    
start()