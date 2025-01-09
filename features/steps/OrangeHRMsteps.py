from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.browser_setup import launch_browser, launch_hrmURL


@given('launch chrome browser')
def launchBrowser_steps(context):
    context.driver = launch_browser
    print("Browser launched successfully.")


@when('open orange hrm homepage')
def openHomepage(context):
    #context.driver.get(launch_hrmURL())
    #ontext.driver = launch_hrmURL
    try:
        url = launch_hrmURL()
        context.driver.get(url)
        print(f"Opened URL: {url}")
    except Exception as e:
        print(f"Error opening URL: {e}")


@then('verify that the logo present on page')
def verifyLogo(context):
    # logo = context.driver.find_element(By.XPATH, "(//img[@alt='company-branding'])").is_displayed()
    # assert logo is True
    try:
        WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//img[@alt='company-branding'])[1]")))
        logo = context.driver.find_element(By.XPATH, "(//img[@alt='company-branding'])[1]").is_displayed()
        assert logo is True
        print("Logo is present on the page.")
    except Exception as e:
        print("Error finding the logo: ", e)


@then('close browser')
def closeBrowser(context):
    #context.driver.close()
    try:
        context.driver.quit()
        print("Browser closed successfully.")
    except Exception as e:
        print(f"Error closing browser: {e}")
