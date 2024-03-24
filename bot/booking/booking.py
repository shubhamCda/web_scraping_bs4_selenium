from selenium import webdriver
from booking.constants import BASE_URL
import os
from selenium.webdriver.common.by import By


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\Users\shubham359\Desktop\Python\Web_Scrapping\web_scraping_bs4_selenium\geckodriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:      #if i'm calling exit() it will run browser and suddenly close it to prevent that from happening  teardown=False
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def close_popup(self):
        popup_win = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'
        )
        popup_win.click()

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CLASS_NAME, "f419a93f12")
        currency_element.click()
        selected_curr_ele = self.find_element(By.CLASS_NAME, "abced745f1")
        selected_curr_ele.click()
