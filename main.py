from selenium import webdriver
import os
from selenium.webdriver.common.by import By

os.environ["PATH"] += r"C:\Users\shubham359\Desktop\Python\Web_Scrapping\web_scraping_bs4_selenium\geckodriver.exe"
driver = webdriver.Firefox()  # Get local instance of Firefox driver
# Make sure you've downloaded the geckodriver from https://github.com/

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(30)   #time.sleep(30)

my_element = driver.find_element(By.ID,"downloadButton")
my_element.click()
