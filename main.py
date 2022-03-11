from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def scrape_top_news():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    browser.get('https://www.youtube.com/channel/UCfLdIEPs1tYj4ieEdJnyNyw') 
    time.sleep(2) 
    followers = browser.find_elements_by_xpath("//yt-formatted-string[starts-with(@id,'subscriber-count')]")
    # print(followers[0].text)

if __name__ == '__main__':
    scrape_top_news()
