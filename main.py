from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



os.environ["PATH"] += r"C:\Users\shubham359\Desktop\Python\Web_Scrapping\web_scraping_bs4_selenium\geckodriver.exe"
driver = webdriver.Firefox()  # Get local instance of Firefox driver
# Make sure you've downloaded the geckodriver from https://github.com/

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(8)   #time.sleep(30)

my_element = driver.find_element(By.ID,"downloadButton")
my_element.click()

# my_second_element = driver.find_element(By.ID, "myshubha")  #After 8sec we will get error bcz, implicitly wait function

# progress_element = driver.find_element(By.CLASS_NAME,"progress-label")
# print(f"{progress_element.text == 'Completed!'}")  # Returns False
#To solve the above's problem of false, we've define a method below

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'), 
        'Complete!'
        )
    )