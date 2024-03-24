from selenium import webdriver
from booking.constants import BASE_URL
import os


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\Users\shubham359\Desktop\Python\Web_Scrapping\web_scraping_bs4_selenium\geckodriver.exe"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        
    def land_first_page(self):
        self.get(BASE_URL)
        
    