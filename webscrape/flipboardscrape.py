from enum import unique
from os import link
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import re
from webscrape.csvWriter import csvWriter
browser = webdriver.Edge()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FlipboardScraper:
    def __init__(self):
        self.browser = webdriver.Edge()

    def signup(self, email, password):
        self.browser.get("https://flipboard.com/login")
        email_field = self.browser.find_element(By.XPATH, "//input[@type='text']")
        password_field = self.browser.find_element(By.XPATH, "//input[@type='password']")

        email_field.send_keys(email)
        password_field.send_keys(password)

        # Kaydolma iþlemini baþlatýn
        signup_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        signup_button.click()

    def changetheMedia(self, media_url):
        self.browser.get(media_url)
        time.sleep(2)
        self.browser.get(media_url)
        media_links = self.get_linksflipboard()
        return media_links

    def get_linksflipboard(self):
        linklist = []
        for i in range(0, 5):
            self.browser.execute_script("window.scrollBy(0, 600);")
            time.sleep(2)

            item = self.browser.find_element(By.CLASS_NAME, 'page')
            itemlinks = item.find_elements(By.TAG_NAME, 'h3')
            for link in itemlinks:
                link = link.find_element(By.TAG_NAME, 'a')
                link_url = link.get_attribute("href")
                linklist.append(link_url)
        return linklist

    def close_browser(self):
        self.browser.quit()

scraper = FlipboardScraper()
scraper.signup("1030510349@erciyes.edu.tr", "Azj9ker2.")
haberturk_links = scraper.changetheMedia('https://flipboard.com/@haberturk/habert-rk-g-ndem-o7g9qt57z')
ntv_links = scraper.changetheMedia('https://flipboard.com/@ntv/g-ndem-u4u56601z')
milliyet_links = scraper.changetheMedia('https://flipboard.com/@milliyet/milliyet-g-ndem-b3orrn0hz')
scraper.close_browser()
csv = csvWriter(ntv_links, haberturk_links, milliyet_links)
csv.ntvtextGenerator()
csv.haberturktextGenerator()
csv.milliyetlinks
