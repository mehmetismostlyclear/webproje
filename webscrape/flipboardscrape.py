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
        for i in range(0, 1):
            self.browser.execute_script("window.scrollBy(0, 800);")
            time.sleep(2)
            try:
                item = self.browser.find_element(By.CLASS_NAME, 'page')
                itemlinks = item.find_elements(By.TAG_NAME, 'h3')
                for link in itemlinks:
                    link = link.find_element(By.TAG_NAME, 'a')
                    link_url = link.get_attribute("href")
                    print(link_url)
                    link_url = self.get_final_url(str(link_url))
                    print(link_url)
  

                    linklist.append(link_url)
            except Exception as e:
                print("link geCersiz", e)
        return linklist
    def get_final_url(self, initial_url):
    # Initialize the WebDriver with the path to the WebDriver executable
        driver = webdriver.Edge()
    
        try:
            driver.get(initial_url)
            final_url = driver.current_url
            return final_url
        except Exception as e:
            print("An error occurred:", e)


    def close_browser(self):
        self.browser.quit()

scraper = FlipboardScraper()
scraper.signup("1030510349@erciyes.edu.tr", "Azj9ker2.")
#haberturk_links = scraper.changetheMedia('https://flipboard.com/@haberturk/habert-rk-g-ndem-o7g9qt57z')
#ntv_links = scraper.changetheMedia('https://flipboard.com/@ntv/g-ndem-u4u56601z')
#milliyet_links = scraper.changetheMedia('https://flipboard.com/@milliyet/milliyet-g-ndem-b3orrn0hz')
sabah_links = scraper.changetheMedia('https://flipboard.com/@sabahcomtr/g-ndem-auklra25z')
scraper.close_browser()
csv = csvWriter()
#csv.ntvtextGenerator(ntv_links)
#csv.haberturktextGenerator(haberturk_links)
#csv.milliyettextGenerator(milliyet_links)
csv.sabahtextGenerator(sabah_links)
csv.write_list_to_csv('11-5-23')

