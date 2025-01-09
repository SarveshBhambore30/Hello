from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def launch_browser(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("headless")
    service_obj = Service("C:\\WebDrivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=options)
    return driver


def launch_hrmURL():
    return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
