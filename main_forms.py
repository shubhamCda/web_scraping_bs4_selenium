from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


os.environ["PATH"] += r"C:\Users\shubham359\Desktop\Python\Web_Scrapping\web_scraping_bs4_selenium\geckodriver.exe"
driver = webdriver.Firefox()

driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.implicitly_wait(5)

name = driver.find_element(By.ID, "fname")
lastname = driver.find_element(By.ID, "lname")


name.send_keys('Shubham')
lastname.send_keys('Bodalkar')

button = driver.find_element(By.CSS_SELECTOR,  'input[type="submit"]')

button.click() # This will  submit the form
